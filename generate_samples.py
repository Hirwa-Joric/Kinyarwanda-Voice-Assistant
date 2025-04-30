"""
Script to generate sample audio files for the Kinyarwanda Voice Assistant.
This script uses gTTS to generate audio files for the questions in the QA pairs.
"""

import os
import json
from gtts import gTTS
from pathlib import Path

# Paths
ROOT_DIR = Path(".")
DATA_DIR = ROOT_DIR / "data"
AUDIO_INPUT_DIR = ROOT_DIR / "audio_samples" / "input"

# Create directories if they don't exist
AUDIO_INPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load QA pairs
qa_file = DATA_DIR / "qa_pairs.json"
with open(qa_file, 'r', encoding='utf-8') as f:
    qa_pairs = json.load(f)

# Create transcriptions file
transcriptions = {}

# Generate audio files for each question
for i, qa_pair in enumerate(qa_pairs):
    question = qa_pair["question"]
    
    # Generate audio file
    audio_file = AUDIO_INPUT_DIR / f"sample{i+1}.mp3"
    
    # Create audio using gTTS
    # Note: Using French as the closest language to Kinyarwanda for TTS
    tts = gTTS(text=question, lang='fr')
    tts.save(str(audio_file))
    
    # Save transcription
    transcriptions[f"sample{i+1}.mp3"] = question
    
    print(f"Generated audio file: {audio_file}")

# Save transcriptions to a file
transcriptions_file = DATA_DIR / "transcriptions.json"
with open(transcriptions_file, 'w', encoding='utf-8') as f:
    json.dump(transcriptions, f, ensure_ascii=False, indent=2)

print(f"Generated {len(qa_pairs)} sample audio files")
print(f"Transcriptions saved to {transcriptions_file}") 