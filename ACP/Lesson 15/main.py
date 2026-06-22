import requests
import html
import json

def get_fact(url):
    try:
        res = requests.get(url)
        data = res.json()
        
        if 'text' in data:
            return data['text']
            
        elif 'results' in data and len(data['results']) > 0:
            q = html.unescape(data['results'][0]['question'])
            a = html.unescape(data['results'][0]['correct_answer'])
            return f"{q} \nanswer: {a}"
            
        else:
            return "raw data found:\n" + json.dumps(data, indent=2)
    except:
        return "error in fetching fact"

urls = {
    "1": "https://uselessfacts.jsph.pl/random.json?language=en",
    "2": "https://opentdb.com/api.php?amount=1&category=18",
    "3": "https://opentdb.com/api.php?amount=1&category=23",
    "4": "https://opentdb.com/api.php?amount=1&category=17",
    "5": "https://opentdb.com/api.php?amount=1&category=21",
    "6": "https://opentdb.com/api.php?amount=1&category=12",
    "7": "https://opentdb.com/api.php?amount=1&category=11"
}

while True:
    print("\npick a category:")
    print("1. general")
    print("2. tech")
    print("3. history")
    print("4. science")
    print("5. sports")
    print("6. music")
    print("7. movies")
    print("8. custom url")
    print("0. exit")

    choice = input("\nenter number: ")

    if choice == "0":
        break
        
    if choice in urls:
        url = urls[choice]
    elif choice == "8":
        url = input("enter url: ")
    else:
        print("invalid choice")
        continue

    print("\nfact:\n" + get_fact(url))

    again = input("\nget another one? (y/n): ")
    if again.lower() != 'y':
        break