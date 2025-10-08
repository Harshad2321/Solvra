"""
Solvra - Data Preprocessing Module
Handles data loading, cleaning, and formatting for the reasoning pipeline
"""

import pandas as pd
import numpy as np
import re
from typing import Dict, List, Tuple, Optional
from pathlib import Path


class DataPreprocessor:
    """
    Preprocesses raw CSV data for the Solvra reasoning system.
    Cleans text, extracts patterns, and categorizes problem types.
    """
    
    def __init__(self, data_dir: str = "../data"):
        self.data_dir = Path(data_dir)
        self.train_df = None
        self.test_df = None
        self.problem_categories = {}
        
    def load_data(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Load training and test datasets"""
        print("📂 Loading datasets...")
        self.train_df = pd.read_csv(self.data_dir / "train.csv")
        self.test_df = pd.read_csv(self.data_dir / "test.csv")
        
        print(f"✅ Loaded {len(self.train_df)} training examples")
        print(f"✅ Loaded {len(self.test_df)} test examples")
        
        # Basic statistics
        print(f"\n📊 Training topics distribution:")
        print(self.train_df['topic'].value_counts())
        
        return self.train_df, self.test_df
    
    def clean_text(self, text: str) -> str:
        """Clean and normalize text"""
        if pd.isna(text):
            return ""
        
        # Remove extra whitespace
        text = ' '.join(text.split())
        
        # Normalize quotes
        text = text.replace('"', '"').replace('"', '"')
        text = text.replace(''', "'").replace(''', "'")
        
        return text.strip()
    
    def extract_numbers(self, text: str) -> List[float]:
        """Extract all numbers from text"""
        # Pattern matches integers, decimals, fractions
        pattern = r'\b\d+\.?\d*\b'
        numbers = re.findall(pattern, text)
        return [float(n) for n in numbers]
    
    def extract_time_durations(self, text: str) -> List[Tuple[float, str]]:
        """Extract time durations (e.g., '2 hours', '30 minutes')"""
        pattern = r'(\d+(?:\.\d+)?)\s*(hour|minute|second|day|week|month|year)s?'
        matches = re.findall(pattern, text.lower())
        return [(float(val), unit) for val, unit in matches]
    
    def extract_distances(self, text: str) -> List[Tuple[float, str]]:
        """Extract distances (e.g., '50 miles', '10 km')"""
        pattern = r'(\d+(?:\.\d+)?)\s*(mile|km|kilometer|meter|feet|inch)s?'
        matches = re.findall(pattern, text.lower())
        return [(float(val), unit) for val, unit in matches]
    
    def identify_problem_type(self, row: pd.Series) -> Dict[str, bool]:
        """
        Identify specific problem characteristics
        Returns flags for different reasoning types needed
        """
        topic = row['topic'].lower()
        problem = row['problem_statement'].lower()
        
        flags = {
            'requires_math': False,
            'requires_sequence': False,
            'requires_spatial': False,
            'requires_logic': False,
            'requires_optimization': False,
            'requires_symbolic': False,
            'has_numbers': False,
            'has_multiple_steps': False
        }
        
        # Check for mathematical problems
        if any(word in problem for word in ['calculate', 'sum', 'product', 'divide', 'multiply', 'percentage']):
            flags['requires_math'] = True
        
        # Check for sequences
        if 'sequence' in topic or 'sequence' in problem:
            flags['requires_sequence'] = True
        
        # Check for spatial reasoning
        if 'spatial' in topic or any(word in problem for word in ['cube', 'corner', 'room', 'door', 'direction']):
            flags['requires_spatial'] = True
        
        # Check for logic puzzles
        if any(word in problem for word in ['always lies', 'always tells', 'truth', 'liar', 'logic']):
            flags['requires_logic'] = True
        
        # Check for optimization
        if 'optimization' in topic or any(word in problem for word in ['minimum', 'maximum', 'optimal', 'shortest', 'least']):
            flags['requires_optimization'] = True
        
        # Check for symbolic math
        if any(word in problem for word in ['equation', 'solve for', 'variable', 'formula']):
            flags['requires_symbolic'] = True
        
        # Check if numbers present
        numbers = self.extract_numbers(problem)
        flags['has_numbers'] = len(numbers) > 0
        
        # Check for multi-step problems
        if any(word in problem for word in ['first', 'then', 'after', 'next', 'finally', 'sequence']):
            flags['has_multiple_steps'] = True
        
        return flags
    
    def preprocess_training_data(self) -> pd.DataFrame:
        """Full preprocessing pipeline for training data"""
        print("\n🔧 Preprocessing training data...")
        
        # Clean text columns
        for col in ['problem_statement', 'solution']:
            if col in self.train_df.columns:
                self.train_df[col] = self.train_df[col].apply(self.clean_text)
        
        # Clean answer options
        for i in range(1, 6):
            col = f'answer_option_{i}'
            if col in self.train_df.columns:
                self.train_df[col] = self.train_df[col].apply(self.clean_text)
        
        # Extract problem characteristics
        problem_types = self.train_df.apply(self.identify_problem_type, axis=1)
        problem_types_df = pd.DataFrame(problem_types.tolist())
        
        # Combine with original data
        self.train_df = pd.concat([self.train_df, problem_types_df], axis=1)
        
        print("✅ Training data preprocessed")
        return self.train_df
    
    def preprocess_test_data(self) -> pd.DataFrame:
        """Full preprocessing pipeline for test data"""
        print("\n🔧 Preprocessing test data...")
        
        # Clean text columns
        self.test_df['problem_statement'] = self.test_df['problem_statement'].apply(self.clean_text)
        
        # Clean answer options
        for i in range(1, 6):
            col = f'answer_option_{i}'
            if col in self.test_df.columns:
                self.test_df[col] = self.test_df[col].apply(self.clean_text)
        
        # Extract problem characteristics
        problem_types = self.test_df.apply(self.identify_problem_type, axis=1)
        problem_types_df = pd.DataFrame(problem_types.tolist())
        
        # Combine with original data
        self.test_df = pd.concat([self.test_df, problem_types_df], axis=1)
        
        print("✅ Test data preprocessed")
        return self.test_df
    
    def create_problem_summary(self, row: pd.Series) -> str:
        """Create a concise summary of the problem"""
        summary = f"Topic: {row['topic']}\n"
        summary += f"Problem: {row['problem_statement'][:200]}...\n"
        
        if 'solution' in row and pd.notna(row['solution']):
            summary += f"Solution approach: {row['solution'][:150]}...\n"
        
        return summary
    
    def save_preprocessed_data(self):
        """Save preprocessed data"""
        if self.train_df is not None:
            self.train_df.to_csv(self.data_dir / "train_preprocessed.csv", index=False)
            print(f"💾 Saved preprocessed training data")
        
        if self.test_df is not None:
            self.test_df.to_csv(self.data_dir / "test_preprocessed.csv", index=False)
            print(f"💾 Saved preprocessed test data")


def main():
    """Demo preprocessing"""
    preprocessor = DataPreprocessor(data_dir="../data")
    
    # Load data
    train_df, test_df = preprocessor.load_data()
    
    # Preprocess
    train_df = preprocessor.preprocess_training_data()
    test_df = preprocessor.preprocess_test_data()
    
    # Save
    preprocessor.save_preprocessed_data()
    
    # Show sample
    print("\n📋 Sample preprocessed entry:")
    print(preprocessor.create_problem_summary(train_df.iloc[0]))
    print(f"\nProblem flags: {train_df.iloc[0][['requires_math', 'requires_spatial', 'requires_optimization']].to_dict()}")


if __name__ == "__main__":
    main()
