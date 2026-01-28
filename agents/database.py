import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

class DB:
    def __init__(self):
        self.supabase: Client = None
        if url and key:
            self.supabase = create_client(url, key)

    def save_job(self, video_url: str, title: str, format_type: str, result: str):
        """
        Save a generated job to the database.
        """
        if not self.supabase:
            print("DB: Skipping save (No Supabase credentials)")
            return
            
        data = {
            "video_url": video_url,
            "title": title,
            "format_type": format_type,
            "content": result,
            "status": "completed"
        }
        
        try:
            self.supabase.table("jobs").insert(data).execute()
        except Exception as e:
            print(f"DB Error: {e}")

    def get_jobs(self):
        """
        Get last 10 jobs.
        """
        if not self.supabase:
            return []
        try:
            response = self.supabase.table("jobs").select("*").order("created_at", desc=True).limit(10).execute()
            return response.data
        except:
            return []

db = DB()
