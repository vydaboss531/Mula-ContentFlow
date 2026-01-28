import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Configuration
# Niche keywords to search for
KEYWORDS = ["AI tools 2024", "Make money with AI", "Crypto bull run", "Passive income software"]
MAX_RESULTS = 5

import json
import subprocess

def search_trending_videos(keyword: str):
    """
    Search YouTube for trending videos in a niche using yt-dlp (no API key needed).
    """
    print(f"Searching for: {keyword}...")
    try:
        # yi-dlp search command: yt-dlp "ytsearch5:keyword" --dump-json
        command = [
            "yt-dlp",
            f"ytsearch{MAX_RESULTS}:{keyword}",
            "--dump-json",
            "--default-search", "ytsearch",
            "--no-playlist",
            "--flat-playlist", # faster, just gets metadata
            "--skip-download"
        ]
        
        result = subprocess.run(command, capture_output=True, text=True)
        videos = []
        
        # Output is line-delimited JSON objects
        for line in result.stdout.strip().split('\n'):
            if line:
                try:
                    data = json.loads(line)
                    videos.append({
                        "url": data.get("url") or f"https://www.youtube.com/watch?v={data.get('id')}",
                        "title": data.get("title"),
                        "views": data.get("view_count", 0) # Note: flat-playlist might not have view count
                    })
                except:
                    pass
                    
        return videos
    except Exception as e:
        print(f"Search failed: {e}")
        return []

from repurposer import repurpose_content
import datetime

def auto_process_trending():
    """
    Main loop: Search -> Process -> Save
    """
    print("--- Starting Growth Bot ---")
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = f"../growth_report_{timestamp}.md"
    
    with open(report_file, "w") as f:
        f.write(f"# Growth Board Report - {timestamp}\n\n")

    for kw in KEYWORDS:
        print(f"\nSearching for verified viral hits: '{kw}'...")
        videos = search_trending_videos(kw)
        
        for vid in videos[:2]: # Limit to top 2 per keyword to save API credits during test
            print(f"  > Processing: {vid['title']}")
            
            # 1. Get Transcript (Mock/Description for now)
            # In a real run, this would call downloader.get_video_data(vid['url'])
            # We'll simulate it for speed or use the title as context if transcript fails
            context = f"Video Title: {vid['title']}. Video Link: {vid['url']}"
            
            # 2. Generate Tweet Thread
            content = repurpose_content(context, "tweet")
            
            # 3. Save to Report
            with open(report_file, "a") as f:
                f.write(f"## {vid['title']}\n")
                f.write(f"**URL**: {vid['url']}\n\n")
                f.write("### Generated Content\n")
                f.write(content + "\n\n")
                f.write("---\n\n")
            
            print("    [+] Content generated and saved.")

    print(f"\n[SUCCESS] Report generated: {report_file}")
    return report_file

if __name__ == "__main__":
    auto_process_trending()
