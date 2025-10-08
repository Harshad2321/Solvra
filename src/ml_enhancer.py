"""
Solvra - Machine Learning Enhancement Module
Trains on training data to learn patterns and boost accuracy to maximum
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Any, Tuple, Optional
from collections import Counter, defaultdict
import re


class MLEnhancer:
    """
    Machine learning enhancements without external ML libraries
    Uses pattern learning, frequency analysis, and heuristic optimization
    """
    
    def __init__(self):
        self.topic_patterns = defaultdict(list)
        self.answer_distribution = defaultdict(Counter)
        self.keyword_to_answer = defaultdict(list)
        self.successful_strategies = []
        self.trained = False
    
    def extract_features(self, problem: Dict[str, Any]) -> Dict[str, Any]:
        """Extract comprehensive features from problem"""
        text = problem['problem_statement'].lower()
        
        features = {
            # Text features
            'word_count': len(text.split()),
            'number_count': len(re.findall(r'\d+', text)),
            'question_marks': text.count('?'),
            'has_minimum': 'minimum' in text or 'shortest' in text or 'least' in text,
            'has_maximum': 'maximum' in text or 'longest' in text or 'most' in text,
            
            # Topic-based
            'topic': problem.get('topic', '').lower(),
            'is_sequence': 'sequence' in problem.get('topic', '').lower(),
            'is_spatial': 'spatial' in problem.get('topic', '').lower(),
            'is_optimization': 'optimization' in problem.get('topic', '').lower(),
            'is_logic': 'logic' in problem.get('topic', '').lower() or 'riddle' in problem.get('topic', '').lower(),
            
            # Keywords
            'has_cube': 'cube' in text,
            'has_sequence_keyword': 'sequence' in text or 'pattern' in text or 'next' in text,
            'has_impossible': 'impossible' in text or 'cannot' in text,
            'has_always': 'always' in text,
            'has_never': 'never' in text,
            
            # Answer option analysis
            'has_another_answer': any('another answer' in str(problem.get(f'answer_option_{i}', '')).lower() 
                                     for i in range(1, 6)),
        }
        
        return features
    
    def train(self, training_data: pd.DataFrame) -> None:
        """
        Learn patterns from training data
        """
        print(" Training ML Enhancer on training data...")
        
        for idx, row in training_data.iterrows():
            if pd.isna(row.get('correct_option_number')):
                continue
            
            correct_answer = int(row['correct_option_number'])
            topic = row['topic'].lower() if 'topic' in row else 'unknown'
            
            # Learn topic-answer patterns
            self.topic_patterns[topic].append(correct_answer)
            
            # Extract features
            features = self.extract_features(row)
            
            # Learn feature-answer correlations
            for feature_name, feature_value in features.items():
                if feature_value and isinstance(feature_value, bool):
                    self.keyword_to_answer[feature_name].append(correct_answer)
            
            # Learn answer distribution
            self.answer_distribution[topic][correct_answer] += 1
        
        # Calculate most common answers per topic
        self.topic_best_guesses = {}
        for topic, counter in self.answer_distribution.items():
            if counter:
                self.topic_best_guesses[topic] = counter.most_common(1)[0][0]
        
        self.trained = True
        print(f" Trained on {len(training_data)} examples")
        print(f"   Learned patterns for {len(self.topic_patterns)} topics")
    
    def predict(self, problem: Dict[str, Any], base_prediction: int = None) -> Tuple[int, float]:
        """
        Predict answer using learned patterns
        Returns (prediction, confidence)
        """
        if not self.trained:
            return base_prediction or 2, 0.5
        
        features = self.extract_features(problem)
        topic = features['topic']
        
        # Strategy 1: Use topic-specific patterns
        votes = Counter()
        confidences = []
        
        # Vote based on topic patterns
        if topic in self.topic_patterns and self.topic_patterns[topic]:
            topic_predictions = self.topic_patterns[topic]
            most_common = Counter(topic_predictions).most_common(3)
            for answer, count in most_common:
                weight = count / len(topic_predictions)
                votes[answer] += weight
                confidences.append(weight)
        
        # Vote based on feature correlations
        for feature_name, feature_value in features.items():
            if feature_value and isinstance(feature_value, bool):
                if feature_name in self.keyword_to_answer:
                    predictions = self.keyword_to_answer[feature_name]
                    if predictions:
                        most_common_answer = Counter(predictions).most_common(1)[0][0]
                        votes[most_common_answer] += 0.3
        
        # Combine with base prediction
        if base_prediction:
            votes[base_prediction] += 2.0  # Strong weight for algorithmic prediction
            confidences.append(0.8)
        
        # Select winner
        if votes:
            prediction = votes.most_common(1)[0][0]
            confidence = min(sum(confidences) / len(confidences), 0.95) if confidences else 0.5
            return prediction, confidence
        
        return base_prediction or 2, 0.5
    
    def get_topic_statistics(self) -> Dict[str, Any]:
        """Get statistics about learned patterns"""
        stats = {}
        for topic, counter in self.answer_distribution.items():
            total = sum(counter.values())
            stats[topic] = {
                'total_examples': total,
                'distribution': dict(counter),
                'most_common': counter.most_common(1)[0] if counter else None
            }
        return stats


class EnsemblePredictor:
    """
    Combines multiple prediction strategies for maximum accuracy
    """
    
    def __init__(self, ml_enhancer: MLEnhancer):
        self.ml_enhancer = ml_enhancer
        self.prediction_history = []
    
    def ensemble_predict(self, problem: Dict[str, Any], 
                         algo_prediction: int,
                         algo_confidence: float) -> Tuple[int, float]:
        """
        Combine algorithmic and ML predictions
        """
        # Get ML prediction
        ml_prediction, ml_confidence = self.ml_enhancer.predict(problem, algo_prediction)
        
        # Weighted voting
        if algo_confidence > 0.9:
            # Trust algorithmic prediction if very confident
            final_prediction = algo_prediction
            final_confidence = algo_confidence
        elif ml_confidence > 0.7 and ml_prediction != algo_prediction:
            # ML has good confidence and disagrees
            # Use weighted average
            if algo_confidence > ml_confidence:
                final_prediction = algo_prediction
                final_confidence = (algo_confidence * 0.6 + ml_confidence * 0.4)
            else:
                final_prediction = ml_prediction
                final_confidence = (ml_confidence * 0.6 + algo_confidence * 0.4)
        else:
            # Default to algorithmic
            final_prediction = algo_prediction
            final_confidence = max(algo_confidence, ml_confidence)
        
        self.prediction_history.append({
            'algo_pred': algo_prediction,
            'ml_pred': ml_prediction,
            'final_pred': final_prediction,
            'algo_conf': algo_confidence,
            'ml_conf': ml_confidence,
            'final_conf': final_confidence
        })
        
        return final_prediction, final_confidence


def demo_ml_enhancer():
    """Test the ML enhancer"""
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent))
    
    from preprocess import DataPreprocessor
    
    # Load data
    preprocessor = DataPreprocessor("data")
    train_df, test_df = preprocessor.load_data()
    
    # Train ML enhancer
    ml_enhancer = MLEnhancer()
    ml_enhancer.train(train_df)
    
    # Show statistics
    stats = ml_enhancer.get_topic_statistics()
    print("\n📊 Learned Topic Statistics:")
    for topic, info in sorted(stats.items()):
        print(f"\n{topic}:")
        print(f"  Examples: {info['total_examples']}")
        if info['most_common']:
            print(f"  Most common answer: Option {info['most_common'][0]} ({info['most_common'][1]} times)")
    
    # Test prediction
    test_problem = train_df.iloc[0].to_dict()
    prediction, confidence = ml_enhancer.predict(test_problem)
    print(f"\n Test Prediction:")
    print(f"   Predicted: Option {prediction} (confidence: {confidence:.2%})")
    print(f"   Actual: Option {test_problem.get('correct_option_number', 'N/A')}")


if __name__ == "__main__":
    demo_ml_enhancer()
