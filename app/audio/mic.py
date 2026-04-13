import sounddevice as sd
import soundfile as sf

DURATION = 5
SAMPLERATE = 16000
FILENAME = "test_recording.wav"

def record_audio():
    print("Recording for 5 seconds...")
    audio = sd.rec(int(DURATION * SAMPLERATE), samplerate=SAMPLERATE, channels=1, dtype='int16')
    sd.wait()
    sf.write(FILENAME, audio, SAMPLERATE)
    print(f"Saved recording as {FILENAME}")

if __name__ == "__main__":
    record_audio()