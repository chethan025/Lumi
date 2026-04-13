import time
import queue
import numpy as np
import sounddevice as sd
import soundfile as sf
from rich.console import Console
from openwakeword.model import Model
from stt import transcribe_audio

console = Console()

SAMPLE_RATE = 16000
BLOCKSIZE = 1280
DETECTION_THRESHOLD = 0.5

VERIFY_DURATION = 2  # seconds
VERIFY_FILE = "verify.wav"

audio_queue = queue.Queue()

def audio_callback(indata, frames, time_info, status):
    if status:
        console.print(f"[red]Audio status:[/red] {status}")
    audio_queue.put(indata.copy())

def record_verification_audio():
    console.print("[dim]Verifying wake phrase...[/dim]")
    audio = sd.rec(int(VERIFY_DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
    sd.wait()
    sf.write(VERIFY_FILE, audio, SAMPLE_RATE)

def is_valid_wake_phrase(text):
    variants = ["hey lumi", "hey loomy", "hey lumy"]
    return any(v in text for v in variants)

def main():
    console.print("[bold cyan]Lumi Wake Engine (Verified)[/bold cyan]")
    console.print("[yellow]Loading wake word model...[/yellow]")

    model = Model()

    console.print("[green]Listennnning...[/green]\n")

    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype='int16',
        blocksize=BLOCKSIZE,
        callback=audio_callback
    ):
        while True:
            audio = audio_queue.get()
            audio = np.squeeze(audio)

            predictions = model.predict(audio)

            for wakeword, score in predictions.items():
                if score > DETECTION_THRESHOLD:
                    console.print(f"[cyan]Wake candidate:[/cyan] {wakeword} ({score:.2f})")

                    # Step 1: record verification audio
                    record_verification_audio()

                    # Step 2: transcribe
                    text = transcribe_audio(VERIFY_FILE)
                    console.print(f"[yellow]Heard:[/yellow] {text}")

                    # Step 3: verify
                    if is_valid_wake_phrase(text):
                        console.print("[bold green]Lumi activated.[/bold green]\n")
                    else:
                        console.print("[red]False trigger ignored.[/red]\n")

                    time.sleep(1)

if __name__ == "__main__":
    main()