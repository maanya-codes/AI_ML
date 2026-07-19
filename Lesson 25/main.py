import time
import requests
from colorama import Fore, Style, init
from config import HF_API_KEY

init(autoreset=True)

DEFAULT_MODEL = "facebook/bart-large-cnn"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}

def summarize(txt, min_len, max_len, model):
    url = f"https://api-inference.huggingface.co/models/{model}"
    payload = {
        "inputs": txt,
        "parameters": {"min_length": min_len, "max_length": max_len}
    }

    print(Fore.BLUE + Style.BRIGHT + f"\nPerforming summarization using {model}...")

    try:
        res = requests.post(url, headers=HEADERS, json=payload, timeout=15)
        result = res.json()

        if isinstance(result, dict) and "estimated_time" in result:
            wait = result["estimated_time"]
            print(Fore.YELLOW + f"Model is waking up... waiting {wait:.1f}s")
            time.sleep(wait)
            return summarize(txt, min_len, max_len, model)

        if isinstance(result, list) and result and "summary_text" in result[0]:
            return result[0]["summary_text"]
        else:
            print(Fore.RED + f"Error response: {result}")
            return None
            
    except Exception as e:
        print(Fore.RED + f"Network/API Error: {e}")
        return None

print(Fore.YELLOW + Style.BRIGHT + "Welcome...Hi whats your name!!!")
name = input("Enter here: ").strip()

if not name:
    name = "user_name"

print(Fore.GREEN + Style.BRIGHT + f"Hi {name}! Let's do some AI magic here: ")
print(Fore.GREEN + Style.BRIGHT + "Enter text to summarize: ")
txt = input("> ").strip()

if not txt:
    print(Fore.RED + "No text provided!")
else:
    print(Fore.YELLOW + "\nEnter the model that you want to use (e.g., google/pegasus-xsum)")
    model = input("Model name (leave blank for default): ").strip()
    if not model:
        model = DEFAULT_MODEL
        
    print(Fore.YELLOW + "\nChoose your summarization style: ")
    print("1. Standard Summary")
    print("2. Longer Summary")
    summary_type = input("Enter 1 or 2: ").strip()

    if summary_type == "1":
        min_length = 50
        max_length = 150
        print(Fore.BLUE + "Standard summary chosen")
    else:
        min_length = 80
        max_length = 200
        print(Fore.BLUE + "Enhanced summary chosen")
        
    summary = summarize(txt, min_length, max_length, model)
    
    if summary:
        print(Fore.GREEN + Style.BRIGHT + f"\nAI Summarized output for {name}:")
        print(Fore.WHITE + summary)
    else:
        print(Fore.RED + "Failed to generate the AI summary of your text.")