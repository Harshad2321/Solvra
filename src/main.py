# Main script for the Solvra reasoning system
# This runs the whole pipeline from loading data to generating predictions

import pandas as pd
from pathlib import Path
from tqdm import tqdm
import warnings
import time
import numpy as np
from sklearn.metrics import f1_score, accuracy_score, classification_report, confusion_matrix
warnings.filterwarnings('ignore')

from preprocess import DataPreprocessor
from reasoning_agent import ReasoningAgent
from verifier import ReasoningVerifier
from trace_logger import TraceLogger
from ml_enhancer import MLEnhancer, EnsemblePredictor


class SolvraPipeline:
    # Main class to run everything
    
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
        
        # Performance metrics
        self.inference_times = []
        self.performance_metrics = {}
    
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
        y_true = []
        y_pred = []
        train_times = []
        
        for idx in tqdm(range(min(num_examples, len(self.train_df))), desc="Analyzing"):
            problem = self.train_df.iloc[idx].to_dict()
            
            # Track inference time
            start_time = time.time()
            
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
            
            # Record inference time
            inference_time = time.time() - start_time
            train_times.append(inference_time)
            
            # Log trace
            self.logger.log_problem_trace(
                idx, problem, corrected_prediction, trace,
                self.verifier.get_verification_report()
            )
            
            # Collect for metrics
            true_label = problem.get('correct_option_number')
            y_true.append(true_label)
            y_pred.append(corrected_prediction)
            
            # Check if correct
            if corrected_prediction == true_label:
                correct_count += 1
        
        # Calculate metrics
        accuracy = (correct_count / num_examples) * 100
        f1_macro = f1_score(y_true, y_pred, average='macro') * 100
        avg_inference_time = np.mean(train_times)
        
        print(f"\n✅ Training complete")
        print(f"📊 Training Accuracy: {accuracy:.2f}% ({correct_count}/{num_examples})")
        print(f"📊 Macro F1 Score: {f1_macro:.2f}%")
        print(f"⏱️  Average Inference Time: {avg_inference_time:.4f}s per problem")
        print(f"⏱️  Total Training Time: {sum(train_times):.2f}s")
        
        # Store metrics
        self.performance_metrics['train_accuracy'] = accuracy
        self.performance_metrics['train_f1_macro'] = f1_macro
        self.performance_metrics['train_avg_time'] = avg_inference_time
        
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
        self.inference_times = []
        
        for idx in tqdm(range(len(self.test_df)), desc="Predicting"):
            problem = self.test_df.iloc[idx].to_dict()
            
            # Track inference time
            start_time = time.time()
            
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
            
            # Record inference time
            inference_time = time.time() - start_time
            self.inference_times.append(inference_time)
            
            self.predictions.append(corrected_prediction)
            
            # Log trace (optional for test set)
            if save_traces and idx < 20:  # Save first 20 for review
                self.logger.log_problem_trace(
                    idx, problem, corrected_prediction, trace,
                    self.verifier.get_verification_report()
                )
        
        # Calculate test metrics
        avg_test_time = np.mean(self.inference_times)
        total_test_time = sum(self.inference_times)
        
        print(f"✅ Predictions complete")
        print(f"⏱️  Average Inference Time: {avg_test_time:.4f}s per problem")
        print(f"⏱️  Total Test Time: {total_test_time:.2f}s")
        
        # Store metrics
        self.performance_metrics['test_avg_time'] = avg_test_time
        self.performance_metrics['test_total_time'] = total_test_time
        return self.predictions
    
    def save_predictions(self, filename: str = "predictions.csv"):
        """
        Save predictions in the required format with all columns
        """
        output_path = self.data_dir / filename
        
        # Create submission DataFrame with all required columns
        # Get solution column if it exists, otherwise create empty strings
        if 'solution' in self.test_df.columns:
            solutions = self.test_df['solution'].values
        else:
            # Create solution explanations from reasoning traces if available
            solutions = [''] * len(self.test_df)
        
        submission_df = pd.DataFrame({
            'topic': self.test_df['topic'].values,
            'problem_statement': self.test_df['problem_statement'].values,
            'solution': solutions,
            'correct option': self.predictions
        })
        
        # Try to save, handle permission errors by using temp file
        try:
            submission_df.to_csv(output_path, index=False)
        except PermissionError:
            # File might be open, try alternate name
            temp_path = self.data_dir / "predictions_new.csv"
            submission_df.to_csv(temp_path, index=False)
            output_path = temp_path
            print(f"⚠️  Original file locked, saved as predictions_new.csv instead")
        
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
    
    def generate_performance_report(self):
        """Generate comprehensive performance metrics report"""
        print("\n" + "="*70)
        print("📊 PERFORMANCE METRICS REPORT")
        print("="*70)
        
        report_lines = []
        report_lines.append("="*70)
        report_lines.append("SOLVRA - AGENTIC REASONING SYSTEM - PERFORMANCE REPORT")
        report_lines.append("="*70)
        report_lines.append("")
        
        # Training Metrics
        if 'train_accuracy' in self.performance_metrics:
            report_lines.append("🎓 TRAINING METRICS")
            report_lines.append("-"*70)
            report_lines.append(f"  Accuracy:           {self.performance_metrics['train_accuracy']:.2f}%")
            report_lines.append(f"  Macro F1 Score:     {self.performance_metrics['train_f1_macro']:.2f}%")
            report_lines.append(f"  Avg Inference Time: {self.performance_metrics['train_avg_time']:.4f}s per problem")
            report_lines.append("")
        
        # Test Metrics
        if 'test_avg_time' in self.performance_metrics:
            report_lines.append("🔮 TEST SET METRICS")
            report_lines.append("-"*70)
            report_lines.append(f"  Test Problems:      {len(self.test_df)}")
            report_lines.append(f"  Avg Inference Time: {self.performance_metrics['test_avg_time']:.4f}s per problem")
            report_lines.append(f"  Total Test Time:    {self.performance_metrics['test_total_time']:.2f}s")
            report_lines.append(f"  Throughput:         {len(self.test_df)/self.performance_metrics['test_total_time']:.2f} problems/sec")
            report_lines.append("")
        
        # Inference Time Distribution
        if self.inference_times:
            report_lines.append("⏱️  INFERENCE TIME ANALYSIS")
            report_lines.append("-"*70)
            report_lines.append(f"  Min Time:           {np.min(self.inference_times):.4f}s")
            report_lines.append(f"  Max Time:           {np.max(self.inference_times):.4f}s")
            report_lines.append(f"  Median Time:        {np.median(self.inference_times):.4f}s")
            report_lines.append(f"  Std Dev:            {np.std(self.inference_times):.4f}s")
            report_lines.append("")
        
        # System Configuration
        report_lines.append("⚙️  SYSTEM CONFIGURATION")
        report_lines.append("-"*70)
        report_lines.append(f"  Training Samples:   {len(self.train_df)}")
        report_lines.append(f"  Test Samples:       {len(self.test_df)}")
        report_lines.append(f"  Solvers:            Math, Logic, Spatial, Sequence")
        report_lines.append(f"  Verification:       Enabled")
        report_lines.append(f"  ML Enhancement:     Enabled")
        report_lines.append(f"  Ensemble:           Enabled")
        report_lines.append("")
        
        report_lines.append("="*70)
        
        # Print report
        report_text = "\n".join(report_lines)
        print(report_text)
        
        # Save report to file
        report_path = self.reports_dir / "performance_metrics.txt"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report_text)
        
        print(f"\n💾 Performance report saved to: {report_path}")
        
        # Save metrics as JSON
        import json
        metrics_path = self.reports_dir / "performance_metrics.json"
        with open(metrics_path, 'w') as f:
            json.dump(self.performance_metrics, f, indent=2)
        
        print(f"💾 Metrics JSON saved to: {metrics_path}")
    
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
        
        # Step 5: Generate comprehensive performance report
        self.generate_performance_report()
        
        print("\n" + "="*60)
        print("🎉 SOLVRA PIPELINE COMPLETED SUCCESSFULLY")
        print("="*60)
        print(f"\n✅ Training Accuracy: {train_accuracy:.2f}%")
        if 'train_f1_macro' in self.performance_metrics:
            print(f"✅ Training F1 Score: {self.performance_metrics['train_f1_macro']:.2f}%")
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
