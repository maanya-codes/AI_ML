import speech_recognition as sr
import pyttsx3
from googletrans import Translator, LANGUAGES

engine = pyttsx3.init()

def speak(text, rate=150):
    try:
        engine.setProperty('rate', rate)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Text to speech error: {e}")

def speech_to_text(source_lang="en-US"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            print("No audio detected.")
            return ""

    try:
        print("Recognizing speech...")
        text = recognizer.recognize_google(audio, language=source_lang)
        print(f"You said: {text}")
        return text.strip()
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"API Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    return ""

def select_target_language():
    user_input = input("Enter target language name or code (e.g. french, es, hindi, ja): ").strip().lower()
    
    if user_input in LANGUAGES:
        return user_input

    for code, name in LANGUAGES.items():
        if user_input == name.lower():
            return code

    print("Language not found. Defaulting to Spanish.")
    return "es"

def translate_text(text, target_language="es"):
    try:
        translator = Translator()
        translation = translator.translate(text, dest=target_language)
        lang_name = LANGUAGES.get(target_language, target_language).title()
        print(f"Translated ({lang_name}): {translation.text}")
        return translation.text
    except Exception as e:
        print(f"Translation error: {e}")
        return ""

def main():
    print("--- Dynamic Voice Translator ---")
    target_language = select_target_language()

    while True:
        text = speech_to_text()

        if not text:
            continue

        lower_text = text.lower()

        if "exit" in lower_text or "quit" in lower_text:
            print("Exiting translator...")
            speak("Goodbye")
            break

        if "change language" in lower_text:
            target_language = select_target_language()
            continue

        translated = translate_text(text, target_language=target_language)
        if translated:
            speak(translated)

if __name__ == "__main__":
    main()
