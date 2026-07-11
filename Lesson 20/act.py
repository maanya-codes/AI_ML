import threading
import sys
import time, pyaudio, numpy as np, matplotlib.pyplot as plt, wave, speech_recognition as sr
from speech_recognition import AudioData

stop_event = threading.Event()
# Defining the Sample Rate globally keeps things consistent
SAMPLE_RATE = 16000 

def analyze_audio(data, rate):
    """Analyze audio data and extract metrics."""
    samples = np.frombuffer(data, dtype=np.int16)
    duration = len(samples) / rate
    avg_amplitude = np.mean(np.abs(samples)) if len(samples) > 0 else 0
    max_amplitude = np.max(np.abs(samples)) if len(samples) > 0 else 0
    
    return {
        'duration': duration,
        'avg_amplitude': avg_amplitude,
        'max_amplitude': max_amplitude
    }

def plot_waveform(data, rate, title="Waveform", color='blue'):
    """Plot audio waveform."""
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

def compare_recordings(rec1, rec2):
    """Compare two recordings and display results."""
    print("\n" + "=" * 40)
    print("COMPARISON RESULTS")
    print("=" * 40)
    
    if rec2['duration'] == 0 or rec2['avg_amplitude'] == 0 or rec2['max_amplitude'] == 0:
        print("Cannot compare: Recording 2 contains no data.")
        return

    # Compare duration
    dur_diff = ((rec1['duration'] - rec2['duration']) / rec2['duration']) * 100
    if dur_diff > 0:
        print(f"Recording 1 is longer by {dur_diff:.1f}%")
    else:
        print(f"Recording 2 is longer by {abs(dur_diff):.1f}%")
    
    # Compare average amplitude (loudness)
    amp_diff = ((rec1['avg_amplitude'] - rec2['avg_amplitude']) / rec2['avg_amplitude']) * 100
    if amp_diff > 0:
        print(f"Recording 1 is louder by {amp_diff:.1f}%")
    else:
        print(f"Recording 2 is louder by {abs(amp_diff):.1f}%")
    
    # Compare max amplitude
    max_diff = ((rec1['max_amplitude'] - rec2['max_amplitude']) / rec2['max_amplitude']) * 100
    if max_diff > 0:
        print(f"Recording 1 has higher peak amplitude by {max_diff:.1f}%")
    else:
        print(f"Recording 2 has higher peak amplitude by {abs(max_diff):.1f}%")

def wait_for_enter():
    input("Press enter to stop: \n")
    stop_event.set()

def spinner():
    chars = '|/-\\'
    i = 0
    while not stop_event.is_set():
        sys.stdout.write(f"\rRecording...{chars[i % 4]}")
        sys.stdout.flush()
        i += 1
        time.sleep(0.1)
    print("\rRecording complete!!!!      ")

def transcribe(audio, rate, width):
    recognizer = sr.Recognizer()
    audio_data = AudioData(audio, rate, width)
    
    try:
        text = recognizer.recognize_google(audio_data)
        print(f"{text}")
        return text
    except sr.UnknownValueError:
        print("[Could not understand]")
        return "[Could not understand]"
    except sr.RequestError as e:
        print(f"[API error: {e}]")
        return "[API error]"

def save(audio, rate, width, filename):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(width)
        wf.setframerate(rate)
        wf.writeframes(audio)
    print(f"Saved: {filename}")

def record():
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=SAMPLE_RATE,
        input=True,
        frames_per_buffer=1024
    )

    frames = []
    stop_event.clear() # Clear event before thread spin-up
    
    threading.Thread(target=wait_for_enter, daemon=True).start()
    threading.Thread(target=spinner, daemon=True).start()

    while not stop_event.is_set():
        try:
            frames.append(stream.read(1024, exception_on_overflow=False))
        except IOError:
            pass
            
    stream.stop_stream()
    stream.close()
    width = p.get_sample_size(pyaudio.paInt16)
    p.terminate()
    return b''.join(frames), SAMPLE_RATE, width


# ==========================================
# DRIVER CODE
# ==========================================

print("=" * 40)
print("Hello this an AI master ASR!!!")
print("=" * 40)
print("Record Voice twice to compare the two recordings\n")

# Recording 1
print("=" * 40)
print("Recording 1: Speak normally: ")
print("=" * 40)

audio1, rate1, width1 = record()
save(audio1, rate1, width1, "audio1.wav")
analyse1 = analyze_audio(audio1, rate1)

print("\n" + "=" * 40)
print("Recording 1 results: ")
print("=" * 40)
print(f"Duration: {analyse1['duration']:.2f} seconds")
print(f"Avg Amplitude: {int(analyse1['avg_amplitude'])}")
print(f"Maximum Amplitude: {int(analyse1['max_amplitude'])}")
print("Transcription: ", end="") 
text1 = transcribe(audio1, rate1, width1)

print("\n" + "-" * 40 + "\n")

# Recording 2
print("=" * 40)
print("Recording 2: Speak louder so amplitude is higher: ")
print("=" * 40)

audio2, rate2, width2 = record()
save(audio2, rate2, width2, "audio2.wav")
analyse2 = analyze_audio(audio2, rate2)

print("\n" + "=" * 40)
print("Recording 2 results: ")
print("=" * 40)
print(f"Duration: {analyse2['duration']:.2f} seconds")
print(f"Avg Amplitude: {int(analyse2['avg_amplitude'])}")
print(f"Maximum Amplitude: {int(analyse2['max_amplitude'])}")
print("Transcription: ", end="") 
text2 = transcribe(audio2, rate2, width2)

# Comparison Execution
compare_recordings(analyse1, analyse2)

# Visual Waveforms
print("\n" + "=" * 40)
print("Displaying Waveforms... ")
print("=" * 40)

plot_waveform(audio1, rate1, "Recording for audio 1", color="green")
plot_waveform(audio2, rate2, "Recording for audio 2", color="blue")