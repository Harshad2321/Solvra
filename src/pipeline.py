import argparse
import json
import time
import pandas as pd
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.classifier import QuestionTypeClassifier
from src.planner import ReasoningPlanner
from src.solver import MathSolver
from src.verifier import SolutionVerifier
from src.reasoning_trace import ReasoningTraceRecorder
from src.log_utils import setup_logger

logger = setup_logger()

class SolvraPipeline:
    def __init__(self, config_path="src/config.json"):
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        
        self.classifier = QuestionTypeClassifier(model_path=self.config['model_path'])
        if Path(self.config['model_path']).exists():
            self.classifier.load_model(self.config['model_path'])
        
        self.planner = ReasoningPlanner(self.classifier)
        self.solver = MathSolver()
        self.verifier = SolutionVerifier()
        self.trace_recorder = ReasoningTraceRecorder()
        
    def process_question(self, question):
        start_time = time.time()
        
        plan = self.planner.create_plan(question)
        
        solution = self.solver.solve(question, plan)
        
        verification = self.verifier.verify(question, solution, plan)
        
        trace_id = self.trace_recorder.create_trace(question, plan, solution, verification)
        
        inference_time = time.time() - start_time
        
        return {
            'question': question,
            'predicted_answer': verification['verified_answer'],
            'trace_id': trace_id,
            'confidence': verification['confidence'],
            'inference_time': inference_time
        }
    
    def run_pipeline(self, input_csv=None, output_csv=None):
        if input_csv is None:
            input_csv = self.config['test_data']
        if output_csv is None:
            output_csv = self.config['output_path']
        
        logger.info(f"Running pipeline on {input_csv}")
        
        df = pd.read_csv(input_csv)
        results = []
        
        for idx, row in df.iterrows():
            question = row['question']
            logger.info(f"Processing question {idx+1}/{len(df)}")
            
            result = self.process_question(question)
            results.append(result)
        
        output_df = pd.DataFrame(results)
        
        Path(output_csv).parent.mkdir(parents=True, exist_ok=True)
        output_df.to_csv(output_csv, index=False)
        logger.info(f"Results saved to {output_csv}")
        
        self.trace_recorder.save_traces()
        
        return output_df

def main():
    parser = argparse.ArgumentParser(description='Solvra Mathematical Reasoning Pipeline')
    parser.add_argument('--input', type=str, default='data/test.csv', help='Input CSV file')
    parser.add_argument('--output', type=str, default='data/output.csv', help='Output CSV file')
    parser.add_argument('--config', type=str, default='src/config.json', help='Config JSON file')
    
    args = parser.parse_args()
    
    pipeline = SolvraPipeline(config_path=args.config)
    pipeline.run_pipeline(input_csv=args.input, output_csv=args.output)

if __name__ == '__main__':
    main()
