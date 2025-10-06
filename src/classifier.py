import pandas as pd
import pickle
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from src.log_utils import setup_logger

logger = setup_logger()

class QuestionTypeClassifier:
    def __init__(self, model_path=None):
        self.model_path = model_path
        self.vectorizer = TfidfVectorizer(max_features=1000, ngram_range=(1, 2))
        self.classifier = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model_loaded = False
        
    def train(self, train_csv_path):
        logger.info(f"Training classifier on {train_csv_path}")
        df = pd.read_csv(train_csv_path)
        
        X = df['question'].values
        y = df['type'].values
        
        X_train, X_val, y_train, y_val = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        X_train_vec = self.vectorizer.fit_transform(X_train)
        X_val_vec = self.vectorizer.transform(X_val)
        
        self.classifier.fit(X_train_vec, y_train)
        
        y_pred = self.classifier.predict(X_val_vec)
        logger.info(f"Validation results:\n{classification_report(y_val, y_pred)}")
        
        if self.model_path:
            self.save_model(self.model_path)
        
        return self
    
    def save_model(self, path):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'wb') as f:
            pickle.dump({
                'vectorizer': self.vectorizer,
                'classifier': self.classifier
            }, f)
        logger.info(f"Model saved to {path}")
    
    def load_model(self, path):
        with open(path, 'rb') as f:
            model_data = pickle.load(f)
        self.vectorizer = model_data['vectorizer']
        self.classifier = model_data['classifier']
        self.model_loaded = True
        logger.info(f"Model loaded from {path}")
        return self
    
    def predict_type(self, question):
        if not self.model_loaded and self.model_path:
            self.load_model(self.model_path)
        
        question_vec = self.vectorizer.transform([question])
        prediction = self.classifier.predict(question_vec)[0]
        return prediction

def train_classifier(train_csv, model_path):
    classifier = QuestionTypeClassifier(model_path=model_path)
    classifier.train(train_csv)
    return classifier
