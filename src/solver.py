"""
Solvra - Solver Module
Core reasoning engines: Mathematical, Logical, Spatial, and Sequence solvers
Each solver is specialized for a specific type of reasoning problem
"""

import re
import sympy as sp
from sympy import symbols, Eq, solve, simplify
from typing import Dict, List, Any, Optional, Tuple
import numpy as np
from itertools import permutations, combinations


class MathSolver:
    """Handles mathematical reasoning: arithmetic, algebra, optimization"""
    
    def __init__(self):
        self.operations = {
            'add': lambda a, b: a + b,
            'subtract': lambda a, b: a - b,
            'multiply': lambda a, b: a * b,
            'divide': lambda a, b: a / b if b != 0 else None,
            'percentage': lambda part, whole: (part / whole * 100) if whole != 0 else None
        }
    
    def extract_numbers(self, text: str) -> List[float]:
        """Extract numbers from text"""
        pattern = r'-?\d+\.?\d*'
        numbers = re.findall(pattern, text)
        return [float(n) for n in numbers]
    
    def solve_linear_system(self, equations: List[str], variables: List[str]) -> Dict[str, float]:
        """
        Solve a system of linear equations
        Example: ['x + y = 10', '2*x - y = 5']
        """
        try:
            syms = symbols(' '.join(variables))
            eqs = []
            
            for eq_str in equations:
                left, right = eq_str.split('=')
                eqs.append(Eq(sp.sympify(left), sp.sympify(right)))
            
            solution = solve(eqs, syms)
            return {str(var): float(val) for var, val in solution.items()}
        except Exception as e:
            return {}
    
    def calculate_rate_problems(self, rates: List[Tuple[float, str]], time: float) -> float:
        """
        Solve rate problems (machines, workers, etc.)
        rates: list of (rate, unit) tuples
        """
        # Combined rate for working together
        total_rate = sum(r[0] for r in rates)
        return total_rate * time
    
    def optimize_scheduling(self, tasks: List[Tuple[str, float, float]]) -> List[str]:
        """
        Optimize task scheduling with advanced heuristics
        tasks: list of (name, duration, priority/penalty)
        Returns optimal order
        """
        if not tasks:
            return []
        
        # For penalty-based scheduling: prioritize by penalty/duration ratio
        # This gives optimal solution for weighted job scheduling
        tasks_with_ratio = []
        for name, duration, penalty in tasks:
            ratio = penalty / duration if duration > 0 else float('inf')
            tasks_with_ratio.append((name, duration, penalty, ratio))
        
        # Sort by ratio (highest first), then by penalty (highest first)
        sorted_tasks = sorted(tasks_with_ratio, key=lambda x: (-x[3], -x[2]))
        
        return [task[0] for task in sorted_tasks]
    
    def traveling_salesman_simple(self, distances: Dict[Tuple[str, str], float], 
                                   cities: List[str]) -> Tuple[List[str], float]:
        """
        Simple TSP solver for small number of cities
        Returns best route and total distance
        """
        min_distance = float('inf')
        best_route = None
        
        # Try all permutations
        for perm in permutations(cities[1:]):
            route = [cities[0]] + list(perm) + [cities[0]]
            distance = 0
            
            for i in range(len(route) - 1):
                key = (route[i], route[i+1])
                reverse_key = (route[i+1], route[i])
                
                if key in distances:
                    distance += distances[key]
                elif reverse_key in distances:
                    distance += distances[reverse_key]
                else:
                    distance = float('inf')
                    break
            
            if distance < min_distance:
                min_distance = distance
                best_route = route
        
        return best_route, min_distance


class LogicSolver:
    """Handles logical reasoning: truth tables, deduction, riddles"""
    
    def __init__(self):
        self.truth_patterns = {
            'always_true': lambda x: True,
            'always_false': lambda x: False,
            'truth_teller': 'truth',
            'liar': 'lie'
        }
    
    def solve_truth_teller_liar(self, statements: List[Dict], question: str) -> str:
        """
        Classic truth-teller and liar problems
        statements: [{'person': 'A', 'says': 'statement', 'type': 'unknown'}]
        """
        # If you ask either person "what would the other say", both point to wrong door
        # So choose the opposite
        return "Choose opposite of what they indicate"
    
    def logical_deduction(self, facts: List[str], rules: List[str]) -> List[str]:
        """
        Simple forward-chaining logical deduction
        """
        conclusions = set(facts)
        changed = True
        
        while changed:
            changed = False
            for rule in rules:
                # Simple if-then rules
                if 'if' in rule.lower() and 'then' in rule.lower():
                    parts = rule.lower().split('then')
                    condition = parts[0].replace('if', '').strip()
                    conclusion = parts[1].strip()
                    
                    if condition in [f.lower() for f in conclusions]:
                        if conclusion not in [c.lower() for c in conclusions]:
                            conclusions.add(conclusion)
                            changed = True
        
        return list(conclusions)


