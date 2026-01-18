from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key='AIzaSyBrCsWNaUbWcwCWnbhnTtPlCsNSa5bQTs8',
    base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
)

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

response = client.chat.completions.create(
    model='gemini-2.5-pro',
    response_format={'type':'json_object'},
    messages=[
        {"role":"system" , "content":Prompt},
        {"role":"user" , "content":"give me road map to become ai developer"}
    ]
)


print(response.choices[0].message.content)
