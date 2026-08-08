import random
import speech_recognition as sr
import pyttsx3
from datetime import datetime

engine = pyttsx3.init()
engine.setProperty('rate', 150)

FUN_FACTS = [
    "Honey never spoils. Archaeologists have found 3000 year old honey that is still edible.",
    "Bananas are curved because they grow towards the sun.",
    "Octopuses have three hearts and blue blood.",
    "A day on Venus is longer than a year on Venus."
]

def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Speech error: {e}")

def set_voice(gender):
    try:
        voices = engine.getProperty('voices')
        if gender == "male":
            engine.setProperty('voice', voices[0].id)
            speak("Voice set to male.")
        elif gender == "female":
            if len(voices) > 1:
                engine.setProperty('voice', voices[1].id)
            else:
                engine.setProperty('voice', voices[0].id)
            speak("Voice set to female.")
    except Exception as e:
        print(f"Could not change voice: {e}")

def get_audio():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
            command = r.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
    except sr.WaitTimeoutError:
        print("Listening timed out.")
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"API Error: {e}")
    except Exception as e:
        print(f"Audio input error: {e}")
    return ""

def respond_to_command(command, user_name):
    if "hello" in command or "hi" in command:
        speak(f"Hello {user_name}! How can I help you today?")
    elif "your name" in command:
        speak("I am your Python voice assistant.")
    elif "date" in command:
        today = datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
    elif "time" in command:
        now = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")
    elif "fact" in command or "fun fact" in command:
        fact = random.choice(FUN_FACTS)
        speak(fact)
    elif "male voice" in command:
        set_voice("male")
    elif "female voice" in command:
        set_voice("female")
    elif "exit" in command or "stop" in command or "bye" in command:
        speak(f"Goodbye {user_name}!")
        return False
    else:
        speak("I'm not sure how to help with that.")
    return True

def main():
    user_name = input("Enter your name: ").strip()
    if not user_name:
        user_name = "friend"

    set_voice("female")
    speak(f"Voice assistant activated. Welcome {user_name}!")

    while True:
        command = get_audio()
        if command:
            if not respond_to_command(command, user_name):
                break

if __name__ == "__main__":
    main()