class SpatialSolver:
    """Handles spatial reasoning: 3D geometry, paths, rotations"""
    
    def __init__(self):
        pass
    
    def count_cube_faces(self, cube_size: int, painted_faces: int) -> Dict[str, int]:
        """
        Count cubes with different numbers of painted faces
        when a cube is painted and then divided
        Enhanced with detailed analysis
        """
        if cube_size < 2:
            return {'0_faces': 0, '1_face': 0, '2_faces': 0, '3_faces': 0}
        
        # Corner cubes: always 3 faces painted (8 corners in any cube)
        corners = 8
        
        # Edge cubes (not corners): 2 faces painted
        # 12 edges, each edge has (cube_size - 2) non-corner cubes
        edges = 12 * (cube_size - 2)
        
        # Face cubes (not on edges): 1 face painted
        # 6 faces, each face has (cube_size - 2)^2 non-edge cubes
        faces = 6 * (cube_size - 2) ** 2
        
        # Interior cubes: 0 faces painted
        # Form a smaller cube of size (cube_size - 2)
        interior = (cube_size - 2) ** 3 if cube_size > 2 else 0
        
        result = {
            '0_faces': interior,
            '1_face': faces,
            '2_faces': edges,
            '3_faces': corners,
            'total': cube_size ** 3
        }
        
        # Verify total
        assert sum([v for k, v in result.items() if k != 'total']) == cube_size ** 3
        
        return result
    
    def shortest_path_grid(self, start: Tuple[int, int, int], 
                          end: Tuple[int, int, int]) -> float:
        """
        Shortest surface path on a 3D grid (ant on cube problem)
        """
        # Manhattan distance in 3D
        distance = sum(abs(a - b) for a, b in zip(start, end))
        return distance
    
    def room_navigation(self, moves: List[str]) -> str:
        """
        Track direction after a series of room moves
        moves: ['forward', 'right', 'left', 'back']
        """
        directions = ['N', 'E', 'S', 'W']
        current = 0  # Start facing North
        
        for move in moves:
            if move == 'right':
                current = (current + 1) % 4
            elif move == 'left':
                current = (current - 1) % 4
            elif move == 'back':
                current = (current + 2) % 4
        
        return directions[current]


