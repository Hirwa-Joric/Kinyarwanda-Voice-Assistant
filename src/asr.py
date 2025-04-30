 """
Automatic Speech Recognition (ASR) module using KinyaWhisper.
This module handles the conversion of Kinyarwanda speech to text using the mbazaNLP/Whisper-Small-Kinyarwanda model.
"""

import os
import torch
import soundfile as sf
import librosa
from transformers import WhisperProcessor, WhisperForConditionalGeneration, pipeline

class KinyarwandaASR:
    def __init__(self, model_name="mbazaNLP/Whisper-Small-Kinyarwanda"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
        
        print(f"Loading KinyaWhisper model on {self.device}...")
        
        # Load model and processor
        self.model = WhisperForConditionalGeneration.from_pretrained(
            model_name,
            torch_dtype=torch_dtype,
            low_cpu_mem_usage=True,
            use_safetensors=True
        )
        self.model.to(self.device)
        
        self.processor = WhisperProcessor.from_pretrained(model_name)
        
        # Force Kinyarwanda as the language
        self.forced_decoder_ids = self.processor.get_decoder_prompt_ids(
            language="sw",  # Use Swahili as proxy for Kinyarwanda in Whisper
            task="transcribe"
        )
        
        # Create pipeline
        self.pipe = pipeline(
            "automatic-speech-recognition",
            model=self.model,
            tokenizer=self.processor.tokenizer,
            feature_extractor=self.processor.feature_extractor,
            max_new_tokens=128,
            chunk_length_s=30,
            batch_size=16,
            return_timestamps=False,
            torch_dtype=torch_dtype,
            device=self.device,
        )
        
        print("KinyaWhisper model loaded successfully.")
    
    def transcribe_audio(self, audio_path):
        """
        Transcribe Kinyarwanda audio to text.
        
        Args:
            audio_path (str): Path to the audio file
            
        Returns:
            str: Transcribed text
        """
        print(f"Transcribing audio: {audio_path}")
        
        # Generate transcription with forced decoder IDs
        result = self.pipe(
            audio_path, 
            generate_kwargs={"forced_decoder_ids": self.forced_decoder_ids}
        )
        transcription = result["text"]
        
        print(f"Transcription: {transcription}")
        return transcription
    
    def transcribe_live(self, audio_array, sample_rate=16000):
        """
        Transcribe live audio input.
        
        Args:
            audio_array: NumPy array of audio data
            sample_rate: Sample rate of audio data
            
        Returns:
            str: Transcribed text
        """
        # Generate transcription with forced decoder IDs
        result = self.pipe(
            {"array": audio_array, "sampling_rate": sample_rate},
            generate_kwargs={"forced_decoder_ids": self.forced_decoder_ids}
        )
        return result["text"]


# Test the module if run directly
if __name__ == "__main__":
    asr = KinyarwandaASR()
    
    # Test with a sample audio file if available
    sample_audio = "../audio_samples/input/sample1.mp3"
    if os.path.exists(sample_audio):
        transcription = asr.transcribe_audio(sample_audio)
        print(f"Sample transcription: {transcription}")
    else:
        print(f"Sample audio file not found: {sample_audio}")