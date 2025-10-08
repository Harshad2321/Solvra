"""
Solvra - Advanced Pattern Matching Module
Specialized algorithms for complex pattern recognition
"""

import re
from typing import List, Dict, Any, Optional, Tuple
import numpy as np


class AdvancedPatternMatcher:
    """
    Advanced pattern matching for high-accuracy problem solving
    """
    
    def __init__(self):
        self.known_patterns = {}
    
    def extract_all_numbers(self, text: str) -> List[float]:
        """Extract all numbers including fractions and decimals"""
        # Match integers, decimals, and fractions
        pattern = r'-?\d+\.?\d*(?:/\d+)?'
        matches = re.findall(pattern, text)
        
        numbers = []
        for match in matches:
            if '/' in match:
                parts = match.split('/')
                numbers.append(float(parts[0]) / float(parts[1]))
            else:
                numbers.append(float(match))
        
        return numbers
    
    def detect_sequence_type(self, numbers: List[float]) -> Dict[str, Any]:
        """
        Comprehensive sequence type detection
        Returns type and parameters
        """
        if len(numbers) < 3:
            return {'type': 'unknown'}
        
        # Test arithmetic
        diffs = [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]
        if len(set([round(d, 6) for d in diffs])) == 1:
            return {'type': 'arithmetic', 'difference': diffs[0]}
        
        # Test geometric
        if all(n != 0 for n in numbers[:-1]):
            ratios = [numbers[i+1] / numbers[i] for i in range(len(numbers)-1)]
            if len(set([round(r, 6) for r in ratios])) == 1:
                return {'type': 'geometric', 'ratio': ratios[0]}
        
        # Test quadratic (n^2 + c)
        indices = list(range(1, len(numbers) + 1))
        for c in range(-10, 11):
            if all(abs(numbers[i] - ((i+1)**2 + c)) < 0.1 for i in range(len(numbers))):
                return {'type': 'quadratic', 'formula': f'n^2 + {c}', 'constant': c}
        
        # Test n^2 + n
        if all(abs(numbers[i] - ((i+1)**2 + (i+1))) < 0.1 for i in range(len(numbers))):
            return {'type': 'quadratic', 'formula': 'n^2 + n'}
        
        # Test cubic
        if all(abs(numbers[i] - (i+1)**3) < 0.1 for i in range(len(numbers))):
            return {'type': 'cubic', 'formula': 'n^3'}
        
        # Test fibonacci-like
        if all(abs(numbers[i] - (numbers[i-1] + numbers[i-2])) < 0.1 
               for i in range(2, len(numbers))):
            return {'type': 'fibonacci'}
        
        # Test exponential (2^n, 3^n, etc.)
        for base in [2, 3, 4, 5]:
            if all(abs(numbers[i] - base**(i+1)) < 0.1 for i in range(len(numbers))):
                return {'type': 'exponential', 'base': base}
        
        # Test second-order differences (quadratic)
        if len(numbers) >= 4:
            second_diffs = [diffs[i+1] - diffs[i] for i in range(len(diffs)-1)]
            if len(set([round(d, 6) for d in second_diffs])) == 1:
                return {'type': 'quadratic_sequence', 'second_difference': second_diffs[0]}
        
        # Test alternating patterns
        if len(numbers) >= 4:
            odd_vals = [numbers[i] for i in range(0, len(numbers), 2)]
            even_vals = [numbers[i] for i in range(1, len(numbers), 2)]
            
            # Check if odd and even positions form separate patterns
            if len(odd_vals) >= 2:
                odd_diffs = [odd_vals[i+1] - odd_vals[i] for i in range(len(odd_vals)-1)]
                if len(set([round(d, 6) for d in odd_diffs])) == 1:
                    return {'type': 'alternating', 'odd_diff': odd_diffs[0] if odd_diffs else 0}
        
        return {'type': 'unknown'}
    
    def predict_next_value(self, numbers: List[float], pattern_info: Dict[str, Any]) -> Optional[float]:
        """Predict next value based on detected pattern"""
        if not numbers:
            return None
        
        pattern_type = pattern_info.get('type')
        
        if pattern_type == 'arithmetic':
            return numbers[-1] + pattern_info['difference']
        
        elif pattern_type == 'geometric':
            return numbers[-1] * pattern_info['ratio']
        
        elif pattern_type == 'quadratic':
            formula = pattern_info.get('formula', '')
            if 'n^2 +' in formula:
                c = pattern_info.get('constant', 0)
                n = len(numbers) + 1
                return n**2 + c
            elif formula == 'n^2 + n':
                n = len(numbers) + 1
                return n**2 + n
        
        elif pattern_type == 'cubic':
            n = len(numbers) + 1
            return n**3
        
        elif pattern_type == 'fibonacci':
            return numbers[-1] + numbers[-2]
        
        elif pattern_type == 'exponential':
            base = pattern_info['base']
            return base ** (len(numbers) + 1)
        
        elif pattern_type == 'quadratic_sequence':
            # Use second difference to predict
            first_diffs = [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]
            next_first_diff = first_diffs[-1] + pattern_info['second_difference']
            return numbers[-1] + next_first_diff
        
        return None
    
    def analyze_problem_keywords(self, text: str) -> Dict[str, bool]:
        """
        Extract key indicators from problem text
        """
        text_lower = text.lower()
        
        return {
            'requires_optimization': any(kw in text_lower for kw in ['minimum', 'maximum', 'optimal', 'shortest', 'longest', 'least', 'most', 'best']),
            'requires_spatial': any(kw in text_lower for kw in ['cube', 'room', 'direction', 'corner', 'face', 'edge', 'rotate', 'flip']),
            'requires_logic': any(kw in text_lower for kw in ['truth', 'liar', 'riddle', 'logic', 'deduce', 'if', 'then', 'therefore']),
            'requires_sequence': any(kw in text_lower for kw in ['sequence', 'pattern', 'next', 'series', 'progression']),
            'is_impossible': any(kw in text_lower for kw in ['impossible', 'cannot', 'no way', 'no solution', 'logical trap']),
            'requires_counting': any(kw in text_lower for kw in ['how many', 'count', 'number of']),
            'requires_scheduling': any(kw in text_lower for kw in ['schedule', 'order', 'sequence', 'tasks', 'deadline']),
            'has_time_constraint': any(kw in text_lower for kw in ['hour', 'minute', 'second', 'day', 'week', 'time']),
        }
    
    def extract_constraints(self, text: str) -> List[str]:
        """Extract constraints from problem description"""
        constraints = []
        
        # Look for "must", "cannot", "only", "at least", "at most"
        constraint_patterns = [
            r'must\s+([^.;]+)',
            r'cannot\s+([^.;]+)',
            r'only\s+([^.;]+)',
            r'at least\s+([^.;]+)',
            r'at most\s+([^.;]+)',
            r'should\s+([^.;]+)',
        ]
        
        for pattern in constraint_patterns:
            matches = re.findall(pattern, text.lower())
            constraints.extend(matches)
        
        return constraints
    
    def match_answer_to_pattern(self, predicted_value: Any, options: List[str]) -> Optional[int]:
        """
        Match predicted value to answer options with fuzzy matching
        """
        if predicted_value is None:
            return None
        
        for i, option in enumerate(options):
            if not option:
                continue
            
            # Skip "Another answer"
            if 'another answer' in option.lower():
                continue
            
            # Extract numbers from option
            option_nums = self.extract_all_numbers(option)
            
            if isinstance(predicted_value, (int, float)):
                for opt_num in option_nums:
                    if abs(opt_num - predicted_value) < 0.5:
                        return i + 1
            
            # String matching
            if isinstance(predicted_value, str):
                if predicted_value.lower() in option.lower():
                    return i + 1
        
        return None
    
    def calculate_confidence(self, pattern_info: Dict[str, Any], prediction: Any) -> float:
        """
        Calculate confidence score for prediction (0-1)
        """
        if pattern_info.get('type') == 'unknown':
            return 0.3
        
        known_types = ['arithmetic', 'geometric', 'quadratic', 'cubic', 'fibonacci', 'exponential']
        if pattern_info.get('type') in known_types:
            return 0.95
        
        if pattern_info.get('type') == 'quadratic_sequence':
            return 0.85
        
        return 0.5


def test_pattern_matcher():
    """Test the pattern matcher"""
    matcher = AdvancedPatternMatcher()
    
    # Test sequences
    test_cases = [
        [2, 5, 10, 17, 26],  # n^2 + 1
        [1, 4, 9, 16, 25],   # n^2
        [1, 8, 27, 64],      # n^3
        [2, 4, 8, 16, 32],   # 2^n
        [1, 1, 2, 3, 5, 8],  # Fibonacci
    ]
    
    for seq in test_cases:
        pattern = matcher.detect_sequence_type(seq)
        prediction = matcher.predict_next_value(seq, pattern)
        confidence = matcher.calculate_confidence(pattern, prediction)
        print(f"Sequence: {seq}")
        print(f"Pattern: {pattern}")
        print(f"Next: {prediction} (confidence: {confidence:.2f})")
        print()


if __name__ == "__main__":
    test_pattern_matcher()
