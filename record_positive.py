import sounddevice as sd
import soundfile as sf
import os

SAMPLE_RATE = 16000
DURATION = 2
OUTPUT_DIR = "/mnt/MATRIX/Files/Projects/Personal Projects/AI/Agents/Lumi/training_dataset/wakeword/lumi/positive"

os.makedirs(OUTPUT_DIR, exist_ok=True)

count = len(os.listdir(OUTPUT_DIR))

print("Say: 'Hey Lumi' naturally. Different tones, speeds, distances.\n")

while True:
    input("Press Enter to record (or Ctrl+C to stop)...")

    print("Recording...")
    audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
    sd.wait()

    filename = f"{OUTPUT_DIR}/sample_{count}.wav"
    sf.write(filename, audio, SAMPLE_RATE)

    print(f"Saved: {filename}")
    count += 1