import subprocess

MODEL_PATH = "models/tts/en_US-hfc_female-medium.onnx"

def speak(text: str):
    try:
        command = [
            "piper",
            "--model", MODEL_PATH,
            "--output-raw"
        ]

        process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE
        )

        # Send text to Piper
        audio, _ = process.communicate(input=text.encode())

        # Play audio using aplay
        player = subprocess.Popen(
            ["aplay", "-r", "22050", "-f", "S16_LE", "-t", "raw", "-"],
            stdin=subprocess.PIPE
        )

        player.communicate(audio)

    except Exception as e:
        print(f"TTS Error: {e}")