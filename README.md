# Youtube video downloader
This is a youtube video downloader which is task 6. I was not able to run this in vscode so go to anaconda and find the python file and click it in open with option and you will be able to run this and you will also need one time google authentification. I genuinely needed this
To create this project first-
1.open anaconda prompt
2.Type-
  2.1 mkdir my_downloader
  2.2 my_downloader
  2.3 pip install pytubefix
  2.4 notepad downloader.py
3. Create the file and type the code
4. Run the program

# YouTube Video Downloader - Setup Guide (2026 Version)

## Why pytubefix?

In 2026, YouTube has strict bot detection that blocks the original `pytube` library. We use **pytubefix**, a drop-in replacement that works exactly the same but with regular fixes to bypass YouTube's detection.

2. **First-time Authentication** (one-time setup):
   - The terminal will show you a code (e.g., `WXYZ-1234`) and a URL
   - Open the URL in your browser
   - Enter the code when prompted
   - Log in with your Google/YouTube account
   - This proves to YouTube you're human!

3. The video will download to your chosen folder

## How to Use

1. Run the script in VSCode terminal
2. Enter YouTube video URL when prompted
3. Enter destination folder (or press Enter for current directory)
4. Wait for download to complete!

## Example URLs
- Standard video: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
- Short URL: `https://youtu.be/dQw4w9WgXcQ`

## Features
  **OAuth Authentication** - Bypasses YouTube's 2026 bot detection
  **Progressive Streams** - Downloads video + audio merged (up to 720p)
  **Cached Authentication** - Only authenticate once, then reuse
  **Smart Error Handling** - Catches invalid URLs, private videos, network issues
  **Video Info Display** - Shows title, author, duration, views before downloading
  **Multiple Downloads** - Download several videos in one session

## Why This Works in 2026

- **`use_oauth=True`**: YouTube requires authentication to prevent bots. This saves a token on your computer so you can download freely
- **`allow_oauth_cache=True`**: Saves your authentication so you don't need to log in every time
- **`get_highest_resolution()`**: Grabs "progressive" streams (audio + video already merged, usually up to 720p)
- **`RegexMatchError` exception**: Catches URL typos specifically, preventing crashes

## Troubleshooting

**"No module named pytubefix"**
→ Run: `pip install pytubefix` (as mentioned before I installed in anaconda since vs terminal was linking it elsewhere)

**Authentication not working**
→ Delete the OAuth cache file and try again (it's saved in your user directory)

**"Video unavailable"**
→ Video might be private, members-only, or region-locked

**Download is slow**
→ Normal for large/high-quality videos

**Want higher quality than 720p?**
→ You'll need to download video and audio separately and merge them with ffmpeg (more advanced)

