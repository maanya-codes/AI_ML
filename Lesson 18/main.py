import requests
from colorama import Fore, Style, init
from config import HF_API_KEY

DEFAULT_MODEL = "facebook/bart-large-cnn"

def summarize(txt, min, max, model):
    payload = {
        "inputs": text,
        "parameters": {"min_length" = min, "max_length" = max}
    }

    print(Fore.BLUE + Style.BRIGHT + f"\n Performing summarization using {model}")

    #fetching the api using a function
    result = fetch(payload, model_name = model)

    if isinstance(result, list) and result and "summary_text" in result[0]:
        return result[0]["summary_text"]
    else:
        print(Fore.RED + "Error", result)

    return None
#driver code or mainpart


#driver code or mainpart

print(Fore.YELLOW + Style.BRIGHT+ "Welcome...Hi whats your name!!!")
name = input("Enter here: ").strip()

if not name:
    name = "user_name"

print(Fore.GREEN + Style.BRIGHT + f"Hi {name} Welcome lets do some AI magic here: ")

print(Fore.GREEN + Style.BRIGHT + "Enter texts to summarize: ")
txt = input(">").strip()

if not txt:
    print(Fore.RED + "No text provided!")
else:
    print(Fore.YELLOW + "Enter the model that you want to use e.g google/pegasus-xsum")
    model = input("Model name(leave blank for default): ")
    if not model:
        model = DEFAULT_MODEL
        
    print(Fore.YELLOW + "Choose your summarization style: ")
    print("1. Standard Summary")
    print("2. Longer Summary")
    summary_type = input("Enter 1 or 2")

    if summary_type == "1":
        min_length = 50
        max_length = 150
        print(Fore.BLUE + "Standard summary chosen")
    else:
        min_length = 80
        max_length = 200
        print(Fore.BLUE + "Enhanced summary chosen")
    summary = summarize(txt, min_length, max_length, model_name = model)
    if summary:
        print(Fore.GREEN + Style.BRIGHT + f"\n AI Summarized output for {name}")
        print(Fore.GREEN + summary)
    else:
        print(Fore.RED + "Failed to generate the AI summary of your text")