import sounddevice as sd
import soundfile as sf
from app.audio.stt import STT

SAMPLE_RATE = 16000
DURATION = 5
FILENAME = "command.wav"

def record():
    print("Speak your command...")
    audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
    sd.wait()
    sf.write(FILENAME, audio, SAMPLE_RATE)
    print("Recording saved.")

def main():
    record()

    stt = STT("small")
    text = stt.transcribe(FILENAME)

    print(f"\nYou said: {text}")

if __name__ == "__main__":
    main()