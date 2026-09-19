import random
import speech_recognition as sr
import pyttsx3
from googletrans import Translator

engine = pyttsx3.init()

greetings = [
    "Listening now, please speak...",
    "Ready, speak into your microphone...",
    "Go ahead and say something in English..."
]

unknown_messages = [
    "Could not understand the audio.",
    "Audio was unclear, please try again.",
    "Sorry, I did not catch that."
]

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "There are 10 types of people in the world: those who understand binary, and those who don't.",
    "Why was the computer cold? It left its Windows open."
]

def speak(text, rate=150):
    try:
        engine.setProperty('rate', rate)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Text to speech error: {e}")

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(random.choice(greetings))
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            print("No speech detected within timeout.")
            return ""

    try:
        print("Recognizing speech...")
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"You said: {text}")
        return text.strip()
    except sr.UnknownValueError:
        print(random.choice(unknown_messages))
    except sr.RequestError as e:
        print(f"API Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return ""

def translate_text(text, target_language="es"):
    try:
        translator = Translator()
        translation = translator.translate(text, dest=target_language)
        print(f"Translated text: {translation.text}")
        return translation.text
    except Exception as e:
        print(f"Translation error: {e}")
        return ""

def display_language_options():
    print("Available translation languages:")
    print("1. Hindi (hi)")
    print("2. Tamil (ta)")
    print("3. Telugu (te)")
    print("4. Bengali (bn)")
    print("5. Marathi (mr)")
    print("6. Gujarati (gu)")
    print("7. Malayalam (ml)")
    print("8. Punjabi (pa)")
    print("9. Spanish (es)")

    language_dict = {
        "1": "hi",
        "2": "ta",
        "3": "te",
        "4": "bn",
        "5": "mr",
        "6": "gu",
        "7": "ml",
        "8": "pa",
        "9": "es"
    }

    choice = input("Please select target language (1-9): ").strip()
    selected_lang = language_dict.get(choice)

    if not selected_lang:
        print("Invalid selection, defaulting to Spanish.")
        return "es"

    return selected_lang

def main():
    target_language = display_language_options()
    speech_rate = 150

    print("\nAssistant started. Voice commands: 'joke', 'faster', 'slower', or 'exit'.\n")

    while True:
        text = speech_to_text()

        if not text:
            continue

        lower_text = text.lower()

        if "exit" in lower_text or "quit" in lower_text:
            print("Exiting assistant...")
            speak("Goodbye", speech_rate)
            break

        elif "joke" in lower_text:
            joke = random.choice(jokes)
            print(f"Joke: {joke}")
            speak(joke, speech_rate)

        elif "faster" in lower_text or "speed up" in lower_text:
            speech_rate += 30
            print(f"Speech rate increased to {speech_rate}")
            speak("Speech rate increased", speech_rate)

        elif "slower" in lower_text or "slow down" in lower_text:
            speech_rate = max(80, speech_rate - 30)
            print(f"Speech rate decreased to {speech_rate}")
            speak("Speech rate decreased", speech_rate)

        else:
            translated_text = translate_text(text, target_language=target_language)
            if translated_text:
                speak(translated_text, speech_rate)
                print("Translation spoken out successfully.\n")

if __name__ == "__main__":
    main()
