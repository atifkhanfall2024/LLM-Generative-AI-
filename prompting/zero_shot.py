from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key='AIzaSyCo3pCXQN82pNIiJFZLxqbodB9dwHdJGyY',
    base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
)

# zero shot prompting
Zero_Prompt = 'You are a reasoning assistant.Think step-by-step and explain how you reach the answer. your name is Muhammad Atif Khan '

response = client.chat.completions.create(
    model='gemini-2.5-pro',
    messages=[
        {"role":"system" , "content":Zero_Prompt},
        {"role":"user" , "content":"let me tell you why imran khan is in jail"}
    ]
)


print(response.choices[0].message.content)
