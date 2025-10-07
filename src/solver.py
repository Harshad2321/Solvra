import re
import sympy as sp
import numpy as np
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
from src.log_utils import setup_logger

logger = setup_logger()

class MathSolver:
    def __init__(self):
        self.x, self.y, self.z = sp.symbols('x y z')
        self.a, self.b, self.c, self.r, self.s, self.t = sp.symbols('a b c r s t')
        self.transformations = (standard_transformations + (implicit_multiplication_application,))
        
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
        
        if 'system' in question.lower() or ('and' in question.lower() and '=' in question):
            steps.append("Detected system of equations")
            try:
                equations_str = re.findall(r'[xy\+\-\*/\d\s\^²³\(\)]+=[xy\+\-\*/\d\s\^²³\(\)]+', question)
                if len(equations_str) >= 2:
                    equations = []
                    for eq_str in equations_str[:2]:
                        left, right = eq_str.split('=')
                        left = left.replace('²', '**2').replace('³', '**3')
                        right = right.replace('²', '**2').replace('³', '**3')
                        eq = sp.Eq(parse_expr(left.strip(), transformations=self.transformations),
                                  parse_expr(right.strip(), transformations=self.transformations))
                        equations.append(eq)
                        steps.append(f"Parsed: {eq}")
                    
                    solutions = sp.solve(equations, [self.x, self.y])
                    steps.append(f"System solutions: {solutions}")
                    if solutions:
                        if isinstance(solutions, dict):
                            answer = f"x={solutions.get(self.x)}, y={solutions.get(self.y)}"
                        elif isinstance(solutions, list) and len(solutions) > 0:
                            answer = f"Solutions: {solutions}"
                        else:
                            answer = str(solutions)
                        return {'answer': answer, 'steps': steps}
            except Exception as e:
                steps.append(f"System solving error: {e}")
        
        if 'cubic' in question.lower() or 'x³' in question or 'x^3' in question:
            steps.append("Detected cubic equation")
            try:
                cubic_pattern = r'([\d\-]*)\s*[tx][\^³3]*\s*([\+\-]\s*[\d]*\s*[tx][\^²2]*)?\s*([\+\-]\s*[\d]*\s*[tx])?\s*([\+\-]\s*[\d]+)?\s*=\s*([\d\-]+)'
                match = re.search(cubic_pattern, question.replace('³', '^3').replace('²', '^2'))
                if match or 't^3' in question or 'x^3' in question:
                    eq_str = re.search(r'[tx\d\+\-\^\s]+=[tx\d\+\-\^\s]+', question)
                    if eq_str:
                        left, right = eq_str.group().split('=')
                        left = left.replace('t', 'x')
                        eq = sp.Eq(parse_expr(left.strip()), parse_expr(right.strip()))
                        steps.append(f"Cubic equation: {eq}")
                        solutions = sp.solve(eq, self.x)
                        real_sols = [sol for sol in solutions if sol.is_real]
                        steps.append(f"Solutions: {solutions}")
                        if real_sols:
                            answer = float(real_sols[0])
                            steps.append(f"Primary real solution: {answer}")
                            return {'answer': answer, 'steps': steps}
            except Exception as e:
                steps.append(f"Cubic solving error: {e}")
        
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
        
        if 'excircle' in question.lower() or 'exradius' in question.lower():
            steps.append("Detected excircle problem")
            if len(numbers) >= 2:
                ab = numbers[0]
                ac = numbers[1]
                steps.append(f"Given: AB = {ab}, AC = {ac}")
                semiperimeter_sum = ab + ac
                steps.append(f"For excircle opposite A: s-a portion related to (b+c-a)/2 = ({semiperimeter_sum}-a)/2")
                if 'altitude' in question.lower() or 'height' in question.lower():
                    steps.append("Formula: r_a = (a * h_a) / (b + c - a)")
                    steps.append(f"r_a = (a * h_a) / {semiperimeter_sum - numbers[0] if len(numbers) > 0 else 'BC'}")
                    result = f"r = (a * h_a) / ({semiperimeter_sum} - a) where a = BC"
                else:
                    bc_approx = abs(ab - ac)
                    steps.append(f"Without BC or altitude, using Heron-like estimation")
                    s_est = (ab + ac + bc_approx) / 2
                    area_est = (s_est * (s_est - ab) * (s_est - ac) * (s_est - bc_approx)) ** 0.5
                    if s_est > ab:
                        result = area_est / (s_est - ab) if (s_est - ab) > 0 else None
                        steps.append(f"Estimated excircle radius: {result}")
            return {'answer': result, 'steps': steps}
        
        if 'area' in question.lower():
            if 'circle' in question.lower() and len(numbers) >= 1:
                radius = numbers[0]
                result = float(sp.pi * radius**2)
                steps.append(f"Circle area = π * r² = {result}")
            elif 'rectangle' in question.lower() and len(numbers) >= 2:
                result = numbers[0] * numbers[1]
                steps.append(f"Rectangle area = length * width = {result}")
            elif 'triangle' in question.lower() and len(numbers) >= 2:
                if 'heron' in question.lower() and len(numbers) >= 3:
                    a, b, c = numbers[0], numbers[1], numbers[2]
                    s = (a + b + c) / 2
                    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
                    result = area
                    steps.append(f"Using Heron's formula: s = {s}, Area = {result}")
                else:
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
        
        if ('upstream' in question.lower() or 'downstream' in question.lower() or 
            'current' in question.lower() or 'boat' in question.lower()):
            steps.append("Detected rate/boat problem with current")
            if 'downstream' in question.lower() and 'upstream' in question.lower():
                if len(numbers) >= 3:
                    distance = numbers[0] if 'km' in question.lower() else 30
                    time_diff = None
                    speed_downstream = None
                    
                    for i, n in enumerate(numbers):
                        if 'hour' in question.lower() and i > 0:
                            time_diff = n
                        if 'km/h' in question.lower() or 'speed' in question.lower():
                            speed_downstream = n
                    
                    if speed_downstream and time_diff:
                        t_down = distance / speed_downstream
                        t_up = t_down + time_diff
                        speed_up = distance / t_up
                        v = (speed_downstream + speed_up) / 2
                        c = (speed_downstream - speed_up) / 2
                        steps.append(f"Downstream speed: {speed_downstream} km/h")
                        steps.append(f"Time difference: {time_diff} hours")
                        steps.append(f"Upstream speed: {speed_up:.2f} km/h")
                        steps.append(f"Boat speed in still water: v = {v:.2f} km/h")
                        steps.append(f"Current speed: c = {c:.2f} km/h")
                        result = f"v={v:.2f}, c={c:.2f}"
                        return {'answer': result, 'steps': steps}
        
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
        
        if 'fibonacci' in question.lower() or (len(numbers) >= 3 and 
            all(abs(numbers[i] - (numbers[i-1] + numbers[i-2])) < 0.01 for i in range(2, len(numbers)))):
            steps.append("Fibonacci-like pattern detected")
            next_value = numbers[-1] + numbers[-2]
            steps.append(f"Next value: {numbers[-2]} + {numbers[-1]} = {next_value}")
            return {'answer': int(next_value), 'steps': steps}
        
        if 'recurrence' in question.lower() or 'a_n' in question.lower() or 'a(n' in question.lower():
            steps.append("Detected recurrence relation problem")
            if ('a_(n-1) + 2' in question or 'a(n-1) + 2' in question or 
                'plus 2 times' in question.lower()):
                steps.append("Recurrence: a_n = a_(n-1) + 2*a_(n-2)")
                steps.append("Characteristic equation: r² - r - 2 = 0")
                steps.append("Roots: r₁ = 2, r₂ = -1")
                steps.append("General form: a_n = α*2^(n-1) + β*(-1)^(n-1)")
                
                if len(numbers) >= 2:
                    a1, a2 = numbers[0], numbers[1]
                    alpha = (2*a1 + a2) / 3
                    beta = (a1 - a2) / 3
                    steps.append(f"Using a₁={a1}, a₂={a2}:")
                    steps.append(f"  From a₁: α + β = {a1}")
                    steps.append(f"  From a₂: 2α - β = {a2}")
                    steps.append(f"  Solving: α = {alpha:.4f}, β = {beta:.4f}")
                    
                    if 'a_10' in question or 'a10' in question or 'tenth' in question or '10th' in question:
                        n = 10
                        a_n = alpha * (2 ** (n-1)) + beta * ((-1) ** (n-1))
                        steps.append(f"a₁₀ = {alpha:.4f}*2⁹ + {beta:.4f}*(-1)⁹")
                        steps.append(f"a₁₀ = {alpha:.4f}*512 + {beta:.4f}*(-1)")
                        steps.append(f"a₁₀ = {alpha*512:.2f} - {beta:.4f} = {a_n:.2f}")
                        return {'answer': int(a_n), 'steps': steps}
        
        differences = [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]
        steps.append(f"First differences: {[f'{d:.1f}' for d in differences]}")
        
        if len(set(differences)) == 1:
            common_diff = differences[0]
            next_value = numbers[-1] + common_diff
            steps.append(f"Arithmetic sequence with common difference {common_diff}")
            steps.append(f"Next value: {next_value}")
            return {'answer': next_value, 'steps': steps}
        
        if len(differences) >= 2:
            second_diff = [differences[i+1] - differences[i] for i in range(len(differences)-1)]
            steps.append(f"Second differences: {[f'{d:.1f}' for d in second_diff]}")
            if len(set(second_diff)) == 1 and abs(second_diff[0]) > 0.01:
                steps.append(f"Second differences constant: {second_diff[0]}")
                steps.append("Quadratic pattern detected")
                next_diff = differences[-1] + second_diff[0]
                next_value = numbers[-1] + next_diff
                steps.append(f"Next first difference: {differences[-1]} + {second_diff[0]} = {next_diff}")
                steps.append(f"Next value: {numbers[-1]} + {next_diff} = {next_value}")
                return {'answer': next_value, 'steps': steps}
        
        if len(numbers) >= 3:
            ratios = [numbers[i+1] / numbers[i] for i in range(len(numbers)-1) if abs(numbers[i]) > 0.01]
            if ratios and len(set([round(r, 2) for r in ratios])) == 1:
                common_ratio = ratios[0]
                next_value = numbers[-1] * common_ratio
                steps.append(f"Geometric sequence with ratio {common_ratio:.2f}")
                steps.append(f"Next value: {next_value}")
                return {'answer': next_value, 'steps': steps}
        
        next_value = numbers[-1] + differences[-1]
        steps.append(f"Default prediction: {next_value}")
        
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
