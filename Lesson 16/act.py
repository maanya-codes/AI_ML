import requests
from config import HF_API_KEY

MODEL_ID = "facebook/bart-large-mnli"
API_URL = f"https://router.huggingface.co/hf-inference/models/{MODEL_ID}"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}
TOPICS = ["Sports", "Technology", "Business", "Politics", "Health"]

def fetch_HF(headline: str):
    
    payload = {"inputs": headline, "parameters": {"candidate_labels": TOPICS}}
    
    #res= requests.get(API_URL)
    #print(res)
    res = requests.post(API_URL, headers= HEADERS, json = payload, timeout=30)
    
    if not res.ok:
        raise RuntimeError(f"HF error {res.status_code}: {res.text}")
        
    return res.json()

def display(headline: str, out: list):
    print(f"\n--- Results for: \"{headline}\" ---")
    for item in out:
        label = item.get("label")
        score = item.get("score", 0)
        print(f" * {label}: {score * 100:.2f}%")
    print("-" * 40 + "\n")

#driver code

print("Welcome")
print("Topics: ", ", ".join(TOPICS))
print("exit")

while True:
    headline = input("Enter headline: ").strip()
    if headline.lower() == "exit":
        print("Goodbye!!")
        break
    if not headline:
        print("Empty headline not allowed")
        continue

    try:
        out = fetch_HF(headline)
        if isinstance(out, list) and out and "label" in out[0]:
            display(headline, out)
        
        else:
            print("Something looks wrong!!")
            print("Received unexpected format:", out)
        
    except Exception as e:
        print("OOps something went wrong. Reason: ", e)
        print("Check Internt or the Humppy face API key")