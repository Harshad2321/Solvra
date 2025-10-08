"""
Solvra - Verifier Module
Validates reasoning steps and checks for consistency
"""

from typing import Dict, List, Any, Tuple, Optional
import re


class ReasoningVerifier:
    """
    Verifies the correctness and consistency of reasoning steps
    Applies heuristics to catch common errors
    """
    
    def __init__(self):
        self.verification_rules = []
        self.warnings = []
    
    def reset_warnings(self):
        """Clear warnings for new verification"""
        self.warnings = []
    
    def add_warning(self, warning: str):
        """Add a verification warning"""
        self.warnings.append(warning)
    
    def verify_numerical_consistency(self, problem: Dict[str, Any], 
                                     predicted_value: float) -> bool:
        """
        Check if predicted numerical value makes sense in context
        """
        problem_text = problem['problem_statement'].lower()
        
        # Extract all numbers from problem
        pattern = r'\b\d+\.?\d*\b'
        numbers = [float(n) for n in re.findall(pattern, problem_text)]
        
        if not numbers:
            return True  # No numbers to compare against
        
        # Check if prediction is within reasonable range
        min_val = min(numbers)
        max_val = max(numbers)
        range_val = max_val - min_val
        
        # Prediction should generally be within 10x the range
        if predicted_value < min_val - 10 * range_val or predicted_value > max_val + 10 * range_val:
            self.add_warning(f"Predicted value {predicted_value} seems out of reasonable range")
            return False
        
        return True
    
    def verify_option_consistency(self, problem: Dict[str, Any], 
                                   predicted_option: int) -> bool:
        """
        Verify that the predicted option makes sense
        """
        if predicted_option < 1 or predicted_option > 5:
            self.add_warning(f"Invalid option number: {predicted_option}")
            return False
        
        # Check if option exists
        opt_key = f'answer_option_{predicted_option}'
        if opt_key not in problem or not problem[opt_key]:
            self.add_warning(f"Option {predicted_option} is empty")
            return False
        
        return True
    
    def verify_logical_consistency(self, reasoning_trace: List[Dict]) -> bool:
        """
        Check if reasoning steps are logically consistent
        """
        if not reasoning_trace:
            self.add_warning("No reasoning trace provided")
            return False
        
        # Check for contradictions
        results = [step.get('result') for step in reasoning_trace if step.get('result')]
        
        # Look for None values that might indicate failures
        none_count = sum(1 for r in results if r is None)
        if none_count > len(results) / 2:
            self.add_warning("Many reasoning steps returned None - possible failures")
            return False
        
        return True
    
    def verify_sequence_prediction(self, problem: Dict[str, Any], 
                                    predicted_option: int) -> Tuple[bool, Optional[float]]:
        """
        Special verification for sequence problems
        Returns (is_valid, suggested_correction)
        """
        if 'sequence' not in problem.get('topic', '').lower():
            return True, None
        
        problem_text = problem['problem_statement']
        
        # Extract sequence from problem
        pattern = r'\b\d+\.?\d*\b'
        numbers = [float(n) for n in re.findall(pattern, problem_text)]
        
        if len(numbers) < 3:
            return True, None  # Can't verify with too few numbers
        
        # Check for common patterns
        # Arithmetic progression
        diffs = [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]
        if len(set([round(d, 2) for d in diffs])) == 1:
            # Arithmetic sequence
            next_num = numbers[-1] + diffs[0]
            
            # Check if predicted option matches
            opt_key = f'answer_option_{predicted_option}'
            if opt_key in problem:
                opt_text = problem[opt_key]
                opt_numbers = [float(n) for n in re.findall(pattern, opt_text)]
                if opt_numbers and abs(opt_numbers[0] - next_num) > 0.01:
                    self.add_warning(f"Arithmetic sequence suggests {next_num}, but option says {opt_numbers[0]}")
                    return False, next_num
        
        # Geometric progression
        if all(n != 0 for n in numbers[:-1]):
            ratios = [numbers[i+1] / numbers[i] for i in range(len(numbers)-1)]
            if len(set([round(r, 4) for r in ratios])) == 1:
                # Geometric sequence
                next_num = numbers[-1] * ratios[0]
                
                opt_key = f'answer_option_{predicted_option}'
                if opt_key in problem:
                    opt_text = problem[opt_key]
                    opt_numbers = [float(n) for n in re.findall(pattern, opt_text)]
                    if opt_numbers and abs(opt_numbers[0] - next_num) > 0.01:
                        self.add_warning(f"Geometric sequence suggests {next_num}, but option says {opt_numbers[0]}")
                        return False, next_num
        
        return True, None
    
    def verify_spatial_reasoning(self, problem: Dict[str, Any], 
                                  predicted_option: int) -> bool:
        """
        Verify spatial reasoning problems (cube painting, etc.)
        """
        if 'spatial' not in problem.get('topic', '').lower():
            return True
        
        problem_text = problem['problem_statement'].lower()
        
        # Check cube painting problems
        if 'cube' in problem_text and 'paint' in problem_text:
            # Extract cube size
            numbers = [float(n) for n in re.findall(r'\b\d+\b', problem_text)]
            
            if numbers:
                cube_size = int(numbers[0])
                total_cubes = cube_size ** 3
                
                # Verify option doesn't exceed total cubes
                opt_key = f'answer_option_{predicted_option}'
                if opt_key in problem:
                    opt_numbers = [float(n) for n in re.findall(r'\b\d+\b', problem[opt_key])]
                    if opt_numbers and opt_numbers[0] > total_cubes:
                        self.add_warning(f"Option value {opt_numbers[0]} exceeds total cubes {total_cubes}")
                        return False
        
        return True
    
    def apply_correction_heuristics(self, problem: Dict[str, Any], 
                                     predicted_option: int,
                                     reasoning_trace: List[Dict]) -> int:
        """
        Apply heuristics to potentially correct the prediction
        Returns corrected option or original if no correction needed
        """
        self.reset_warnings()
        
        # Run all verification checks
        verifications = [
            self.verify_option_consistency(problem, predicted_option),
            self.verify_logical_consistency(reasoning_trace),
            self.verify_spatial_reasoning(problem, predicted_option)
        ]
        
        # Special handling for sequences
        seq_valid, suggested = self.verify_sequence_prediction(problem, predicted_option)
        
        if not seq_valid and suggested is not None:
            # Try to find option matching the suggested value
            for i in range(1, 6):
                opt_key = f'answer_option_{i}'
                if opt_key in problem:
                    opt_numbers = [float(n) for n in re.findall(r'\b\d+\.?\d*\b', problem[opt_key])]
                    if opt_numbers and abs(opt_numbers[0] - suggested) < 0.01:
                        self.add_warning(f"Corrected option from {predicted_option} to {i}")
                        return i
        
        # If multiple verifications failed, use fallback
        failed_count = sum(1 for v in verifications if not v)
        if failed_count >= 2:
            self.add_warning("Multiple verifications failed, using fallback")
            # Fallback to middle option if unsure
            return 3
        
        return predicted_option
    
    def get_verification_report(self) -> str:
        """Get human-readable verification report"""
        if not self.warnings:
            return "✅ All verifications passed"
        
        report = "⚠️  VERIFICATION WARNINGS:\n"
        for i, warning in enumerate(self.warnings, 1):
            report += f"{i}. {warning}\n"
        return report


def demo_verifier():
    """Demo the verifier"""
    verifier = ReasoningVerifier()
    
    # Sample problem
    problem = {
        'topic': 'Sequence solving',
        'problem_statement': 'Find the next number: 2, 4, 6, 8, ?',
        'answer_option_1': '10',
        'answer_option_2': '12',
        'answer_option_3': '14',
        'answer_option_4': '16',
        'answer_option_5': 'Another answer'
    }
    
    reasoning_trace = [
        {'step': 'Extract sequence', 'result': [2, 4, 6, 8]},
        {'step': 'Identify pattern', 'result': 'arithmetic'},
        {'step': 'Predict next', 'result': 10}
    ]
    
    predicted_option = 1
    
    # Verify
    corrected = verifier.apply_correction_heuristics(problem, predicted_option, reasoning_trace)
    print(f"Original prediction: {predicted_option}")
    print(f"Corrected prediction: {corrected}")
    print(f"\n{verifier.get_verification_report()}")


if __name__ == "__main__":
    demo_verifier()
