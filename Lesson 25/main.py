from hugging import generate
from config import HF_API_KEY

# change it to groq to use groq api and model
print("Welcome to AI prompt engineering learning session!\n\n")

vague = input("Enter a vague prompt")
print("\nResponse to vague prompt is as so:")
print(generate(vague))

specific = input("Enter a more specific prompt")
print("\nResponse to specific prompt is as so:")
print(generate(specific))

context = input("Add proper context to your prompt: ")
print("\nResponse to proper prompt is as so:")
print(generate(context))

print("--- reflect on response--- \n\nAre inputs different?")



