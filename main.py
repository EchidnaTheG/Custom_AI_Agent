import os
from dotenv import load_dotenv
import sys
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")




client = genai.Client(api_key=api_key)
prompt = sys.argv

if len(prompt) <= 1:
    sys.exit(1)
else:
    verbose_status= False
    prompt_list = prompt[1:-1]
    if prompt[-1] == "--verbose":
        verbose_status = True
    prompt_string= " ".join(prompt_list)
    messages=[types.Content(role="user", parts=[types.Part(text=prompt_string)])]
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
    print(response.text)
    if verbose_status:
        print(f"User prompt: {prompt_string}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

