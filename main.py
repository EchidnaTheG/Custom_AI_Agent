import os
from dotenv import load_dotenv
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

prompt = sys.argv
prompt_list = prompt[1:]
prompt_string= " ".join(prompt_list)
response = client.models.generate_content(model="gemini-2.0-flash-001", contents=prompt_list)
print(response.text)
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")