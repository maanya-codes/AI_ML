import requests

def jokes():
    url = "https://official-joke-api.appspot.com/random_joke"
    res = requests.get(url)

    if res.status_code == 200:
        jo = res.json()
        print(jo)
        return f"{jo['setup']} - {jo['punchline']}"
    else:
        return "failed to retrieve"

print("Welcome to the random jokes center!")


while True:
    inp =  input("press Jo for a joke or q to quit: ")
    if inp in ("jo", "JO", "Jo"):
        joke = jokes()
        print(joke)

    elif inp in ("q", "Q"):
        print("Goodbye!!!")
        break

    else:
        print("Invalid Choice!")

