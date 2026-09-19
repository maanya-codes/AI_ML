import random
import speech_recognition as sr
import pyttsx3
from googletrans import Translator

engine = pyttsx3.init()

GREETINGS = [
    "Listening now, please speak...",
    "Ready! Say something in English...",
    "Go ahead, speak into your microphone..."
]

UNKNOWN_RESPONSES = [
    "Sorry, I couldn't understand that.",
    "I didn't catch what you said. Please try again.",
    "Audio was unclear, could you repeat that?"
]

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "There are 10 types of people in the world: those who understand binary, and those who don't.",
    "Why was the computer cold? It left its Windows open."
]


def speak(text, rate=150):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()


def speech_to_text():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print(random.choice(GREETINGS))
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        
        try:
            audio = recognizer.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            print("Listening timed out. No input detected.")
            return ""

    try:
        print("Recognizing speech...")
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"You said: {text}")
        return text.strip()
    except sr.UnknownValueError:
        print(random.choice(UNKNOWN_RESPONSES))
        return ""
    except sr.RequestError as e:
        print(f"Speech recognition service error: {e}")
        return ""


def translate_text(text, target_language="es"):
    try:
        translator = Translator()
        translation = translator.translate(text, dest=target_language)
        print(f"Translated text: {translation.text}")
        return translation.text
    except Exception as e:
        print(f"Translation failed: {e}")
        return ""


def display_language_options():
    print("Available target languages:")
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

    choice = input("Select language number (1-9): ").strip()
    selected_lang = language_dict.get(choice)

    if not selected_lang:
        print("Invalid selection. Defaulting to Spanish (es).")
        return "es"
        
    return selected_lang


def main():
    target_language = display_language_options()
    speech_rate = 150
    
    print("\n--- Assistant Started ---")
    print("Custom controls available: 'joke', 'faster', 'slower', or 'exit'\n")

    while True:
        original_text = speech_to_text()

        if not original_text:
            continue

        lower_text = original_text.lower()

        if "exit" in lower_text or "quit" in lower_text:
            print("Closing application...")
            speak("Goodbye!", speech_rate)
            break

        elif "joke" in lower_text:
            joke = random.choice(JOKES)
            print(f"Joke: {joke}")
            speak(joke, speech_rate)

        elif "faster" in lower_text or "speed up" in lower_text:
            speech_rate += 30
            print(f"Speech rate set to {speech_rate} WPM")
            speak("Speech rate increased", speech_rate)

        elif "slower" in lower_text or "slow down" in lower_text:
            speech_rate = max(80, speech_rate - 30)
            print(f"Speech rate set to {speech_rate} WPM")
            speak("Speech rate decreased", speech_rate)

        else:
            translated_text = translate_text(original_text, target_language=target_language)
            if translated_text:
                speak(translated_text, speech_rate)
                print("Translation spoken successfully.\n")


if __name__ == "__main__":
    main()
