# Kinyarwanda Voice Assistant Documentation

## Overview

The Kinyarwanda Voice Assistant is a voice interface that:
1. Accepts speech input in Kinyarwanda
2. Transcribes the speech to text using KinyaWhisper
3. Matches the text to predefined questions using NLP and vector embeddings
4. Responds with an appropriate answer in Kinyarwanda
5. Converts the answer back to speech

## System Requirements

- Python 3.8 or higher
- Minimum 4GB RAM
- At least 10GB of free disk space (for full version with models)
- Internet connection (for initial setup)
- Microphone (for voice input)
- Speakers (for voice output)

## Setup Options

This project provides three setup options:

### 1. Minimal Demo (Recommended for Testing)

The minimal demo uses a simple text interface without the speech recognition component, requiring minimal dependencies.

```bash
# Run the minimal setup script
./setup_minimal.sh

# Run the demo
source venv/bin/activate
python run_demo.py
```

### 2. Standard Setup (Full Features)

The standard setup includes all components: ASR, NLP, and TTS.

```bash
# Run the setup script
./setup.sh

# Run the application
source venv/bin/activate
python src/app.py
```

### 3. Manual Setup

If you prefer to set up manually:

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Download FastText model (optional, for better NLP)
./setup_fasttext.sh

# Run the application
python src/app.py
```

## Architecture

The application is built with a modular architecture that separates concerns:

- **ASR Module** (`src/asr.py`): Handles speech recognition using the KinyaWhisper model
- **NLP Module** (`src/nlp.py`): Processes text and matches questions to answers using vector similarity
- **TTS Module** (`src/tts.py`): Converts text responses to speech
- **Web Interface** (`src/app.py`): Provides a user-friendly interface using Gradio

## Using the Voice Assistant

### Demo Version

1. Run the demo application: `python run_demo.py`
2. Open the Gradio interface in your browser (usually at http://127.0.0.1:7860)
3. In the "Text Assistant" tab:
   - Type a question in Kinyarwanda
   - Click "Process"
   - View the text answer and listen to the voice response
4. In the "Add QA Pairs" tab:
   - Add new question-answer pairs to the system

### Full Version

1. Run the full application: `python src/app.py`
2. Open the Gradio interface in your browser (usually at http://127.0.0.1:7860)
3. In the "Voice Assistant" tab:
   - Click the microphone icon and speak in Kinyarwanda
   - Click "Process"
   - View the transcription and answer, and listen to the voice response
4. In the "Add QA Pairs" tab:
   - Add new question-answer pairs to the system

## Extending the Assistant

### Adding New QA Pairs

You can add new question-answer pairs in two ways:

1. Through the web interface in the "Add QA Pairs" tab
2. By editing the `data/qa_pairs.json` file directly

### Improving NLP Matching

The default NLP matching uses basic text similarity. For better results:

1. Install FastText: `./setup_fasttext.sh`
2. The system will automatically use FastText embeddings for better matching

## Troubleshooting

### Speech Recognition Issues

- Ensure your microphone is properly connected and permitted in your browser
- Speak clearly and at a normal pace
- Try to minimize background noise

### Model Loading Issues

- Make sure you have enough disk space
- Check your internet connection during initial setup
- Ensure you have Python 3.8 or higher

### Application Won't Start

- Make sure your virtual environment is activated
- Check that all dependencies are installed
- Verify that you're in the correct directory

## Contributing

We welcome contributions! Please see our contributing guidelines:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is released under the MIT License.