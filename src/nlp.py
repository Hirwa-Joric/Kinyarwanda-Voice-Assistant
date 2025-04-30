 """
Natural Language Processing (NLP) module for Kinyarwanda.
This module handles the matching of transcribed questions to predefined answers.
"""

import os
import json
import fasttext
import numpy as np
from pathlib import Path

class KinyarwandaNLP:
    def __init__(self, qa_file=None):
        """
        Initialize NLP module with QA pairs.
        
        Args:
            qa_file (str): Path to JSON file containing question-answer pairs
        """
        self.qa_pairs = self._load_qa_pairs(qa_file)
        self.default_answer = "Mbabarira, sinumva ikibazo. Ongera ubaze mu bundi buryo."  # "Sorry, I don't understand. Please ask differently."
        
        # If no embeddings model is available, use simple text matching
        self.use_embeddings = False
        
        # Try to load FastText model for better matching (if available)
        try:
            model_path = Path(__file__).parent.parent / "data" / "cc.rw.300.bin"
            if os.path.exists(model_path):
                self.model = fasttext.load_model(str(model_path))
                self.use_embeddings = True
                print("FastText model loaded for Kinyarwanda")
            else:
                print("FastText model not found. Using simple text matching.")
        except Exception as e:
            print(f"Could not load FastText model: {e}. Using simple text matching.")
    
    def _load_qa_pairs(self, qa_file):
        """
        Load question-answer pairs from a JSON file or use defaults.
        
        Args:
            qa_file (str): Path to JSON file
            
        Returns:
            list: List of dictionaries containing question-answer pairs
        """
        # Default QA pairs (will be used if no file is provided or file doesn't exist)
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
        
        if qa_file and os.path.exists(qa_file):
            try:
                with open(qa_file, 'r', encoding='utf-8') as f:
                    loaded_qa = json.load(f)
                print(f"Loaded {len(loaded_qa)} QA pairs from {qa_file}")
                return loaded_qa
            except Exception as e:
                print(f"Error loading QA file: {e}. Using default QA pairs.")
                return default_qa
        else:
            print("Using default QA pairs")
            return default_qa
    
    def save_qa_pairs(self, filepath):
        """Save the current QA pairs to a JSON file."""
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.qa_pairs, f, ensure_ascii=False, indent=2)
            print(f"Saved {len(self.qa_pairs)} QA pairs to {filepath}")
            return True
        except Exception as e:
            print(f"Error saving QA pairs: {e}")
            return False
    
    def add_qa_pair(self, question, answer):
        """Add a new question-answer pair."""
        self.qa_pairs.append({"question": question, "answer": answer})
    
    def _get_text_similarity(self, text1, text2):
        """Simple text similarity based on word overlap."""
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        intersection = words1.intersection(words2)
        
        if not words1 or not words2:
            return 0
        
        # Jaccard similarity
        return len(intersection) / (len(words1) + len(words2) - len(intersection))
    
    def _get_vector_similarity(self, text1, text2):
        """Get similarity between two texts using FastText embeddings."""
        vec1 = self.model.get_sentence_vector(text1)
        vec2 = self.model.get_sentence_vector(text2)
        
        # Normalize vectors
        vec1 = vec1 / np.linalg.norm(vec1)
        vec2 = vec2 / np.linalg.norm(vec2)
        
        # Cosine similarity
        return np.dot(vec1, vec2)
    
    def get_answer(self, question):
        """
        Match a question to the closest predefined question and return the answer.
        
        Args:
            question (str): The question to match
            
        Returns:
            str: The answer to the matched question
        """
        best_match = None
        best_score = 0.4  # Minimum similarity threshold
        
        for qa_pair in self.qa_pairs:
            if self.use_embeddings:
                similarity = self._get_vector_similarity(question, qa_pair["question"])
            else:
                similarity = self._get_text_similarity(question, qa_pair["question"])
            
            if similarity > best_score:
                best_score = similarity
                best_match = qa_pair
        
        if best_match:
            return best_match["answer"]
        else:
            return self.default_answer


# Test the module if run directly
if __name__ == "__main__":
    nlp = KinyarwandaNLP()
    
    # Test with sample questions
    test_questions = [
        "Muraho, amakuru?",
        "Witwa nde?",
        "Urakoze",
        "Ntacyo"
    ]
    
    for question in test_questions:
        answer = nlp.get_answer(question)
        print(f"Q: {question}")
        print(f"A: {answer}")
        print()