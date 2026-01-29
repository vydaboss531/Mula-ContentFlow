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
    Main loop: Search -> Process -> Return results for persistence
    """
    print("--- Starting Growth Bot ---")
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = f"../growth_report_{timestamp}.md"
    discoveries = []
    
    with open(report_file, "w") as f:
        f.write(f"# Growth Board Report - {timestamp}\n\n")

    for kw in KEYWORDS:
        print(f"\nSearching for verified viral hits: '{kw}'...")
        videos = search_trending_videos(kw)
        
        for vid in videos[:2]: # Limit for speed/API cost
            print(f"  > Processing: {vid['title']}")
            
            # 1. Get Context
            context = f"Video Title: {vid['title']}. Video Link: {vid['url']}"
            
            # 2. Generate
            content = repurpose_content(context, "tweet")
            
            # 3. Store result
            discovery = {
                "title": vid['title'],
                "url": vid['url'],
                "content": content,
                "format": "tweet"
            }
            discoveries.append(discovery)
            
            # 4. Save to Local Report
            with open(report_file, "a") as f:
                f.write(f"## {vid['title']}\n")
                f.write(f"**URL**: {vid['url']}\n\n")
                f.write("### Generated Content\n")
                f.write(content + "\n\n")
                f.write("---\n\n")
            
            print("    [+] Content generated and stored.")

    print(f"\n[SUCCESS] Report generated: {report_file}")
    return discoveries

if __name__ == "__main__":
    auto_process_trending()
