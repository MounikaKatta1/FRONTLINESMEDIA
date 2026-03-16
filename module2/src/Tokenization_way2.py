import os
from dotenv import load_dotenv
from google import genai

load_dotenv("D:/FLM-Mounika/Assignments/module2/.env")

# API KEY
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configuration API (GEMINI)
client = genai.Client(api_key=GEMINI_API_KEY)

sentence = " Hello Prabhavathi!Welcome To AI Mastery Crash Course forbetter future"

prompt = f'''
Tokenize the following sentence and return tokens and token_ids

Sentence : {sentence}

Return result in this format

Tokens : [...]
Token_ids : [...]

(Generate numeric_ids for demonstration)
'''

resp = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents=prompt
)

print(resp.text)