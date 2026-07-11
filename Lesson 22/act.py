import speech_recognition as sr
from googletrans import Translator
import pygame, tempfile, os, pyttsx3
import asyncio

def speak(text, language="te"):
    eng = pyttsx3.init()
    eng.setProperty("rate", 150)
    voices = eng.getProperty("voices")
    
    if language == "en":
        eng.setProperty("voice", voices[0].id)
    else:
        eng.setProperty("voice", voices[1].id)
        
    eng.say(text)
    eng.runAndWait()
def translated_text(text, target_language="es"):
    translate = Translator()
    translation = asyncio.run(translate.translate(text, dest=target_language))
    print(f"The translated text is: {translation.text}")
    return translation.text

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak something in english here: ")
        recognizer.adjust_for_ambient_noise(source, duration=0.5) 
        audio = recognizer.listen(source)

    try:
        print("Recognizing speech...")
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"You said: {text}")
        return text

    except sr.UnknownValueError:
        print("Audio not clear")
    except sr.RequestError as e:
        print(f"Unable to fetch the API!!! Error: {e}")

    return ""

def display_lang():
    print("Available translation languages!!!")
    print("1. Tamil")
    print("2. Hindi")
    print("3. Telugu")
    print("4. Bengali")
    print("5. Marathi")
    print("6. Gujrati")
    print("7. Malyalam")
    print("8. Punjabi")
    print("9. Kannada")

    choice = input("Please select the language to translate your english audio(1-9): ")

    lang = {
        "1": "ta", "2": "hi", "3": "te", "4": "bn", "5": "mr",
        "6": "gu", "7": "ml", "8": "pa", "9": "kn"
    }

    return lang.get(choice, "te")

#driver code
target_language = display_lang()
original_text = speech_to_text()

if original_text:
    final_translation = translated_text(original_text, target_language=target_language)
    speak(final_translation, language=target_language)