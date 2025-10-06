import re
import sympy as sp
import numpy as np
from sympy.parsing.sympy_parser import parse_expr
from src.log_utils import setup_logger

logger = setup_logger()

class MathSolver:
    def __init__(self):
        self.x, self.y, self.z = sp.symbols('x y z')
        
    def solve(self, question, plan):
        question_type = plan['type']
        
        solvers = {
            'arithmetic': self.solve_arithmetic,
            'algebra': self.solve_algebra,
            'geometry': self.solve_geometry,
            'logic': self.solve_logic,
            'word_problem': self.solve_word_problem,
            'comparison': self.solve_comparison,
            'pattern': self.solve_pattern
        }
        
        solver_func = solvers.get(question_type, self.solve_generic)
        
        try:
            result = solver_func(question, plan)
            return result
        except Exception as e:
            logger.error(f"Error solving question: {e}")
            return {
                'answer': None,
                'steps': [],
                'error': str(e)
            }
    
    def solve_arithmetic(self, question, plan):
        steps = []
        numbers = re.findall(r'-?\d+\.?\d*', question)
        numbers = [float(n) for n in numbers]
        
        steps.append(f"Identified numbers: {numbers}")
        
        result = None
        if 'sum' in question.lower() or 'add' in question.lower() or '+' in question:
            result = sum(numbers)
            steps.append(f"Calculated sum: {result}")
        elif 'product' in question.lower() or 'multiply' in question.lower() or '*' in question:
            result = np.prod(numbers)
            steps.append(f"Calculated product: {result}")
        elif 'difference' in question.lower() or 'subtract' in question.lower() or '-' in question:
            result = numbers[0] - sum(numbers[1:]) if len(numbers) > 1 else numbers[0]
            steps.append(f"Calculated difference: {result}")
        elif 'quotient' in question.lower() or 'divide' in question.lower() or '/' in question:
            result = numbers[0] / numbers[1] if len(numbers) > 1 else numbers[0]
            steps.append(f"Calculated quotient: {result}")
        else:
            result = sum(numbers)
            steps.append(f"Default calculation (sum): {result}")
        
        return {'answer': result, 'steps': steps}
    
    def solve_algebra(self, question, plan):
        steps = []
        
        equation_pattern = r'([x\+\-\*/\d\s=]+)'
        matches = re.findall(equation_pattern, question)
        
        for match in matches:
            if '=' in match:
                try:
                    left, right = match.split('=')
                    equation = sp.Eq(parse_expr(left.strip()), parse_expr(right.strip()))
                    steps.append(f"Parsed equation: {equation}")
                    
                    solution = sp.solve(equation, self.x)
                    steps.append(f"Solved equation: x = {solution}")
                    
                    if solution:
                        answer = float(solution[0]) if len(solution) > 0 else None
                        return {'answer': answer, 'steps': steps}
                except Exception as e:
                    steps.append(f"Error parsing equation: {e}")
        
        numbers = re.findall(r'-?\d+\.?\d*', question)
        if numbers:
            answer = float(numbers[-1])
        else:
            answer = None
        
        return {'answer': answer, 'steps': steps}
    
    def solve_geometry(self, question, plan):
        steps = []
        numbers = re.findall(r'-?\d+\.?\d*', question)
        numbers = [float(n) for n in numbers]
        
        steps.append(f"Extracted dimensions: {numbers}")
        
        result = None
        if 'area' in question.lower():
            if 'circle' in question.lower() and len(numbers) >= 1:
                radius = numbers[0]
                result = float(sp.pi * radius**2)
                steps.append(f"Circle area = π * r² = {result}")
            elif 'rectangle' in question.lower() and len(numbers) >= 2:
                result = numbers[0] * numbers[1]
                steps.append(f"Rectangle area = length * width = {result}")
            elif 'triangle' in question.lower() and len(numbers) >= 2:
                result = 0.5 * numbers[0] * numbers[1]
                steps.append(f"Triangle area = 0.5 * base * height = {result}")
        elif 'perimeter' in question.lower():
            if 'square' in question.lower() and len(numbers) >= 1:
                result = 4 * numbers[0]
                steps.append(f"Square perimeter = 4 * side = {result}")
            elif 'rectangle' in question.lower() and len(numbers) >= 2:
                result = 2 * (numbers[0] + numbers[1])
                steps.append(f"Rectangle perimeter = 2 * (length + width) = {result}")
        elif 'volume' in question.lower():
            if 'cube' in question.lower() and len(numbers) >= 1:
                result = numbers[0]**3
                steps.append(f"Cube volume = side³ = {result}")
            elif len(numbers) >= 3:
                result = numbers[0] * numbers[1] * numbers[2]
                steps.append(f"Volume = length * width * height = {result}")
        
        return {'answer': result, 'steps': steps}
    
    def solve_logic(self, question, plan):
        steps = []
        
        if 'true' in question.lower() and 'false' in question.lower():
            if 'and' in question.lower():
                result = False
                steps.append("Logical AND with False = False")
            elif 'or' in question.lower():
                result = True
                steps.append("Logical OR with True = True")
            else:
                result = True
        elif 'not' in question.lower():
            if 'true' in question.lower():
                result = False
                steps.append("NOT True = False")
            else:
                result = True
                steps.append("NOT False = True")
        else:
            result = True
        
        return {'answer': result, 'steps': steps}
    
    def solve_word_problem(self, question, plan):
        steps = []
        numbers = re.findall(r'-?\d+\.?\d*', question)
        numbers = [float(n) for n in numbers]
        
        steps.append(f"Extracted numbers: {numbers}")
        
        result = None
        if any(word in question.lower() for word in ['total', 'sum', 'altogether']):
            result = sum(numbers)
            steps.append(f"Calculated total: {result}")
        elif any(word in question.lower() for word in ['left', 'remaining', 'difference']):
            result = numbers[0] - sum(numbers[1:]) if len(numbers) > 1 else numbers[0]
            steps.append(f"Calculated remaining: {result}")
        elif any(word in question.lower() for word in ['each', 'per', 'rate']):
            result = numbers[0] * numbers[1] if len(numbers) >= 2 else numbers[0]
            steps.append(f"Calculated total: {result}")
        else:
            result = sum(numbers)
            steps.append(f"Default calculation: {result}")
        
        return {'answer': result, 'steps': steps}
    
    def solve_comparison(self, question, plan):
        steps = []
        numbers = re.findall(r'-?\d+\.?\d*', question)
        numbers = [float(n) for n in numbers]
        
        steps.append(f"Extracted values: {numbers}")
        
        if 'greater' in question.lower() or 'larger' in question.lower() or 'more' in question.lower():
            result = max(numbers) if numbers else None
            steps.append(f"Maximum value: {result}")
        elif 'less' in question.lower() or 'smaller' in question.lower() or 'fewer' in question.lower():
            result = min(numbers) if numbers else None
            steps.append(f"Minimum value: {result}")
        elif 'equal' in question.lower():
            result = all(n == numbers[0] for n in numbers) if numbers else None
            steps.append(f"All equal: {result}")
        else:
            result = max(numbers) if numbers else None
        
        return {'answer': result, 'steps': steps}
    
    def solve_pattern(self, question, plan):
        steps = []
        numbers = re.findall(r'-?\d+\.?\d*', question)
        numbers = [float(n) for n in numbers]
        
        steps.append(f"Identified sequence: {numbers}")
        
        if len(numbers) < 2:
            return {'answer': None, 'steps': steps}
        
        differences = [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]
        steps.append(f"Calculated differences: {differences}")
        
        if len(set(differences)) == 1:
            common_diff = differences[0]
            next_value = numbers[-1] + common_diff
            steps.append(f"Arithmetic sequence with difference {common_diff}")
            steps.append(f"Next value: {next_value}")
            return {'answer': next_value, 'steps': steps}
        
        if len(numbers) >= 2:
            ratios = [numbers[i+1] / numbers[i] for i in range(len(numbers)-1) if numbers[i] != 0]
            if ratios and len(set(ratios)) == 1:
                common_ratio = ratios[0]
                next_value = numbers[-1] * common_ratio
                steps.append(f"Geometric sequence with ratio {common_ratio}")
                steps.append(f"Next value: {next_value}")
                return {'answer': next_value, 'steps': steps}
        
        next_value = numbers[-1] + differences[-1]
        steps.append(f"Predicted next value: {next_value}")
        
        return {'answer': next_value, 'steps': steps}
    
    def solve_generic(self, question, plan):
        steps = []
        numbers = re.findall(r'-?\d+\.?\d*', question)
        numbers = [float(n) for n in numbers]
        
        if numbers:
            result = sum(numbers)
            steps.append(f"Generic solve: sum of numbers = {result}")
        else:
            result = None
            steps.append("No numeric solution found")
        
        return {'answer': result, 'steps': steps}
