# Gen Ai
- api keys from here = https://console.groq.com/keys
- then use a model

# also used google studio apis for free
- pip install google-genai
- then i used that 
- goes to pricing and check free trails

# now how we use that gemini api as a open ai 
- same code as for groq and also for openai only with additional lines add api key and based url inside openai function 



## Advance prompt enginerring
- zero shot
- one shot
- few shot
- chian of thought
- Automated chain of tought
- persona based prompting



## Hugging Face 
  - hugging face is like a github for ai models where we use ai models build  , use and share models spaces and datasets

## how work 
 - User Input
   │
   ▼
"Who are you?"
   │
   ▼
┌─────────────────────────────┐
│  Hugging Face Pipeline      │
│  (text-generation task)     │
└─────────────────────────────┘
   │
   ▼
┌─────────────────────────────┐
│   Transformer Model          │
│  (google/gemma-3-270m-it)   │
│  - Understands input text    │
│  - Predicts next words       │
└─────────────────────────────┘
   │
   ▼
Python Output
[{'generated_text': "I am Gemma, an AI assistant here to help you."}]
   │
   ▼
Print to Screen
"I am Gemma, an AI assistant here to help you."
