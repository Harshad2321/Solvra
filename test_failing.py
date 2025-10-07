"""
Detailed test of the two failing problems
"""

from src.pipeline import SolvraPipeline
from src.solver import MathSolver

def test_logic_puzzle():
    print("=" * 80)
    print("TEST: Logic Puzzle (Knights/Knaves)")
    print("=" * 80)
    
    question = """On an island of knights (always truth) and knaves (always lie) three people say:
P: "Exactly one of us is a knight."
Q: "P is a knave."
R: "Q is a knave."
Determine the types (knight/knave) of P,Q,R."""
    
    # Test direct solver
    solver = MathSolver()
    plan = {'type': 'logic'}
    
    print("\nDirect solver test:")
    try:
        result = solver.solve(question, plan)
        print(f"Answer: {result['answer']}")
        print(f"Steps: {result['steps']}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

def test_constrained_opt():
    print("\n" + "=" * 80)
    print("TEST: Constrained Optimization")
    print("=" * 80)
    
    question = "Find the maximum value of f(x,y) = x^2*y subject to x^2 + 2*y^2 = 8 with real x, y."
    
    # Test direct solver
    solver = MathSolver()
    plan = {'type': 'comparison'}  # Should route to comparison
    
    print("\nDirect solver test with comparison type:")
    try:
        result = solver.solve(question, plan)
        print(f"Answer: {result['answer']}")
        print(f"Steps:")
        for step in result['steps']:
            print(f"  - {step}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_logic_puzzle()
    test_constrained_opt()
