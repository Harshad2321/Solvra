"""
Solvra - Main Pipeline
Orchestrates the entire reasoning system from data loading to prediction generation
Enhanced with ML pattern learning for maximum accuracy
"""

import pandas as pd
from pathlib import Path
from tqdm import tqdm
import warnings
warnings.filterwarnings('ignore')

from preprocess import DataPreprocessor
from reasoning_agent import ReasoningAgent
from verifier import ReasoningVerifier
from trace_logger import TraceLogger
from ml_enhancer import MLEnhancer, EnsemblePredictor


class SolvraPipeline:
    """
    Main pipeline that orchestrates the entire Solvra reasoning system
    """
    
    def __init__(self, data_dir: str = "../data", reports_dir: str = "../reports"):
        self.data_dir = Path(data_dir)
        self.reports_dir = Path(reports_dir)
        
        # Initialize components
        self.preprocessor = DataPreprocessor(data_dir=str(self.data_dir))
        self.agent = ReasoningAgent()
        self.verifier = ReasoningVerifier()
        self.logger = TraceLogger(log_dir=str(self.reports_dir))
        
        # Initialize ML components
        self.ml_enhancer = MLEnhancer()
        self.ensemble = None
        
        # Data
        self.train_df = None
        self.test_df = None
        self.predictions = []
    
    def load_and_preprocess(self):
        """Load and preprocess all data"""
        print("🚀 SOLVRA PIPELINE STARTED")
        print("="*60 + "\n")
        
        # Load data
        self.train_df, self.test_df = self.preprocessor.load_data()
        
        # Preprocess
        self.train_df = self.preprocessor.preprocess_training_data()
        self.test_df = self.preprocessor.preprocess_test_data()
        
        # Save preprocessed data
        self.preprocessor.save_preprocessed_data()
    
    def train_on_examples(self, num_examples: int = 50):
        """
        Enhanced training: Learn patterns from training data + analyze examples
        """
        print(f"\n🎓 Training ML Enhancer on all {len(self.train_df)} examples...")
        print("-"*60)
        
        # Train ML enhancer on full training set
        self.ml_enhancer.train(self.train_df)
        
        # Initialize ensemble predictor
        self.ensemble = EnsemblePredictor(self.ml_enhancer)
        
        print(f"\n🧪 Analyzing {num_examples} training examples for verification...")
        print("-"*60)
        
        correct_count = 0
        
        for idx in tqdm(range(min(num_examples, len(self.train_df))), desc="Analyzing"):
            problem = self.train_df.iloc[idx].to_dict()
            
            # Run reasoning
            prediction, trace = self.agent.reason_step_by_step(problem)
            
            # Use ensemble prediction
            final_prediction, confidence = self.ensemble.ensemble_predict(
                problem, prediction, 0.8  # Base confidence
            )
            
            # Verify and correct if needed
            corrected_prediction = self.verifier.apply_correction_heuristics(
                problem, final_prediction, trace
            )
            
            # Log trace
            self.logger.log_problem_trace(
                idx, problem, corrected_prediction, trace,
                self.verifier.get_verification_report()
            )
            
            # Check if correct
            if corrected_prediction == problem.get('correct_option_number'):
                correct_count += 1
        
        accuracy = (correct_count / num_examples) * 100
        print(f"\n✅ Training complete")
        print(f"📊 Training Accuracy: {accuracy:.2f}% ({correct_count}/{num_examples})")
        
        # Print detailed summary
        self.logger.print_summary()
        
        return accuracy
    
    def predict_test_set(self, save_traces: bool = True):
        """
        Generate predictions for the entire test set using ensemble approach
        """
        print(f"\n🔮 Generating predictions for {len(self.test_df)} test problems...")
        print("-"*60)
        
        if not self.ml_enhancer.trained:
            print("⚠️  Warning: ML enhancer not trained. Training now...")
            self.ml_enhancer.train(self.train_df)
            self.ensemble = EnsemblePredictor(self.ml_enhancer)
        
        self.predictions = []
        
        for idx in tqdm(range(len(self.test_df)), desc="Predicting"):
            problem = self.test_df.iloc[idx].to_dict()
            
            # Run reasoning
            prediction, trace = self.agent.reason_step_by_step(problem)
            
            # Use ensemble prediction for better accuracy
            if self.ensemble:
                corrected_prediction, confidence = self.ensemble.ensemble_predict(
                    problem, prediction, 0.8
                )
            else:
                # Fallback to verification
                corrected_prediction = self.verifier.apply_correction_heuristics(
                    problem, prediction, trace
                )
            
            self.predictions.append(corrected_prediction)
            
            # Log trace (optional for test set)
            if save_traces and idx < 20:  # Save first 20 for review
                self.logger.log_problem_trace(
                    idx, problem, corrected_prediction, trace,
                    self.verifier.get_verification_report()
                )
        
        print(f"✅ Predictions complete")
        return self.predictions
    
    def save_predictions(self, filename: str = "predictions.csv"):
        """
        Save predictions in the required format
        """
        output_path = self.data_dir / filename
        
        # Create submission DataFrame
        submission_df = pd.DataFrame({
            'correct option': self.predictions
        })
        
        submission_df.to_csv(output_path, index=False)
        print(f"\n💾 Predictions saved to: {output_path}")
        
        # Show sample predictions
        print("\n📋 Sample predictions:")
        print(submission_df.head(10))
    
    def generate_reports(self):
        """
        Generate all analysis reports
        """
        print("\n📊 Generating reports...")
        
        # Save traces
        self.logger.save_traces_json()
        self.logger.save_traces_csv()
        
        # Generate HTML report
        self.logger.generate_html_report()
        
        # Generate evaluation metrics if we have ground truth
        if 'correct_option_number' in self.train_df.columns:
            self._generate_evaluation_report()
    
    def _generate_evaluation_report(self):
        """Generate detailed evaluation report"""
        print("\n📈 Generating evaluation report...")
        
        # This would contain detailed metrics
        # For now, the logger already handles most of this
        pass
    
    def run_full_pipeline(self, train_samples: int = 100, 
                         generate_test_predictions: bool = True):
        """
        Run the complete pipeline end-to-end
        """
        # Step 1: Load and preprocess
        self.load_and_preprocess()
        
        # Step 2: Analyze training examples
        train_accuracy = self.train_on_examples(num_examples=train_samples)
        
        # Step 3: Generate reports for training
        self.generate_reports()
        
        # Step 4: Generate test predictions
        if generate_test_predictions:
            self.predict_test_set(save_traces=True)
            self.save_predictions()
        
        print("\n" + "="*60)
        print("🎉 SOLVRA PIPELINE COMPLETED SUCCESSFULLY")
        print("="*60)
        print(f"\n✅ Training Accuracy: {train_accuracy:.2f}%")
        print(f"📁 Reports saved in: {self.reports_dir}")
        print(f"📁 Predictions saved in: {self.data_dir}")
        print("\n🏆 Ready for Ethos 2025 submission!")


def main():
    """
    Main entry point for Solvra
    """
    # Initialize pipeline
    pipeline = SolvraPipeline(
        data_dir="../data",
        reports_dir="../reports"
    )
    
    # Run full pipeline
    # Start with smaller sample for testing, increase for final run
    pipeline.run_full_pipeline(
        train_samples=50,  # Increase to 534 for full training analysis
        generate_test_predictions=True
    )


if __name__ == "__main__":
    main()
