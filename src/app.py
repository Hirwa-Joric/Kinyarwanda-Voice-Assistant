 """
Main application for Kinyarwanda Voice Assistant.
Integrates ASR, NLP, and TTS modules with a Gradio interface.
"""

import os
import time
import json
import gradio as gr
import numpy as np
from pathlib import Path

from asr import KinyarwandaASR
from nlp import KinyarwandaNLP
from tts import KinyarwandaTTS

# Paths
ROOT_DIR = Path(__file__).parent.parent
DATA_DIR = ROOT_DIR / "data"
AUDIO_INPUT_DIR = ROOT_DIR / "audio_samples" / "input"
AUDIO_OUTPUT_DIR = ROOT_DIR / "audio_samples" / "output"

# Create directories if they don't exist
DATA_DIR.mkdir(parents=True, exist_ok=True)
AUDIO_INPUT_DIR.mkdir(parents=True, exist_ok=True)
AUDIO_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Initialize components
asr = None
nlp = None
tts = None

def save_audio_input(audio_data, sample_rate):
    """Save input audio for later review/training."""
    timestamp = int(time.time())
    filename = AUDIO_INPUT_DIR / f"input_{timestamp}.wav"
    
    # Convert tuple to numpy array if needed
    if isinstance(audio_data, tuple):
        audio_data = audio_data[0]
    
    # Save the audio file
    with open(filename, "wb") as f:
        import soundfile as sf
        sf.write(f, audio_data, sample_rate, format="WAV")
    
    return str(filename)

def save_interaction(question, transcription, answer, audio_file):
    """Save interaction data for review."""
    interaction_file = DATA_DIR / "interactions.json"
    
    # Load existing interactions
    if interaction_file.exists():
        try:
            with open(interaction_file, "r", encoding="utf-8") as f:
                interactions = json.load(f)
        except:
            interactions = []
    else:
        interactions = []
    
    # Add new interaction
    interactions.append({
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "audio_file": str(audio_file),
        "transcription": transcription,
        "matched_question": question,
        "answer": answer
    })
    
    # Save interactions
    with open(interaction_file, "w", encoding="utf-8") as f:
        json.dump(interactions, f, ensure_ascii=False, indent=2)

def process_audio(audio_data, sample_rate):
    """
    Process audio input and return speech response.
    
    Args:
        audio_data: Audio data from Gradio
        sample_rate: Sample rate of audio
        
    Returns:
        tuple: (text_response, audio_response_path)
    """
    global asr, nlp, tts
    
    # Initialize components if not already done
    if asr is None:
        asr = KinyarwandaASR()
    
    if nlp is None:
        qa_file = DATA_DIR / "qa_pairs.json"
        nlp = KinyarwandaNLP(qa_file if qa_file.exists() else None)
    
    if tts is None:
        tts = KinyarwandaTTS(use_coqui=False, output_dir=AUDIO_OUTPUT_DIR)
    
    # Save the input audio
    audio_file = save_audio_input(audio_data, sample_rate)
    
    # Transcribe audio
    transcription = asr.transcribe_live(audio_data, sample_rate)
    
    # Get answer
    answer = nlp.get_answer(transcription)
    
    # Convert answer to speech
    speech_file = tts.text_to_speech(answer)
    
    # Save interaction
    save_interaction(transcription, transcription, answer, audio_file)
    
    return transcription, answer, speech_file

def add_qa_pair(question, answer):
    """Add a new QA pair to the system."""
    global nlp
    
    if nlp is None:
        qa_file = DATA_DIR / "qa_pairs.json"
        nlp = KinyarwandaNLP(qa_file if qa_file.exists() else None)
    
    nlp.add_qa_pair(question, answer)
    
    # Save updated QA pairs
    qa_file = DATA_DIR / "qa_pairs.json"
    nlp.save_qa_pairs(qa_file)
    
    return f"Added QA pair: '{question}' -> '{answer}'"

def create_ui():
    """Create Gradio UI for the application."""
    with gr.Blocks(title="Kinyarwanda Voice Assistant") as app:
        gr.Markdown("# Kinyarwanda Voice Assistant")
        gr.Markdown("Speak in Kinyarwanda and get a voice response.")
        
        with gr.Tab("Voice Assistant"):
            with gr.Row():
                with gr.Column():
                    # Input section
                    gr.Markdown("### Speak in Kinyarwanda")
                    audio_input = gr.Audio(
                        sources=["microphone"],
                        type="numpy",
                        label="Speak here"
                    )
                    btn_process = gr.Button("Process", variant="primary")
                
                with gr.Column():
                    # Output section
                    transcription_output = gr.Textbox(label="Transcription")
                    answer_output = gr.Textbox(label="Answer")
                    audio_output = gr.Audio(label="Voice Response")
            
            # Process button click event
            btn_process.click(
                fn=process_audio,
                inputs=[audio_input],
                outputs=[transcription_output, answer_output, audio_output]
            )
        
        with gr.Tab("Add QA Pairs"):
            with gr.Row():
                with gr.Column():
                    question_input = gr.Textbox(label="Question in Kinyarwanda")
                    answer_input = gr.Textbox(label="Answer in Kinyarwanda")
                    btn_add = gr.Button("Add QA Pair")
                    result_output = gr.Textbox(label="Result")
            
            # Add QA pair button click event
            btn_add.click(
                fn=add_qa_pair,
                inputs=[question_input, answer_input],
                outputs=[result_output]
            )
        
        gr.Markdown("### About")
        gr.Markdown("""
        This is a mini Kinyarwanda Voice Assistant that:
        1. Transcribes Kinyarwanda speech to text using KinyaWhisper
        2. Matches questions to predefined answers using NLP
        3. Converts answers back to speech using TTS
        """)
    
    return app

def main():
    """Main function to run the application."""
    # Create default QA pairs file if it doesn't exist
    qa_file = DATA_DIR / "qa_pairs.json"
    if not qa_file.exists():
        default_qa = [
            {
                "question": "Muraho, Amakuru?", 
                "answer": "Meza, murakoze! Nagufasha iki?"
            },
            {
                "question": "Witwa nde?", 
                "answer": "Nitwa Kinyarwanda Assistant. Ndi porogaramu ikugufasha mu Kinyarwanda."
            },
            {
                "question": "Saa ngahe?",
                "answer": "Mbabarira, sinshobora kumenya isaha ubu."
            },
            {
                "question": "Hari amakuru ki uyu munsi?", 
                "answer": "Mbabarira, sinshobora gukurikirana amakuru ubu ngubu."
            },
            {
                "question": "Urakoze cyane", 
                "answer": "Nta kibazo! Ndagufasha igihe cyose."
            }
        ]
        with open(qa_file, 'w', encoding='utf-8') as f:
            json.dump(default_qa, f, ensure_ascii=False, indent=2)
        print(f"Created default QA pairs file at {qa_file}")
    
    # Create and launch Gradio UI
    app = create_ui()
    app.launch(share=False)

if __name__ == "__main__":
    main()