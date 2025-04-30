 #!/bin/bash

# Minimal setup script for Kinyarwanda Voice Assistant Demo

echo "Setting up Kinyarwanda Voice Assistant Demo (Minimal Version)..."

# Create virtual environment
echo "Creating virtual environment..."
python -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install minimal dependencies
echo "Installing minimal dependencies..."
pip install --upgrade pip
pip install gradio gtts

# Create necessary directories
echo "Creating directories..."
mkdir -p data audio_samples/input audio_samples/output

echo "Setup complete!"
echo "To start the demo application, run: source venv/bin/activate && python run_demo.py"