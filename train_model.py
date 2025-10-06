import sys
sys.path.insert(0, '.')

from src.classifier import train_classifier

if __name__ == '__main__':
    print("Training classifier on train.csv...")
    classifier = train_classifier('data/train.csv', 'models/question_type.pkl')
    print("Classifier training complete. Model saved to models/question_type.pkl")
