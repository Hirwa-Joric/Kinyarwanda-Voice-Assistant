 """
Text-to-Speech (TTS) module for Kinyarwanda.
This module handles the conversion of text to speech.
"""

import os
from pathlib import Path
import torch
from gtts import gTTS
from TTS.api import TTS as CoquiTTS

class KinyarwandaTTS:
    def __init__(self, use_coqui=False, output_dir=None):
        """
        Initialize TTS module.
        
        Args:
            use_coqui (bool): Whether to use Coqui TTS (if False, use gTTS)
            output_dir (str): Directory to save audio files
        """
        self.use_coqui = use_coqui
        
        if output_dir:
            self.output_dir = Path(output_dir)
        else:
            self.output_dir = Path(__file__).parent.parent / "audio_samples" / "output"
        
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        if use_coqui:
            try:
                # Initialize Coqui TTS - try to use a suitable model
                device = "cuda" if torch.cuda.is_available() else "cpu"
                
                # Since there might not be a specific Kinyarwanda model,
                # we'll use a multilingual model and specify the language
                self.tts = CoquiTTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")
                self.tts.to(device)
                print(f"Coqui TTS loaded on {device}")
            except Exception as e:
                print(f"Error loading Coqui TTS: {e}. Falling back to gTTS.")
                self.use_coqui = False
    
    def text_to_speech(self, text, output_file=None):
        """
        Convert text to speech.
        
        Args:
            text (str): Text to convert to speech
            output_file (str): Path to save the audio file (optional)
            
        Returns:
            str: Path to the generated audio file
        """
        if not output_file:
            output_file = self.output_dir / f"response_{len(os.listdir(self.output_dir))}.mp3"
        
        output_file = Path(output_file)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        if self.use_coqui:
            try:
                # For XTTS v2, we need to specify a speaker reference
                self.tts.tts_to_file(
                    text=text,
                    file_path=str(output_file),
                    language="fr",  # Using French as it's similar to Kinyarwanda in pronunciation
                    speaker_wav=None  # This would be better with a Kinyarwanda reference file
                )
            except Exception as e:
                print(f"Error with Coqui TTS: {e}. Falling back to gTTS.")
                tts = gTTS(text=text, lang='fr')  # Using French as a fallback
                tts.save(str(output_file))
        else:
            # Use gTTS with French as the closest available language to Kinyarwanda
            tts = gTTS(text=text, lang='fr')
            tts.save(str(output_file))
        
        print(f"Generated speech at: {output_file}")
        return str(output_file)


# Test the module if run directly
if __name__ == "__main__":
    tts = KinyarwandaTTS(use_coqui=False)
    
    # Test with sample text
    test_text = "Muraho, nitwa Kinyarwanda Assistant. Ndi porogaramu ikugufasha mu Kinyarwanda."
    output_path = tts.text_to_speech(test_text)
    print(f"Generated speech file: {output_path}")