 # Kinyarwanda Voice Assistant Manual

## Overview

The Kinyarwanda Voice Assistant is a mini voice assistant that:
1. Accepts speech input in Kinyarwanda
2. Transcribes the speech to text using KinyaWhisper
3. Matches the text to predefined questions using NLP
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

## Project Structure

- `src/` - Source code
  - `asr.py` - Speech recognition module
  - `nlp.py` - NLP matching module
  - `tts.py` - Text-to-speech module
  - `app.py` - Main application
- `data/` - Data files
  - `qa_pairs.json` - Question-answer pairs
- `audio_samples/` - Audio files
  - `input/` - Input speech samples
  - `output/` - Generated speech responses
- `requirements.txt` - Dependencies
- `setup.sh` - Setup script
- `setup_minimal.sh` - Minimal setup script
- `setup_fasttext.sh` - Script to download FastText model
- `run_demo.py` - Simplified demo application

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

## Sample QA Pairs

The system comes with several predefined question-answer pairs, including:

- "Muraho, Amakuru?" → "Meza, murakoze! Nagufasha iki?"
- "Witwa nde?" → "Nitwa Kinyarwanda Assistant. Ndi porogaramu ikugufasha mu Kinyarwanda."
- "Saa ngahe?" → "Mbabarira, sinshobora kumenya isaha ubu."
- "Hari amakuru ki uyu munsi?" → "Mbabarira, sinshobora gukurikirana amakuru ubu ngubu."
- "Urakoze cyane" → "Nta kibazo! Ndagufasha igihe cyose."

You can add more QA pairs through the interface.

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

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is released under the MIT License.