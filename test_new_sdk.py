import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

try:
    from google import genai
    print("genai imported successfully")
except ImportError:
    print("google-genai not installed yet")
