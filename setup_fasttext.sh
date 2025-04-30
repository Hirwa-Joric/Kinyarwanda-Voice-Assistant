 #!/bin/bash

# Setup script for downloading FastText model for Kinyarwanda

echo "Downloading FastText model for Kinyarwanda..."

# Create data directory if it doesn't exist
mkdir -p data

# Download FastText model for Kinyarwanda
if [ ! -f "data/cc.rw.300.bin" ]; then
    echo "Downloading FastText model (approx. 2.7GB compressed, 8.4GB uncompressed)..."
    wget -P data https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.rw.300.bin.gz
    echo "Extracting FastText model..."
    gunzip data/cc.rw.300.bin.gz
    echo "FastText model downloaded and extracted successfully."
else
    echo "FastText model already exists."
fi

echo "Setup complete!"