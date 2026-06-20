import requests
import random
import html

URL = f"https://opentdb.com/api.php?amount=10&category=9&type=multiple"

def get_gk_questions():
    response = requests.get(URL)
    
    if response.status_code == 200:
        data = response.json()
        if data['response_code'] == 0 and data['results']:
            return data['results']
            
    return None

data_set = get_gk_questions()

if not data_set:
    print("failed to fetch the mcq's")
    exit()

score = 0
quit_early = False

print("Welcome to the GK quiz")
print("Type 0 to quit \n")


for i,q in enumerate(data_set, 1):
    question = html.unescape(q['question'])
    correct = html.unescape(q['correct_answer'])
    incorrect = [html.unescape(a) for a in q['incorrect_answers']]

    options = incorrect + [correct]
    random.shuffle(options)
    
    print(f"Question {i}: {question}")

    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
        
    while True:
        try:
            inp = input("Enter your answer as 1-4 or 0 to quit: ")
            if inp=='0':
                print("Ok..Goodbye")
                quit_early = True
                break
            choice = int(inp)
            
            if 1 <= choice <= 4:
                break
                
            else:
                print("Choose either 1-4 as answer or 0 to quit")
                
        except ValueError:
            print("Invalid Input")
            
    if quit_early:
        break
        
    if options[choice-1] == correct:
        print("Kudos for the correct answer \n")
        score += 1
    else:
        print("Sorry you entered wrong answer\n")

if quit_early:
    print(f"You answered {score} correct answers before quitting")
    
else:
    print(f"Final score: {score}/10")