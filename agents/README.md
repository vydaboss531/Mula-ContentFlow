# ContentFlow Agents

This directory contains the Python agents responsible for backend automation.

## Agents
1.  **YT-Downloader**: Downloads video and extracts transcript using `yt-dlp`.
2.  **Repurposer**: Uses LLMs (OpenAI/Anthropic) to convert transcripts into blogs/tweets.
3.  **GrowthBot**: Automates finding trending videos.

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
