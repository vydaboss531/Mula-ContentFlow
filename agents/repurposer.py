from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = None
if os.getenv("OPENAI_API_KEY"):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def repurpose_content(transcript: str, format_type: str = "blog"):
    """
    Uses OpenAI to convert transcript into a specific format.
    """
    if not client:
        return "Error: OPENAI_API_KEY not found. Please add it to agents/.env"

    if not transcript:
        return "No transcript available to repurpose."

    prompt = f"""
    You are an expert content marketer. Your task is to take the following YouTube video transcript and repurpose it into a {format_type}.
    
    Rules:
    - Make it engaging and viral-worthy.
    - Use proper formatting (Markdown for blogs).
    - If it's a blog, include a catchy title.
    - If it's a tweet, make it a thread.
    
    Transcript:
    {transcript[:15000]}  # Truncate to avoid token limits for now
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a professional content creator helper."},
                {"role": "user", "content": prompt}
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error calling OpenAI: {str(e)}"

if __name__ == "__main__":
    # Test with dummy data
    print(repurpose_content("This is a test transcript about AI automation.", "tweet"))
