# Lumi - AI Personal Assistant

Lumi is an open-source AI-powered personal assistant that interacts via voice commands. It features wake word detection, speech-to-text, text-to-speech, and a modular skill system for extensibility.

## Features

- **Wake Word Detection**: Uses OpenWakeWord for detecting wake words like "Lumi" or "Alexa".
- **Speech-to-Text**: Powered by Whisper (small model) for accurate transcription.
- **Text-to-Speech**: Uses ONNX models for natural speech synthesis.
- **Intent Routing**: Processes commands and routes to appropriate skills.
- **Skills**:
  - Time queries
  - Application launching
  - (Planned: Weather, System control, Screenshots)

## Installation

1. Clone the repository.
2. Create a virtual environment: `python -m venv .venv`
3. Activate: `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

Note: Additional dependencies like `openwakeword`, `onnxruntime` may need to be installed separately if not in requirements.txt.

## Usage

Run the assistant: `python app/assistant.py`

It will listen for the wake word, then process voice commands.

## Project Structure

- `app/`: Main application
  - `assistant.py`: Main loop for wake word detection and command processing
  - `config.py`: Configuration (currently empty)
  - `main.py`: Placeholder entry point
  - `audio/`: Audio processing modules
    - `mic.py`: Microphone handling
    - `stt.py`: Speech-to-text using Whisper
    - `tts.py`: Text-to-speech using ONNX
    - `wakeword.py`: Wake word detection
  - `core/`: Core logic
    - `intent_parser.py`: Intent parsing
    - `response.py`: Response generation
    - `router.py`: Command routing to skills
    - `state.py`: State management
- `skills/`: Skill implementations
  - `time_skill.py`: Time queries
  - `app_launcher.py`: Application launching
- `utils/`: Utilities
  - `helpers.py`: Helper functions
  - `logger.py`: Logging
- `data/`: Data storage
  - `logs/`: Log files
  - `memory/`: Memory data
- `models/`: Pre-trained models
  - `tts/`: Text-to-speech models
  - `wakeword/`: Wake word models
- `training_data/`: Training data for wake word
- `docker/`: Docker configuration
- `requirements.txt`: Python dependencies
- `test_*.py`: Test scripts

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests. Add new skills in the `skills/` directory and update the router accordingly.