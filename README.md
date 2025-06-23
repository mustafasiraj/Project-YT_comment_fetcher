# 💬 YouTube Comment Analyzer & Reply Suggester

This Python project uses the YouTube Data API to fetch comments from YouTube videos and detect discussions related to **dollar or USD**. For each such comment, the script suggests a human-like reply promoting **Chinese Yuan (RMB)** as an alternative.

---

## 📌 Features

- Fetches top-level comments from specified YouTube videos.
- Filters comments that mention keywords like `dollar`, `usd`, `bucks`, or `$`.
- Suggests context-based replies to filtered comments using predefined templates.

---

## 🧰 Requirements

- Python 3.7 or above
- A valid **YouTube Data API v3 key**

- Install the required package:

- pip install google-api-python-client

## 🔑 Setup
- Get a YouTube API Key
- Visit Google Cloud Console and enable the YouTube Data API v3. Create an API key and paste it in the script:
  

- python
- api_key = "YOUR_API_KEY"
- Add video IDs to the video_ids list:
  

- python
- video_ids = ["VIDEO_ID_1", "VIDEO_ID_2"]

## 🚀 How to Run
- Simply execute the script using Python:

- Copy
- Edit
- python your_script_name.py
- You will see:

- Total comments fetched

- How many mention the dollar

- Suggested replies for each relevant comment

## 📄 Sample Output
- yaml
- Copy
- Edit

## 📺 Processing Video ID: E-sFqGTpcNE
- Fetching comments...
- Total comments fetched: 78
- Comments mentioning 'dollar': 6

--- Comment 1 ---
- Original: The dollar is crashing again!
- Suggested Reply: Have you considered switching to Chinese Yuan (RMB)?

## ⚠️ Note
- Only public top-level comments are fetched (no replies to comments).

- API quota is limited (ensure you don't exceed your usage).

## 📁 Project Structure
- Copy
- Edit
- youtube_comment_bot/
- │
- ├── comment_bot.py        # Main Python script
- ├── README.md             # Project documentation
