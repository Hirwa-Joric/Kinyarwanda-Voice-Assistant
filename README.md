# Kinyarwanda Voice Assistant

A voice interface application that processes Kinyarwanda speech, understands questions using NLP, and responds with natural voice output.

## Features

- Speech Recognition (ASR) using KinyaWhisper (mbazaNLP/Whisper-Small-Kinyarwanda)
- Natural Language Processing (NLP) with FastText vector embedding support
- Text-to-Speech (TTS) synthesis for natural-sounding responses
- Interactive web interface with real-time voice processing
- Knowledge base of common Kinyarwanda phrases and information
- Expandable conversation capabilities

## Project Structure

```
├── src/                  # Source code
│   ├── asr.py            # Speech recognition module (KinyaWhisper)
│   ├── nlp.py            # NLP matching module with FastText support
│   ├── tts.py            # Text-to-speech synthesis module
│   └── app.py            # Main application with Gradio interface
├── data/                 # Data files
│   ├── qa_pairs.json     # Knowledge base in Kinyarwanda
│   └── transcriptions.json # Processing records
├── audio_samples/        # Processed audio
│   ├── input/            # Processed speech inputs
│   └── output/           # Generated voice responses
├── setup.sh              # Full setup script
├── setup_minimal.sh      # Minimal setup script
├── setup_asr.sh          # ASR model setup script
├── setup_fasttext.sh     # FastText model setup script
├── run_demo.py           # Demo application
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

## Key Components

### 1. Core Processing Modules
The application is built on four specialized components:
- **Speech Recognition**: Converts Kinyarwanda speech to text using advanced acoustic models
- **Language Understanding**: Processes text inputs and identifies user intent
- **Knowledge Matching**: Maps user questions to appropriate answers
- **Speech Synthesis**: Converts text responses to natural-sounding speech

### 2. Voice Processing
The system demonstrates real-time voice capabilities:
- **Speech Recognition**: Accurately processes 10+ different Kinyarwanda voice inputs
- **Speech Output**: Generates natural-sounding voice responses in Kinyarwanda
- **Conversation Flow**: Maintains context through request-response pairs

### 3. Knowledge System
- **Contextual Understanding**: Matches queries to the most relevant knowledge entries
- **Dynamic Responses**: Provides appropriate answers to a variety of questions
- **Extensible**: Knowledge base can be expanded through the interface

## Setup Instructions

### Option 1: Quick Demo Setup (Recommended for Testing)

```bash
# Run the minimal setup script
./setup_minimal.sh

# Run the demo
source venv/bin/activate
python run_demo.py
```

### Option 2: Full Setup (with Voice Recognition)

```bash
# Run the full setup script
./setup.sh

# Set up the ASR model
./setup_asr.sh

# Run the application
source venv/bin/activate
python src/app.py
```

## Usage

### Demo Version

1. The demo provides a text interface where you can input Kinyarwanda text
2. The system processes your input and identifies the intent
3. It retrieves the appropriate response from its knowledge base
4. The answer is displayed and spoken using text-to-speech

### Full Version

1. The full version provides a complete voice interface
2. Speak in Kinyarwanda into your microphone
3. The application processes your speech in real-time
4. It matches your request to the appropriate response
5. The system responds both visually and with voice

## Conversation Examples

The system can handle the following Kinyarwanda interactions:

1. "Muraho, Amakuru?" → "Meza, murakoze! Nagufasha iki?"
2. "Witwa nde?" → "Nitwa Kinyarwanda Assistant. Ndi porogaramu ikugufasha mu Kinyarwanda."
3. "Saa ngahe?" → "Mbabarira, sinshobora kumenya isaha ubu."
4. "Hari amakuru ki uyu munsi?" → "Mbabarira, sinshobora gukurikirana amakuru ubu ngubu."
5. "Urakoze cyane" → "Nta kibazo! Ndagufasha igihe cyose."
6. "Ni iki Kigali?" → "Kigali ni umurwa mukuru wa Repubulika y'u Rwanda."
7. "Ikinyarwanda ni iki?" → "Ikinyarwanda ni ururimi ruvugwa mu Rwanda, ni urwimburiro n'umuco w'abanyarwanda."
8. "Telefoni yawe ni iyihe?" → "Mbabarira, nta nimero ya telefoni mfite."
9. "Ni nde Perezida wa Rwanda?" → "Paul Kagame ni Perezida wa Repubulika y'u Rwanda."
10. "Uri he?" → "Ndi muri porogaramu, ntabwo mfite ahantu. Ndi gusa kugufasha."

## Technologies Used

- **ASR**: KinyaWhisper (mbazaNLP/Whisper-Small-Kinyarwanda) for Kinyarwanda speech recognition
- **NLP**: FastText vector embeddings for semantic understanding
- **TTS**: Advanced speech synthesis optimized for Kinyarwanda
- **UI**: Gradio for the interactive real-time interface

## Roadmap

- Enhanced conversation capabilities with context awareness
- Expanded knowledge base coverage
- Improved speech recognition accuracy for diverse accents
- Support for additional Rwandan languages

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License