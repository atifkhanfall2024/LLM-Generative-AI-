import os
from dotenv import load_dotenv
from openai import OpenAI
from groq import Groq


load_dotenv()

client = Groq(api_key=os.getenv('API_KEY'))

response = client.chat.completions.create(
    model='llama-3.3-70b-versatile',
    messages=[
        {"role":"user" , "content":"which model you have used"}
    ]
)

print(response.choices[0].message.content)