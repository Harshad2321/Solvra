import re
from src.log_utils import setup_logger

logger = setup_logger()

class SolutionVerifier:
    def __init__(self):
        pass
    
    def verify(self, question, solution, plan):
        verification_result = {
            'is_valid': True,
            'confidence': 0.0,
            'checks': [],
            'verified_answer': solution['answer']
        }
        
        if solution.get('error'):
            verification_result['is_valid'] = False
            verification_result['confidence'] = 0.0
            verification_result['checks'].append(f"Solver error: {solution['error']}")
            return verification_result
        
        answer = solution['answer']
        
        if answer is None:
            verification_result['is_valid'] = False
            verification_result['confidence'] = 0.0
            verification_result['checks'].append("No answer generated")
            return verification_result
        
        verification_result['checks'].append("Answer exists")
        
        numbers = re.findall(r'-?\d+\.?\d*', question)
        numbers = [float(n) for n in numbers]
        
        if isinstance(answer, (int, float)):
            verification_result['checks'].append("Answer is numeric")
            
            if numbers and abs(answer) > max(abs(n) for n in numbers) * 1000:
                verification_result['confidence'] = 0.3
                verification_result['checks'].append("Warning: Answer magnitude is unusually large")
            elif numbers and answer == sum(numbers):
                verification_result['confidence'] = 0.9
                verification_result['checks'].append("Answer matches sum of inputs")
            elif numbers and answer in numbers:
                verification_result['confidence'] = 0.85
                verification_result['checks'].append("Answer is one of the input numbers")
            else:
                verification_result['confidence'] = 0.75
                verification_result['checks'].append("Answer is within reasonable bounds")
        elif isinstance(answer, bool):
            verification_result['confidence'] = 0.8
            verification_result['checks'].append("Answer is boolean (logical)")
        else:
            verification_result['confidence'] = 0.5
            verification_result['checks'].append("Answer type is non-standard")
        
        question_type = plan.get('type', '')
        if question_type == 'arithmetic' and len(solution.get('steps', [])) > 0:
            verification_result['confidence'] = min(1.0, verification_result['confidence'] + 0.1)
        elif question_type == 'algebra' and '=' in question:
            verification_result['confidence'] = min(1.0, verification_result['confidence'] + 0.05)
        
        logger.info(f"Verification result: {verification_result['confidence']:.2f} confidence")
        
        return verification_result
    
    def cross_check(self, answer, expected_range=None):
        if expected_range:
            lower, upper = expected_range
            return lower <= answer <= upper
        return True
