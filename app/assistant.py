import time
import queue
import numpy as np
import sounddevice as sd
import soundfile as sf
from rich.console import Console

from openwakeword.model import Model
from audio.stt import STT
from audio.tts import speak

from core.router import route_command


console = Console()

SAMPLE_RATE = 16000
BLOCKSIZE = 1280
RECORD_SECONDS = 4
DETECTION_THRESHOLD = 0.5

audio_queue = queue.Queue()

def audio_callback(indata, frames, time_info, status):
    if status:
        console.print(f"[red]Audio status:[/red] {status}")
    audio_queue.put(indata.copy())

def record_command():
    console.print("[yellow]Listening for command...[/yellow]")

    audio = sd.rec(
        int(RECORD_SECONDS * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype='int16'
    )
    sd.wait()

    filename = "command.wav"
    sf.write(filename, audio, SAMPLE_RATE)

    return filename

def main():
    console.print("[bold cyan]Lumi Assistant v0.1[/bold cyan]")

    # Wake word model
    model = Model()  # later replace with your custom lumi model

    # STT
    stt = STT("small")

    console.print("[green]Listening for wake word...[/green]\n")

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
                    console.print(f"\n[bold green]Wake word detected:[/bold green] {wakeword}")

                    # Record command
                    file = record_command()

                    # Transcribe
                    text = stt.transcribe(file)


                    console.print(f"[cyan]You said:[/cyan] {text}")

                    response = route_command(text)

                    console.print(f"[green]Lumi:[/green] {response}\n")
                    speak(response)

                    time.sleep(1)

if __name__ == "__main__":
    main()