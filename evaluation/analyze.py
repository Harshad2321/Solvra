import pandas as pd
import json
import sys
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.log_utils import setup_logger

logger = setup_logger()

class ResultsAnalyzer:
    def __init__(self):
        pass
    
    def analyze_by_category(self, test_csv, output_csv):
        test_df = pd.read_csv(test_csv)
        output_df = pd.read_csv(output_csv)
        
        merged_df = test_df.merge(output_df, on='question', how='inner')
        
        category_stats = defaultdict(lambda: {'total': 0, 'correct': 0, 'accuracy': 0.0})
        
        for idx, row in merged_df.iterrows():
            question_type = row['type']
            true_answer = self.normalize_answer(row['answer'])
            pred_answer = self.normalize_answer(row['predicted_answer'])
            
            category_stats[question_type]['total'] += 1
            
            if self.answers_match(true_answer, pred_answer):
                category_stats[question_type]['correct'] += 1
        
        for category in category_stats:
            total = category_stats[category]['total']
            correct = category_stats[category]['correct']
            category_stats[category]['accuracy'] = correct / total if total > 0 else 0
        
        logger.info("Per-category accuracy:")
        for category, stats in category_stats.items():
            logger.info(f"{category}: {stats['accuracy']:.4f} ({stats['correct']}/{stats['total']})")
        
        return dict(category_stats)
    
    def analyze_reasoning_consistency(self, traces_file='data/reasoning_traces.json'):
        if not Path(traces_file).exists():
            logger.warning(f"Traces file {traces_file} not found")
            return {}
        
        with open(traces_file, 'r') as f:
            traces = json.load(f)
        
        consistency_report = {
            'total_traces': len(traces),
            'valid_solutions': 0,
            'invalid_solutions': 0,
            'avg_confidence': 0.0,
            'avg_steps': 0.0
        }
        
        confidences = []
        steps_counts = []
        
        for trace in traces:
            if trace['verification']['is_valid']:
                consistency_report['valid_solutions'] += 1
            else:
                consistency_report['invalid_solutions'] += 1
            
            confidences.append(trace['verification']['confidence'])
            steps_counts.append(len(trace['solution']['steps_executed']))
        
        if confidences:
            consistency_report['avg_confidence'] = sum(confidences) / len(confidences)
        if steps_counts:
            consistency_report['avg_steps'] = sum(steps_counts) / len(steps_counts)
        
        logger.info(f"Reasoning consistency report:")
        logger.info(f"Valid solutions: {consistency_report['valid_solutions']}/{consistency_report['total_traces']}")
        logger.info(f"Average confidence: {consistency_report['avg_confidence']:.4f}")
        logger.info(f"Average steps per solution: {consistency_report['avg_steps']:.2f}")
        
        return consistency_report
    
    def generate_full_report(self, test_csv='data/test.csv', output_csv='data/output.csv', 
                           traces_file='data/reasoning_traces.json'):
        print("\n" + "="*60)
        print("SOLVRA ANALYSIS REPORT")
        print("="*60)
        
        category_stats = self.analyze_by_category(test_csv, output_csv)
        
        print("\n--- Per-Category Accuracy ---")
        for category, stats in category_stats.items():
            print(f"{category:15s}: {stats['accuracy']:.4f} ({stats['correct']}/{stats['total']})")
        
        consistency_report = self.analyze_reasoning_consistency(traces_file)
        
        print("\n--- Reasoning Consistency ---")
        print(f"Total traces: {consistency_report['total_traces']}")
        print(f"Valid solutions: {consistency_report['valid_solutions']}")
        print(f"Invalid solutions: {consistency_report['invalid_solutions']}")
        print(f"Average confidence: {consistency_report['avg_confidence']:.4f}")
        print(f"Average steps: {consistency_report['avg_steps']:.2f}")
        
        print("\n" + "="*60)
        
        return {
            'category_stats': category_stats,
            'consistency_report': consistency_report
        }
    
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

if __name__ == '__main__':
    analyzer = ResultsAnalyzer()
    analyzer.generate_full_report()
