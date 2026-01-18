from google import genai
import os

client = genai.Client(api_key='AIzaSyDlMThqOFVHZQ5AzuWKOjhoDRwJWFxnnts')

response = client.models.generate_content(
    model='gemini-2.5-pro',
    contents='which model you have used'
)


print(response.text)

