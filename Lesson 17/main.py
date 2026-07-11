import requests, re, random
from config import HF_API_KEY

MODEL = "sentence-transformers/all-MiniLM-L6-V2"
API_URL = f"https://router.huggingface.co/hf-inference/models/{MODEL}"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}
TH = 0.75


TOK = lambda s: " | ".join(s.split())
bar = lambda s: "█"*int(s*10)+"░"*(10-int(s*10))
clean = lambda t: [w for w in (re.sub(r"[^a-z0-9']+", "", x.lower()) for x in t.split()) if w]
nums = lambda t: set(re.findall(r"\d+(?:\.\d+)?", t))
has = lambda t, arr: any(a in set(clean(t)) for a in arr)

#The api fetch part
def hf(q1, q2):
    payload = {"inputs": {"source_sentence": q1, "sentences":[q2]}}
    
    #res= requests.get(API_URL)
    #print(res)
    res = requests.post(API_URL, header= HEADERS, json = payload, timeout=30)
    data = res.json()
    if not res.ok:
        raise RuntimeError(f"HF error {res.status_code}: {res.text}")
        
    return float (data[0])

#The operation function

def oper(q1, q2, heading):
    print(f"-----{heading}: ------")
    base = hf(q1, q2)
    strong = sorted({w for w in clean(q1) if len(w)>=4} & {w for w in clean(q2) if len(w)>=4})
    s = score(base, q1, q2, strong)
    display(s)
    showF(q1, q2)

print("Welcome")
print("Type 2 sentences , type exit to quit!!")
print("exit")

while True:
    ques1 = input("Enter question 1 or sentence 1: ").strip()
    if ques1.lower() == "exit":
        print("Goodbye!!")
        break

    ques2 = input("Enter question 2 or sentence 2: ").strip()
    if ques2.lower() == "exit":
        print("Goodbye!!")
        break


    if not ques1 or not ques2:
        print("Empty sentence not allowed")
        continue

    try:
        out = oper(ques1, ques2, "Your questions")
    
        
        if isinstance(out, list) and out and "label" in out[0]:
            display(headline, out)
        
        else:
            print("Something looks wrong!!")
            print("Received unexpected format:", out)
        
    except Exception as e:
        print("OOps something went wrong. Reason: ", e)
        print("Check Internt or the Humppy face API key")