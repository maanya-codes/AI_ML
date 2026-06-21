import requests

url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"

def get_fact():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Random Fact: {data['text']}")
    else:
        print("Failed to fetch fact")
    
print("== Welcome to the Useless Facts Centre ==")
while True:
    print("\n=============================\n")
    print("Enter:\nN: For next fact\nQ: quit")
    inp = input("Your choice: ")
    if inp in ("q", "Q"):
        print("Exiting....")
        break
    elif inp in ("N", "n"):
        get_fact()
    else:
        print("Invalid Choice!")
        continue

    

 