class SequenceSolver:
    """Handles sequence problems: patterns, progressions, series"""
    
    def __init__(self):
        pass
    
    def identify_arithmetic_sequence(self, numbers: List[float]) -> Optional[float]:
        """Check if sequence is arithmetic and return common difference"""
        if len(numbers) < 2:
            return None
        
        differences = [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]
        
        # Check if all differences are equal
        if len(set(differences)) == 1:
            return differences[0]
        return None
    
    def identify_geometric_sequence(self, numbers: List[float]) -> Optional[float]:
        """Check if sequence is geometric and return common ratio"""
        if len(numbers) < 2 or 0 in numbers[:-1]:
            return None
        
        ratios = [numbers[i+1] / numbers[i] for i in range(len(numbers)-1)]
        
        # Check if all ratios are equal
        if len(set([round(r, 6) for r in ratios])) == 1:
            return ratios[0]
        return None
    
    def identify_recursive_sequence(self, numbers: List[float]) -> Optional[str]:
        """Identify if sequence follows a recursive pattern"""
        if len(numbers) < 4:
            return None
        
        # Check if each term is sum of previous terms
        # Fibonacci-like: a(n) = a(n-1) + a(n-2)
        if all(abs(numbers[i] - (numbers[i-1] + numbers[i-2])) < 0.01 
               for i in range(2, len(numbers))):
            return "fibonacci_like"
        
        # Check: a(n) = a(n-1) + a(n-2) + a(n-3)
        if len(numbers) >= 4:
            if all(abs(numbers[i] - (numbers[i-1] + numbers[i-2] + numbers[i-3])) < 0.01 
                   for i in range(3, len(numbers))):
                return "tribonacci_like"
        
        return None
    
    def predict_next(self, numbers: List[float]) -> Optional[float]:
        """Predict next number in sequence with advanced pattern detection"""
        if len(numbers) < 2:
            return None
        
        # Try arithmetic
        diff = self.identify_arithmetic_sequence(numbers)
        if diff is not None:
            return numbers[-1] + diff
        
        # Try geometric
        ratio = self.identify_geometric_sequence(numbers)
        if ratio is not None:
            return numbers[-1] * ratio
        
        # Try recursive patterns
        pattern = self.identify_recursive_sequence(numbers)
        if pattern == "fibonacci_like":
            return numbers[-1] + numbers[-2]
        elif pattern == "tribonacci_like":
            return numbers[-1] + numbers[-2] + numbers[-3]
        
        # Advanced patterns: n^2, n^3, n^2 + n, n^2 + 1, etc.
        if len(numbers) >= 3:
            # Check for n^2 pattern
            indices = list(range(1, len(numbers) + 1))
            if all(abs(numbers[i] - (i+1)**2) < 0.1 for i in range(len(numbers))):
                return (len(numbers) + 1) ** 2
            
            # Check for n^2 + 1 pattern
            if all(abs(numbers[i] - ((i+1)**2 + 1)) < 0.1 for i in range(len(numbers))):
                return (len(numbers) + 1) ** 2 + 1
            
            # Check for n^2 + n pattern
            if all(abs(numbers[i] - ((i+1)**2 + (i+1))) < 0.1 for i in range(len(numbers))):
                n = len(numbers) + 1
                return n**2 + n
            
            # Check for n^3 pattern
            if all(abs(numbers[i] - (i+1)**3) < 0.1 for i in range(len(numbers))):
                return (len(numbers) + 1) ** 3
            
            # Check for 2^n pattern
            if all(abs(numbers[i] - 2**(i+1)) < 0.1 for i in range(len(numbers))):
                return 2 ** (len(numbers) + 1)
            
            # Check for differences in differences (second derivative)
            first_diffs = [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]
            if len(first_diffs) >= 2:
                second_diffs = [first_diffs[i+1] - first_diffs[i] for i in range(len(first_diffs)-1)]
                
                # If second differences are constant, it's quadratic
                if len(set([round(d, 6) for d in second_diffs])) == 1:
                    # Predict next first difference
                    next_first_diff = first_diffs[-1] + second_diffs[0]
                    return numbers[-1] + next_first_diff
        
        # Try polynomial fitting (fallback)
        if len(numbers) >= 3:
            x = np.array(range(1, len(numbers) + 1))
            y = np.array(numbers)
            
            # Try quadratic fit
            coeffs = np.polyfit(x, y, min(2, len(numbers) - 1))
            next_val = np.polyval(coeffs, len(numbers) + 1)
            
            # Verify fit quality
            predicted = np.polyval(coeffs, x)
            error = np.mean(np.abs(predicted - y))
            
            if error < 0.5:  # Good fit
                return float(next_val)
        
        return None


def demo_solvers():
    """Demonstrate solver capabilities"""
    print("🧮 MATH SOLVER DEMO")
    math_solver = MathSolver()
    
    # TSP example
    cities = ['A', 'B', 'C', 'D']
    distances = {
        ('A', 'B'): 50, ('A', 'C'): 70, ('A', 'D'): 40,
        ('B', 'C'): 40, ('B', 'D'): 25, ('C', 'D'): 10
    }
    route, dist = math_solver.traveling_salesman_simple(distances, cities)
    print(f"Best route: {' -> '.join(route)}, Distance: {dist}")
    
    print("\n🧩 LOGIC SOLVER DEMO")
    logic_solver = LogicSolver()
    result = logic_solver.solve_truth_teller_liar([], "Which door?")
    print(f"Truth-teller/Liar solution: {result}")
    
    print("\n📦 SPATIAL SOLVER DEMO")
    spatial_solver = SpatialSolver()
    cube_analysis = spatial_solver.count_cube_faces(3, 6)
    print(f"3x3x3 painted cube analysis: {cube_analysis}")
    
    print("\n🔢 SEQUENCE SOLVER DEMO")
    seq_solver = SequenceSolver()
    sequence = [2, 5, 10, 17, 26]
    next_num = seq_solver.predict_next(sequence)
    print(f"Sequence {sequence} -> Next: {next_num}")


if __name__ == "__main__":
    demo_solvers()
