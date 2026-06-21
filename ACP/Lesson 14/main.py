import requests
import html
import random
import time

def get_category_choice():
    print("Select a Category:")
    print("1. Any Category")
    print("2. General Knowledge")
    print("3. Science & Nature")
    print("4. Sports")
    
    while True:
        choice = input("Enter category number (1-4): ")
        if choice == '1': return None
        elif choice == '2': return 9
        elif choice == '3': return 17
        elif choice == '4': return 21
        else:
            print("Invalid input. Please enter 1, 2, 3, or 4.")

def fetch_questions(amount=5, category=None):
    url = f"https://opentdb.com/api.php?amount={amount}&type=multiple"
    if category:
        url += f"&category={category}"
        
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get('results', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching questions: {e}")
        return []

def main():
    print("=== Welcome to the Trivia Game! ===")
    print("You have 10 seconds to answer each question.\n")
    
    category_id = get_category_choice()
    print("\nFetching questions...\n")
    
    questions = fetch_questions(amount=5, category=category_id)
    if not questions:
        print("Could not load questions. Exiting.")
        return

    score = 0
    time_limit = 10.0

    for index, q in enumerate(questions, 1):
        category = html.unescape(q['category'])
        question_text = html.unescape(q['question'])
        correct_answer = html.unescape(q['correct_answer'])
        incorrect_answers = [html.unescape(ans) for ans in q['incorrect_answers']]

        options = incorrect_answers + [correct_answer]
        random.shuffle(options)

        print("-" * 40)
        print(f"Question {index} | Category: {category}") 
        print(f"Q: {question_text}")
        
        for i, opt in enumerate(options, 1):
            print(f"  {i}. {opt}")

        start_time = time.time()
        
        answered_correctly = False
        while True:
            user_input = input("\nYour answer (1-4): ")
            end_time = time.time()
            
            if (end_time - start_time) > time_limit:
                print(f"\n⏰ Time's up! You took {end_time - start_time:.1f} seconds.")
                print(f"The correct answer was: {correct_answer}")
                break
            
            if user_input not in ['1', '2', '3', '4']:
                print("Invalid input. Please enter exactly 1, 2, 3, or 4.")
                continue
                
            user_choice_idx = int(user_input) - 1
            if options[user_choice_idx] == correct_answer:
                print("\n✅ Correct!")
                score += 1
            else:
                print(f"\n❌ Incorrect. The correct answer was: {correct_answer}")
            
            break

        time.sleep(1)

    print("=" * 40)
    print("Quiz Complete!")
    print(f"Your final score is: {score} out of {len(questions)}")
    print("=" * 40)

if __name__ == "__main__":
    main()