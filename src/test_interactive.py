"""
Solvra - Interactive Testing Script
Test individual problems interactively
"""

from reasoning_agent import ReasoningAgent
from verifier import ReasoningVerifier
from preprocess import DataPreprocessor
import sys


class InteractiveTester:
    """Interactive problem solver for testing"""
    
    def __init__(self):
        self.agent = ReasoningAgent()
        self.verifier = ReasoningVerifier()
        self.preprocessor = DataPreprocessor(data_dir="../data")
    
    def load_problem(self, problem_idx: int, dataset='train'):
        """Load a problem by index"""
        if dataset == 'train':
            if self.preprocessor.train_df is None:
                self.preprocessor.train_df, _ = self.preprocessor.load_data()
                self.preprocessor.train_df = self.preprocessor.preprocess_training_data()
            
            if problem_idx >= len(self.preprocessor.train_df):
                print(f"Error: Problem {problem_idx} not found. Max: {len(self.preprocessor.train_df)-1}")
                return None
            
            return self.preprocessor.train_df.iloc[problem_idx].to_dict()
        
        else:  # test
            if self.preprocessor.test_df is None:
                _, self.preprocessor.test_df = self.preprocessor.load_data()
                self.preprocessor.test_df = self.preprocessor.preprocess_test_data()
            
            if problem_idx >= len(self.preprocessor.test_df):
                print(f"Error: Problem {problem_idx} not found. Max: {len(self.preprocessor.test_df)-1}")
                return None
            
            return self.preprocessor.test_df.iloc[problem_idx].to_dict()
    
    def display_problem(self, problem: dict):
        """Display problem in formatted way"""
        print("\n" + "="*70)
        print(f"PROBLEM: {problem.get('topic', 'Unknown')}")
        print("="*70)
        print(f"\n{problem['problem_statement']}")
        print("\nOPTIONS:")
        for i in range(1, 6):
            opt_key = f'answer_option_{i}'
            if opt_key in problem and problem[opt_key]:
                print(f"  {i}. {problem[opt_key]}")
        
        if 'correct_option_number' in problem:
            print(f"\n✓ Correct Answer: Option {problem['correct_option_number']}")
        
        print("="*70 + "\n")
    
    def solve_and_explain(self, problem: dict):
        """Solve problem and show detailed explanation"""
        # Solve
        prediction, trace = self.agent.reason_step_by_step(problem)
        
        # Verify
        corrected = self.verifier.apply_correction_heuristics(problem, prediction, trace)
        
        # Display reasoning
        print("🤖 SOLVRA REASONING TRACE")
        print("-"*70)
        print(self.agent.get_trace_summary())
        
        # Display verification
        print("\n🔍 VERIFICATION")
        print("-"*70)
        print(self.verifier.get_verification_report())
        
        # Display answer
        print("\n🎯 FINAL ANSWER")
        print("-"*70)
        print(f"Original Prediction: Option {prediction}")
        if corrected != prediction:
            print(f"Corrected To: Option {corrected}")
        else:
            print(f"Verified: Option {corrected}")
        
        # Check if correct
        if 'correct_option_number' in problem:
            correct = int(problem['correct_option_number'])
            if corrected == correct:
                print("\n✅ CORRECT!")
            else:
                print(f"\n❌ INCORRECT (Expected: {correct})")
        
        print("="*70 + "\n")
        
        return corrected
    
    def interactive_mode(self):
        """Interactive testing mode"""
        print("\n" + "="*70)
        print("  SOLVRA INTERACTIVE TESTER")
        print("="*70)
        print("\nCommands:")
        print("  train <n>  - Test training problem n")
        print("  test <n>   - Test test problem n")
        print("  random     - Test random training problem")
        print("  quit       - Exit")
        print("="*70 + "\n")
        
        while True:
            try:
                command = input("solvra> ").strip().lower()
                
                if command == 'quit' or command == 'exit':
                    print("Goodbye!")
                    break
                
                elif command == 'random':
                    import random
                    if self.preprocessor.train_df is None:
                        self.preprocessor.train_df, _ = self.preprocessor.load_data()
                        self.preprocessor.train_df = self.preprocessor.preprocess_training_data()
                    
                    idx = random.randint(0, len(self.preprocessor.train_df)-1)
                    problem = self.load_problem(idx, 'train')
                    if problem:
                        self.display_problem(problem)
                        self.solve_and_explain(problem)
                
                elif command.startswith('train '):
                    idx = int(command.split()[1])
                    problem = self.load_problem(idx, 'train')
                    if problem:
                        self.display_problem(problem)
                        self.solve_and_explain(problem)
                
                elif command.startswith('test '):
                    idx = int(command.split()[1])
                    problem = self.load_problem(idx, 'test')
                    if problem:
                        self.display_problem(problem)
                        self.solve_and_explain(problem)
                
                elif command == 'help':
                    print("\nCommands:")
                    print("  train <n>  - Test training problem n")
                    print("  test <n>   - Test test problem n")
                    print("  random     - Test random training problem")
                    print("  quit       - Exit\n")
                
                else:
                    print("Unknown command. Type 'help' for available commands.")
            
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
                print("Type 'help' for available commands.")


def main():
    """Main entry point"""
    tester = InteractiveTester()
    
    # Check if command line arguments provided
    if len(sys.argv) > 1:
        dataset = sys.argv[1]
        idx = int(sys.argv[2]) if len(sys.argv) > 2 else 0
        
        problem = tester.load_problem(idx, dataset)
        if problem:
            tester.display_problem(problem)
            tester.solve_and_explain(problem)
    else:
        # Interactive mode
        tester.interactive_mode()


if __name__ == "__main__":
    main()
