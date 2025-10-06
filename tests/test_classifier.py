import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.classifier import QuestionTypeClassifier

def test_classifier_initialization():
    classifier = QuestionTypeClassifier()
    assert classifier is not None
    assert classifier.vectorizer is not None
    assert classifier.classifier is not None

def test_classifier_predict_type():
    classifier = QuestionTypeClassifier()
    
    question = "What is 5 plus 3?"
    
    result = classifier.predict_type(question)
    
    assert result is not None
    assert isinstance(result, str)

def test_classifier_returns_valid_type():
    valid_types = ['arithmetic', 'algebra', 'geometry', 'logic', 'word_problem', 'comparison', 'pattern']
    
    classifier = QuestionTypeClassifier()
    
    if Path('models/question_type.pkl').exists():
        classifier.load_model('models/question_type.pkl')
        
        question = "Calculate 10 + 20"
        result = classifier.predict_type(question)
        
        assert result is not None
