from openai import OpenAI
from dotenv import load_dotenv
import json
import time
from groq import Groq
import os

load_dotenv()

# client = OpenAI(
#     api_key='AIzaSyDCs0HHAfq_SEFGFr9jwrCtWYg5hZrxUPk',
#     base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
# )

client = Groq(api_key=os.getenv('Groq_Api'))

# chain of tought
Prompt = """

Act as an Ai developer . you should need to work on chain of though process . if some one ask a question then solve it step by step .
first start , then plan think give proper resons why you should use specific thing properly and then give output .

Rules:
- your answer will be properly in json format
- your response will be in proper step by step with explaination 
- also give proper code

Examples:
Q:Suppose some one ask to add n number program write
A: your answer will be in json format step by step first start then plain , reasoning  , output

"""

print('\n\n\n')

# first we need to make message history

message_history = [
    {"role":"system"  , "content":Prompt}
]

User_input = input("👤 ")
message_history.append({"role":"user" , "content":User_input})

while True:
   
     
     response = client.chat.completions.create(
        model='meta-llama/llama-4-maverick-17b-128e-instruct',
        response_format={'type':'json_object'},
        messages=message_history
    )
  
     Api_out =  response.choices[0].message.content
     message_history.append({"role":"assistant" , "content":Api_out})
    
     parse_it = json.loads(Api_out)
   

     if parse_it.get('step') == "start" :
        print("🔥 " , parse_it.get("content"))
        continue
     if parse_it.get('step') == "plan" :
        print("🧠 " , parse_it.get("content"))
        continue
     if parse_it.get('step') == "reasoning" :
        print("📖 " , parse_it.get("content"))
        continue
     if parse_it.get('step') == "output" :
        print("✅ " , parse_it.get("content"))
        break

print('\n\n\n')