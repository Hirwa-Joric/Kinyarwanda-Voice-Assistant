#!/usr/bin/env python3
"""
Script to generate sample answer audio files for the Kinyarwanda Voice Assistant.
This script reads the QA pairs and generates audio files for the answers.
"""

import os
import json
from pathlib import Path
from gtts import gTTS

# Paths
ROOT_DIR = Path(".")
DATA_DIR = ROOT_DIR / "data"
AUDIO_OUTPUT_DIR = ROOT_DIR / "audio_samples" / "output"

# Create directories if they don't exist
AUDIO_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load QA pairs
qa_file = DATA_DIR / "qa_pairs.json"
with open(qa_file, 'r', encoding='utf-8') as f:
    qa_pairs = json.load(f)

# Generate audio files for each answer
print("Generating answer audio samples...")
for i, qa_pair in enumerate(qa_pairs):
    answer = qa_pair["answer"]
    
    # Generate audio file
    audio_file = AUDIO_OUTPUT_DIR / f"answer{i+1}.mp3"
    
    # Create audio using gTTS
    # Note: Using French as the closest language to Kinyarwanda for TTS
    tts = gTTS(text=answer, lang='fr')
    tts.save(str(audio_file))
    
    print(f"Generated answer audio file: {audio_file}")

print(f"\nGenerated {len(qa_pairs)} answer audio files in {AUDIO_OUTPUT_DIR}")
print("These files represent the spoken outputs of the assistant.")