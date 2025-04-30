# Kinyarwanda Voice Assistant

A voice assistant that processes Kinyarwanda speech, understands questions using NLP, and responds with voice output.

## Features

- Speech Recognition (ASR) using KinyaWhisper (mbazaNLP/Whisper-Small-Kinyarwanda)
- Natural Language Processing (NLP) for question-answer matching with FastText support
- Text-to-Speech (TTS) for spoken responses
- Interactive web interface for voice interaction
- Predefined Kinyarwanda question-answer pairs
- Expandable knowledge base

## Project Structure

```
├── src/                  # Source code
│   ├── asr.py            # Speech recognition module (KinyaWhisper)
│   ├── nlp.py            # NLP matching module  
│   ├── tts.py            # Text-to-speech module
│   └── app.py            # Main application with Gradio interface
├── data/                 # Data files
│   ├── qa_pairs.json     # Question-answer pairs in Kinyarwanda
│   └── transcriptions.json # Audio file transcriptions
├── audio_samples/        # Audio files
│   ├── input/            # Input speech samples
│   └── output/           # Generated speech responses
├── setup.sh              # Full setup script
├── setup_minimal.sh      # Minimal setup script
├── setup_asr.sh          # ASR model setup script
├── setup_fasttext.sh     # FastText model setup script
├── generate_samples.py   # Script to generate sample audio files
├── audio_sample_generator.py # Script to generate answer audio files
├── run_demo.py           # Simplified demo application
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

## Project Components

### 1. Python Source Files
The project contains multiple Python modules:
- `src/asr.py` - Speech recognition module using KinyaWhisper
- `src/nlp.py` - NLP module for text processing and matching
- `src/tts.py` - Text-to-speech module for generating spoken responses
- `src/app.py` - Main application with web interface
- `run_demo.py` - Simplified demo application
- `generate_samples.py` - Tool to generate question audio samples
- `audio_sample_generator.py` - Tool to generate answer audio samples

### 2. Audio Files
The project includes:
- **Input Audio Files**: 10 sample question recordings in Kinyarwanda (in `audio_samples/input/`)
- **Output Audio Files**: 10 sample answer recordings (in `audio_samples/output/`)
- **Transcriptions**: JSON mapping of audio files to text transcriptions (`data/transcriptions.json`)

### 3. NLP Mapping
- **Question-Answer Pairs**: 10 predefined QA pairs in Kinyarwanda (`data/qa_pairs.json`)
- **Matching Algorithm**: Text similarity with FastText vector support (`src/nlp.py`)

## Setup Instructions

### Option 1: Quick Demo Setup (Recommended for Testing)

```bash
# Run the minimal setup script
./setup_minimal.sh

# Generate sample audio files
source venv/bin/activate
python generate_samples.py
python audio_sample_generator.py

# Run the demo
python run_demo.py
```

### Option 2: Full Setup (with ASR)

```bash
# Run the full setup script
./setup.sh

# Set up the ASR model
./setup_asr.sh

# Generate sample audio files
source venv/bin/activate
python generate_samples.py
python audio_sample_generator.py

# Run the application
python src/app.py
```

## Usage

### Demo Version

1. The demo provides a text interface where you can input Kinyarwanda text
2. It will match your input to the closest predefined question
3. It will display the answer and speak it using text-to-speech

### Full Version

1. The full version provides a voice interface
2. Speak in Kinyarwanda into your microphone
3. The application will transcribe your speech using KinyaWhisper
4. It will match the transcribed text to the closest predefined question
5. It will display and speak the answer

## Question-Answer Pairs

The system includes the following Kinyarwanda QA pairs:

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
- **NLP**: Text similarity with FastText vector embedding support
- **TTS**: gTTS (Google Text-to-Speech) for voice output
- **UI**: Gradio for the interactive web interface

## Roadmap

- Add support for more complex conversational patterns
- Improve speech recognition accuracy
- Expand the knowledge base
- Add support for more African languages

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License