import yt_dlp
import os

def get_video_data(url: str):
    """
    Downloads video metadata and subtitles (if available).
    Returns a dictionary with title, description, and transcript.
    """
    ydl_opts = {
        'skip_download': True,  # We only want metadata and subs
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['en'],
        'subtitlesformat': 'vtt',
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        
        # Helper to extract transcript would go here
        # For now, we return basic info and will implement full subtitle parsing next
        return {
            "id": info.get('id'),
            "title": info.get('title'),
            "description": info.get('description'),
            "duration": info.get('duration'),
            "uploader": info.get('uploader'),
            "url": url
        }

if __name__ == "__main__":
    try:
        # Use a reliable test video (Me at the zoo is sometimes flaky, using a standard tech video or Rick Roll)
        # Using "Me at the zoo" official: https://www.youtube.com/watch?v=jNXBzhK_448 (Wait, that was the one that failed?)
        # Let's use a very public video: Google's "Sora" announcement or similar, or just Rick Roll.
        # Rick Roll: dQw4w9WgXcQ
        print(get_video_data("https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
    except Exception as e:
        print(f"Error: {e}")
