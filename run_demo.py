 """
Simplified demo of Kinyarwanda Voice Assistant.
This version uses minimal components for quick testing.
"""

import os
import time
import json
import gradio as gr
from pathlib import Path
from gtts import gTTS

# Paths
ROOT_DIR = Path(".")
DATA_DIR = ROOT_DIR / "data"
AUDIO_OUTPUT_DIR = ROOT_DIR / "audio_samples" / "output"

# Create directories if they don't exist
DATA_DIR.mkdir(parents=True, exist_ok=True)
AUDIO_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load QA pairs
qa_file = DATA_DIR / "qa_pairs.json"
if qa_file.exists():
    with open(qa_file, 'r', encoding='utf-8') as f:
        qa_pairs = json.load(f)
else:
    # Default QA pairs
    qa_pairs = [
        {
            "question": "Muraho, Amakuru?",
            "answer": "Meza, murakoze! Nagufasha iki?"
        },
        {
            "question": "Witwa nde?",
            "answer": "Nitwa Kinyarwanda Assistant. Ndi porogaramu ikugufasha mu Kinyarwanda."
        },
        {
            "question": "Urakoze cyane",
            "answer": "Nta kibazo! Ndagufasha igihe cyose."
        }
    ]

def text_to_speech(text):
    """Simple TTS using gTTS."""
    output_file = AUDIO_OUTPUT_DIR / f"response_{int(time.time())}.mp3"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Use French as the closest available language to Kinyarwanda
    tts = gTTS(text=text, lang='fr')
    tts.save(str(output_file))
    
    return str(output_file)

def get_text_similarity(text1, text2):
    """Simple text similarity based on word overlap."""
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    intersection = words1.intersection(words2)
    
    if not words1 or not words2:
        return 0
    
    # Jaccard similarity
    return len(intersection) / (len(words1) + len(words2) - len(intersection))

def get_answer(question):
    """Match a question to the closest predefined question and return the answer."""
    best_match = None
    best_score = 0.4  # Minimum similarity threshold
    
    for qa_pair in qa_pairs:
        similarity = get_text_similarity(question, qa_pair["question"])
        
        if similarity > best_score:
            best_score = similarity
            best_match = qa_pair
    
    if best_match:
        return best_match["answer"]
    else:
        return "Mbabarira, sinumva ikibazo. Ongera ubaze mu bundi buryo."

def process_text(text_input):
    """Process text input and return text and speech responses."""
    # Get answer
    answer = get_answer(text_input)
    
    # Convert answer to speech
    speech_file = text_to_speech(answer)
    
    return answer, speech_file

def add_qa_pair(question, answer):
    """Add a new QA pair to the system."""
    global qa_pairs
    
    qa_pairs.append({"question": question, "answer": answer})
    
    # Save updated QA pairs
    with open(qa_file, 'w', encoding='utf-8') as f:
        json.dump(qa_pairs, f, ensure_ascii=False, indent=2)
    
    return f"Added QA pair: '{question}' -> '{answer}'"

def create_ui():
    """Create Gradio UI for the application."""
    with gr.Blocks(title="Kinyarwanda Voice Assistant Demo") as app:
        gr.Markdown("# Kinyarwanda Voice Assistant Demo")
        gr.Markdown("Type in Kinyarwanda and get a voice response.")
        
        with gr.Tab("Text Assistant"):
            with gr.Row():
                with gr.Column():
                    # Input section
                    text_input = gr.Textbox(
                        label="Enter text in Kinyarwanda",
                        placeholder="Example: Muraho, Amakuru?"
                    )
                    btn_process = gr.Button("Process", variant="primary")
                
                with gr.Column():
                    # Output section
                    answer_output = gr.Textbox(label="Answer")
                    audio_output = gr.Audio(label="Voice Response")
            
            # Process button click event
            btn_process.click(
                fn=process_text,
                inputs=[text_input],
                outputs=[answer_output, audio_output]
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
        
        gr.Markdown("### Available Questions")
        questions_md = "\n".join([f"- {qa['question']}" for qa in qa_pairs])
        gr.Markdown(questions_md)
        
        gr.Markdown("### About")
        gr.Markdown("""
        This is a simplified demo of the Kinyarwanda Voice Assistant that:
        1. Matches questions to predefined answers using simple text similarity
        2. Converts answers back to speech using gTTS
        
        For the full version with speech recognition, run `python src/app.py` after setup.
        """)
    
    return app

def main():
    # Create and launch Gradio UI
    app = create_ui()
    app.launch(share=False)

if __name__ == "__main__":
    main()