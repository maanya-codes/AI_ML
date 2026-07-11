import time
import requests
from config import HF_API_KEY

MODEL_URL = "https://api-inference.huggingface.co/models/mrm8488/bert-tiny-finetuned-sms-spam-detection"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}

def run_inference(text_input):
    try:
        res = requests.post(MODEL_URL, headers=HEADERS, json={"inputs": text_input}, timeout=10)
        res.raise_for_status()
        output = res.json()
        
        if isinstance(output, dict) and "estimated_time" in output:
            delay = output["estimated_time"]
            print(f"\n[System] Model is loading. Retrying in {delay:.1f}s...")
            time.sleep(delay)
            return run_inference(text_input)
            
        return output
    except Exception as err:
        print(f"\n[!] Connection error: {err}")
        return None

def process_and_show(data):
    if not data or not isinstance(data, list):
        print("[!] Could not process response data.")
        return

    try:
        scores = data[0]
        top_match = max(scores, key=lambda val: val["score"])
        
        label_str = top_match["label"].upper()
        pct = top_match["score"] * 100
        
        is_spam = "SPAM" in label_str or "1" in label_str
        verdict = "🚨 SPAM DETECTED" if is_spam else "✅ SAFE / HAM"
        
        print("\n" + "~" * 40)
        print(f" Verdict: {verdict} ({pct:.1f}%)")
        print("~" * 40)
        for item in scores:
            clean_name = "Spam" if ("SPAM" in item["label"].upper() or "1" in item["label"]) else "Safe"
            print(f" - {clean_name}: {item['score'] * 100:.1f}%")
        print("~" * 40 + "\n")
        
    except Exception:
        print(f"[!] Parsing error. Raw payload: {data}")

def start_app():
    print("--- Spam Classification Tool Loaded ---")
    print("Commands: 'exit' or 'quit' to close.\n")
    
    while True:
        prompt = input("Enter text: ").strip()
        
        if not prompt:
            continue
            
        if prompt.lower() in ["exit", "quit"]:
            print("Closing application.")
            break
            
        print("Analyzing payload...")
        api_data = run_inference(prompt)
        process_and_show(api_data)

if __name__ == "__main__":
    start_app()