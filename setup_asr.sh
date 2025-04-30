#!/bin/bash

# Setup script for Kinyarwanda ASR model

echo "Setting up Kinyarwanda ASR model..."

# Activate the virtual environment
source venv/bin/activate

# Install the necessary dependencies
pip install transformers torch soundfile librosa

# Create a script to download and cache the model
cat > download_model.py << EOL
from transformers import WhisperProcessor, WhisperForConditionalGeneration

print("Downloading and caching Kinyarwanda Whisper model...")
model_name = "mbazaNLP/Whisper-Small-Kinyarwanda"
processor = WhisperProcessor.from_pretrained(model_name)
model = WhisperForConditionalGeneration.from_pretrained(model_name)
print("Model downloaded and cached successfully!")
EOL

# Run the download script
python download_model.py

echo "Kinyarwanda ASR model setup complete!" 