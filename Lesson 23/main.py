import speech_recognition as sr
import pyttsx3
from datetime import datetime

def speak(text):
    print(f"Assistant: {text}")
    eng = pyttsx3.init()
    eng.setProperty("rate", 150)
    eng.say(text)
    eng.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("== Speak now ==")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Could not understand")
        except sr.RequestError as e:
            print("API not working")
    return ""

def respond(command):
    if "hello" in command:
        speak("Hey, man. You want help or what?")
    elif "name" in command:
        speak("Your mom. Thats personal info, stalker.")
    elif "time" in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"The time is: {now}")
    elif "exit" in command:
        speak("Goodbye")
        return False
    else:
        speak("Sorry I cannot hear you, I'm kinda busy")
    return True

speak("Voice Assistant activated. Say something")

while True:
    command = get_audio()
    if command:
        if not respond(command):
            break