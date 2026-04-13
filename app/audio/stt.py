from faster_whisper import WhisperModel

class STT:
    def __init__(self, model_size="small"):
        print("Loading Whisper model...")
        self.model = WhisperModel(model_size, compute_type="int8")

    def transcribe(self, audio_path):
        segments, _ = self.model.transcribe(audio_path)

        text = ""
        for segment in segments:
            text += segment.text

        return text.strip()