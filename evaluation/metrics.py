import pandas as pd
import numpy as np
import sys
from sklearn.metrics import f1_score, accuracy_score
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.log_utils import setup_logger

logger = setup_logger()

class MetricsEvaluator:
    def __init__(self):
        pass
    
    def compute_metrics(self, test_csv, output_csv):
        test_df = pd.read_csv(test_csv)
        output_df = pd.read_csv(output_csv)
        
        merged_df = test_df.merge(output_df, on='question', how='inner')
        
        y_true = []
        y_pred = []
        
        for idx, row in merged_df.iterrows():
            true_answer = self.normalize_answer(row['answer'])
            pred_answer = self.normalize_answer(row['predicted_answer'])
            
            y_true.append(true_answer)
            y_pred.append(pred_answer)
        
        correct = sum(1 for t, p in zip(y_true, y_pred) if self.answers_match(t, p))
        accuracy = correct / len(y_true) if len(y_true) > 0 else 0
        
        inference_times = output_df['inference_time'].values
        avg_inference_time = np.mean(inference_times)
        
        metrics = {
            'accuracy': accuracy,
            'total_questions': len(y_true),
            'correct_answers': correct,
            'average_inference_time': avg_inference_time,
            'inference_times': inference_times.tolist()
        }
        
        logger.info(f"Accuracy: {accuracy:.4f}")
        logger.info(f"Average Inference Time: {avg_inference_time:.4f}s")
        
        return metrics
    
    def compute_macro_f1(self, test_csv, output_csv):
        test_df = pd.read_csv(test_csv)
        output_df = pd.read_csv(output_csv)
        
        merged_df = test_df.merge(output_df, on='question', how='inner')
        
        types = test_df['type'].unique()
        f1_scores = []
        
        for question_type in types:
            type_df = merged_df[merged_df['type'] == question_type]
            
            y_true = []
            y_pred = []
            
            for idx, row in type_df.iterrows():
                true_answer = self.normalize_answer(row['answer'])
                pred_answer = self.normalize_answer(row['predicted_answer'])
                
                match = self.answers_match(true_answer, pred_answer)
                y_true.append(1 if match else 0)
                y_pred.append(1)
            
            if len(y_true) > 0:
                type_accuracy = sum(y_true) / len(y_true)
                f1_scores.append(type_accuracy)
        
        macro_f1 = np.mean(f1_scores) if f1_scores else 0
        
        logger.info(f"Macro F1 Score: {macro_f1:.4f}")
        
        return macro_f1
    
    def normalize_answer(self, answer):
        if pd.isna(answer):
            return None
        if isinstance(answer, str):
            answer = answer.strip().lower()
            try:
                return float(answer)
            except ValueError:
                return answer
        return answer
    
    def answers_match(self, true_answer, pred_answer):
        if true_answer is None or pred_answer is None:
            return False
        
        if isinstance(true_answer, (int, float)) and isinstance(pred_answer, (int, float)):
            return abs(true_answer - pred_answer) < 0.01
        
        return str(true_answer).lower().strip() == str(pred_answer).lower().strip()

def evaluate_model(test_csv='data/test.csv', output_csv='data/output.csv'):
    evaluator = MetricsEvaluator()
    metrics = evaluator.compute_metrics(test_csv, output_csv)
    macro_f1 = evaluator.compute_macro_f1(test_csv, output_csv)
    
    print(f"\nEvaluation Results:")
    print(f"Accuracy: {metrics['accuracy']:.4f}")
    print(f"Macro F1 Score: {macro_f1:.4f}")
    print(f"Average Inference Time: {metrics['average_inference_time']:.4f}s")
    
    return metrics, macro_f1

if __name__ == '__main__':
    evaluate_model()
