from transformers import pipeline

# Create a text-generation pipeline
pipe = pipeline("text-generation", model="google/gemma-3-270m-it")

# Ask a question
output = pipe("Who are you?", max_length=50)

# Print the answer
print(output)
