# Kinyarwanda Voice Assistant

A mini voice assistant that processes Kinyarwanda speech, understands questions using NLP, and responds with voice output.

## Features

- Speech Recognition (ASR) using KinyaWhisper
- Natural Language Processing (NLP) for question-answer matching
- Text-to-Speech (TTS) for spoken responses
- Simple interface for voice interaction

## Project Structure

```
├── src/                  # Source code
│   ├── asr.py            # Speech recognition module
│   ├── nlp.py            # NLP matching module  
│   ├── tts.py            # Text-to-speech module
│   └── app.py            # Main application
├── data/                 # Data files
│   └── qa_pairs.json     # Question-answer pairs
├── audio_samples/        # Audio files
│   ├── input/            # Input speech samples
│   └── output/           # Generated speech responses
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd Kinyarwanda_AI
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/app.py
   ```

## Usage

1. The assistant will listen for Kinyarwanda speech input.
2. It will transcribe the speech to text using KinyaWhisper.
3. The text will be matched to predefined questions.
4. The answer will be generated as speech output.

## Technologies Used

- KinyaWhisper for Automatic Speech Recognition (ASR)
- Basic NLP for question-answer matching
- Coqui TTS or gTTS for Text-to-Speech synthesis
- Gradio for the user interface

## License

[MIT License]