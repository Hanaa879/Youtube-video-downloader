from pytubefix import YouTube
from pytubefix.exceptions import RegexMatchError
import os

def download_video():
    """Download a YouTube video to specified folder"""
    
    print("=" * 50)
    print("YouTube Video Downloader (2026)")
    print("=" * 50)
    
    # Get video URL from user
    video_url = input("\nEnter YouTube video URL: ").strip()
    
    # Get destination folder
    destination = input("Enter destination folder (press Enter for current directory): ").strip()
    
    # Use current directory if none specified
    if not destination:
        destination = os.getcwd()
    
    # Create destination folder if it doesn't exist
    try:
        os.makedirs(destination, exist_ok=True)
    except Exception as e:
        print(f"\n Error creating destination folder: {e}")
        return
    
    try:
        print("\n Fetching video information...")
        print(" First time? You'll need to authenticate with Google (one-time setup)")
        
        # Create YouTube object with OAuth (bypasses bot detection)
        yt = YouTube(video_url, use_oauth=True, allow_oauth_cache=True)
        
        # Display video info
        print(f"\n📹 Title: {yt.title}")
        print(f" Author: {yt.author}")
        print(f" Duration: {yt.length // 60}:{yt.length % 60:02d}")
        print(f" Views: {yt.views:,}")
        
        # Get highest resolution progressive stream (audio + video merged, usually up to 720p)
        print("\n Downloading highest resolution (progressive stream)...")
        stream = yt.streams.get_highest_resolution()
        
        # Download the video
        print(f" Downloading to: {destination}")
        stream.download(output_path=destination)
        
        print(f"\n Download complete!")
        print(f" Saved as: {yt.title}.mp4")
        
    except RegexMatchError:
        # Specific error for invalid YouTube URLs
        print("\n Error, Invalid YouTube URL format")
        print("Make sure the URL looks like:")
        print("  • https://www.youtube.com/watch?v=VIDEO_ID")
        print("  • https://youtu.be/VIDEO_ID")
        
    except PermissionError:
        print("\n Error, Permission denied")
        print("The video might be private or members-only")
        print("Try logging in with a YouTube Premium account that has access")
        
    except Exception as e:
        # Handle other errors
        error_msg = str(e).lower()
        
        if "unavailable" in error_msg or "private" in error_msg:
            print("\n Error, Video is unavailable, private, or age-restricted")
            print("If you have access, try authenticating with your YouTube account")
        elif "network" in error_msg or "connection" in error_msg:
            print("\n Error, Network connection issue")
            print("Check your internet connection and try again")
        else:
            print(f"\n An error occurred: {e}")
        
        print("\nTips:")
        print("• Verify the URL is correct and the video is public")
        print("• Check your internet connection")
        print("• If authentication fails, delete the OAuth cache and try again")

def main():
    """Main function to run the downloader"""
    while True:
        download_video()
        
        # Ask if user wants to download another video
        again = input("\n\nDownload another video? (y/n): ").strip().lower()
        if again != 'y':
            print("\n Thanks for using YouTube Downloader!")
            break
        print("\n")

if __name__ == "__main__":
    main()