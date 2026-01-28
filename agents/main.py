from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from downloader import get_video_data
from repurposer import repurpose_content
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Enable CORS for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class VideoRequest(BaseModel):
    url: str
    format_type: str = "blog"

@app.get("/")
def read_root():
    return {"status": "ContentFlow Agent Active"}

@app.post("/process")
def process_video(request: VideoRequest):
    try:
        # 1. Download Data
        print(f"Processing URL: {request.url}")
        video_data = get_video_data(request.url)
        
        # 2. Extract Transcript (Simulated or Real)
        # Note: downloader.py currently returns basic dict. 
        # Real implementation would grab subtitles.
        # For MVP, we'll use the description if transcript is missing, or a placeholder.
        transcript = video_data.get('description', '') 
        if not transcript:
             transcript = f"Video Title: {video_data.get('title')}. No description available."

        # 3. Repurpose
        if os.getenv("OPENAI_API_KEY"):
            content = repurpose_content(transcript, request.format_type)
        else:
            content = f"## (Mock) Generated {request.format_type} for {video_data.get('title')}\n\n*Add OPENAI_API_KEY to agents/.env to see real AI output.*\n\nSummary: {transcript[:200]}..."

        return {
            "status": "success", 
            "video": video_data, 
            "generated_content": content
        }
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
