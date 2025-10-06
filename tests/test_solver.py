import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.solver import MathSolver

def test_solver_initialization():
    solver = MathSolver()
    assert solver is not None

def test_solver_arithmetic():
    solver = MathSolver()
    
    question = "What is 10 plus 5?"
    plan = {'type': 'arithmetic', 'steps': []}
    
    result = solver.solve(question, plan)
    
    assert result is not None
    assert 'answer' in result
    assert 'steps' in result
    assert isinstance(result['answer'], (int, float, bool)) or result['answer'] is None

def test_solver_returns_numeric():
    solver = MathSolver()
    
    question = "Calculate 7 times 8"
    plan = {'type': 'arithmetic', 'steps': []}
    
    result = solver.solve(question, plan)
    
    assert result['answer'] is not None
    assert isinstance(result['answer'], (int, float))

def test_solver_algebra():
    solver = MathSolver()
    
    question = "Solve x + 5 = 10"
    plan = {'type': 'algebra', 'steps': []}
    
    result = solver.solve(question, plan)
    
    assert result is not None
    assert 'answer' in result

def test_solver_geometry():
    solver = MathSolver()
    
    question = "What is the area of a rectangle with length 5 and width 3?"
    plan = {'type': 'geometry', 'steps': []}
    
    result = solver.solve(question, plan)
    
    assert result is not None
    assert result['answer'] is not None
