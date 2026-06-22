import requests

def jokes():
    url = "https://catfact.ninja/fact"
    res = requests.get(url)

    if res.status_code == 200:
        jo = res.json()
        return f"{jo['fact']}"
    else:
        return "failed to retrieve"

print("=== Cat facts! ===")
while True:
    inp =  input("press C for a cat fact or q to quit: ")
    if inp in ("c", "C"):
        joke = jokes()
        print(joke)

    elif inp in ("q", "Q"):
        print("Goodbye!!!")
        break

    else:
        print("Invalid Choice!")

