import speech_recognition as sr
from googletrans import Translator
import pygame, tempfile, os
from gtts import gTTS
import asyncio


def translated_text(text, target_language="te"):
    translate = Translator()
    translation = asyncio.run(translate.translate(text, dest=target_language))
    print(f"The translated text is: {translation.text}")
    return translation.text

def speak(text, language="te"):
    try:
        print(f"Speaking: {text[:50]}... ")
        tts = gTTS(text=text, lang=language, slow=False)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            temp_file = f.name
        tts.save(temp_file)

        pygame.mixer.init()
        pygame.mixer.music.load(temp_file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.wait(100)

        pygame.mixer.quit()
        os.remove(temp_file)
        print("Audio played successfullyyyyyyyyyyyyyyy")
        return True        

    except Exception as e:
        print(f"API Issue, {e}")
        return False
    
    
def speech_to_text():
    recogniser = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something in english...")
        audio = recogniser.listen(source=source)

    try:
        print("Recognising speech. . .  ")
        text = recogniser.recognize_google(audio, language="en-US")
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Audio is not clear")
    except sr.RequestError as e:
        print(f"Unable to fetch API")
    
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

    choice = input("Select language to translate (1-9): ")
    lang = {
        "1": "ta", "2": "hi", "3": "te", "4": "bn", "5": "mr",
        "6": "gu", "7": "ml", "8": "pa", "9": "kn"
    }

    return lang.get(choice, "te")
#driver code ===
target_language = display_lang()
original_text = speech_to_text()

if original_text:
    final_translation = translated_text(original_text, target_language=target_language)
    speak(final_translation, language=target_language)
    print("Translated audio into language of your choice")