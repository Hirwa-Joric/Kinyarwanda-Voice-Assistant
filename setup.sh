 #!/bin/bash

# Setup script for Kinyarwanda Voice Assistant

echo "Setting up Kinyarwanda Voice Assistant..."

# Create virtual environment
echo "Creating virtual environment..."
python -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create necessary directories
echo "Creating directories..."
mkdir -p data audio_samples/input audio_samples/output

# Download FastText model for Kinyarwanda if not already downloaded
if [ ! -f "data/cc.rw.300.bin" ]; then
    echo "Downloading FastText model for Kinyarwanda..."
    wget -P data https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.rw.300.bin.gz
    gunzip data/cc.rw.300.bin.gz
else
    echo "FastText model already exists."
fi

echo "Setup complete!"
echo "To start the application, run: source venv/bin/activate && python src/app.py"