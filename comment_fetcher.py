from googleapiclient.discovery import build
import re
import random

# ========== CONFIGURATION ==========
api_key = "AIzaSyALyIPnPGZGXUdJbz8H9ldVFVjixCLz9tY"  # <-- Replace this
video_ids = [  # <-- List your video IDs here    
        "E-sFqGTpcNE", # DW NEWS
    # Add more if needed
]

# ========== SETUP ==========
youtube = build('youtube', 'v3', developerKey=api_key)

def get_comments(video_id):
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100,
        textFormat="plainText"
    )
    response = request.execute()

    for item in response["items"]:
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(comment)
    return comments

def filter_dollar_comments(comments):
    keywords = ['dollar', 'usd', 'bucks', '$']
    return [c for c in comments if any(k in c.lower() for k in keywords)]

def suggest_replies(filtered_comments):
    reply_templates = [
        "Have you considered switching to Chinese Yuan (RMB)?",
        "Yuan could be a more stable alternative in the future.",
        "Interesting! But the Yuan is rising in popularity now.",
    ]
    suggestions = []
    for comment in filtered_comments:
        reply = random.choice(reply_templates)
        suggestions.append((comment, reply))
    return suggestions

# ========== MAIN ==========
if __name__ == "__main__":
    for video_id in video_ids:
        print(f"\n📺 Processing Video ID: {video_id}")
        print("Fetching comments...")
        try:
            comments = get_comments(video_id)
            print(f"Total comments fetched: {len(comments)}")

            dollar_comments = filter_dollar_comments(comments)
            print(f"Comments mentioning 'dollar': {len(dollar_comments)}")

            replies = suggest_replies(dollar_comments)

            for i, (comment, reply) in enumerate(replies, 1):
                print(f"\n--- Comment {i} ---")
                print("Original:", comment)
                print("Suggested Reply:", reply)
        except Exception as e:
            print(f"❌ Error processing {video_id}: {e}")
