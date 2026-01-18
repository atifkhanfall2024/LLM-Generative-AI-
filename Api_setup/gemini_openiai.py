from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key='AIzaSyDlMThqOFVHZQ5AzuWKOjhoDRwJWFxnnts',
    base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
)

response = client.chat.completions.create(
    model='gemini-2.5-pro',
    messages=[
        {"role":"system" , "content":"Hi act as an software enginerr only solve computer science related fields questions as well as ai and data science not solve physics as well as arts subjets questions"},
        {"role":"user" , "content":"do you know about bohr law"}
    ]
)


print(response.choices[0].message.content)
