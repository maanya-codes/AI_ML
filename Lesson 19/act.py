import sys, time, threading
import wave, pyaudio
import numpy as np
import matplotlib.pyplot as plt
import speech_recognition as sr
from speech_recognition import AudioData


stop_event = threading.Event()

def save(audio, rate, width, filename="rec.wav"):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(width)
        wf.setframerate(rate)
        wf.writeframes(audio)

        print(f"Saved: {filename}")

def wait_for_enter():
    input("press enter to stop: ")
    stop_event.set()

def spinner():
    chars = '|/-\\'
    i = 0
    while not stop_event.is_set():
        sys.stdout.write(f"\rRecording...{chars[i % 4]}")
        sys.stdout.flush()
        i += 1
        time.sleep(0.1)
        
    print(" Recording complete!!!! ")
def plot(data, rate, title="Waveform", color='blue'):
    samples = np.frombuffer(data, dtype=np.int16)
    time_axis = np.linspace(0, len(samples) / rate, len(samples))
    
    plt.figure(figsize=(10, 4))
    plt.plot(time_axis, samples, color=color)
    plt.title(title)

    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def transcribe(audio, rate, width):
    recognizer = sr.Recognizer()
    audio = AudioData(audio, rate, width)
    
    try:
        text = recognizer.recognize_google(audio)
        print(f"Transcription: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return "[Could not understand]"
    except sr.RequestError as e:
        print(f"API error: {e}")
        return "[API error]"
def save(audio, rate, width, filename="rec.wav"):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(width)
        wf.setframerate(rate)
        wf.writeframes(audio)

        print(f"Saved: {filename}")

def record():
    p = pyaudio.PyAudio()
    stream = p.open(
    format = pyaudio.paInt16,
    channels = 1,
    rate = 16000,
    input=True,
    frames_per_buffer=1024
    )

    frames = []
    threading.Thread(target = wait_for_enter, daemon= True).start()
    threading.Thread(target = spinner, daemon= True).start()

    while not stop_event.is_set():
        frames.append(stream.read(1024))
    stream.stop_stream()
    stream.close()
    width = p.get_sample_size(pyaudio.paInt16)
    p.terminate()
    stop_event.clear()
    return b''.join(frames), 1600, width
    

print("="*40)
print("Hello this an AI master ASR!!")
print("="*40)
print("Speak into your mic!")

audio, rate, width = record() #assume it does the work

save(audio, rate, width)

transcribe(audio, rate, width)

plot(audio, rate)


