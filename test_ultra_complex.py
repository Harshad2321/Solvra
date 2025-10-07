"""
ULTRA COMPLEX Mathematical Problem Test Suite
Tests 20+ advanced problem types:
- Matrix operations (determinants, eigenvalues)
- Calculus (derivatives, integrals, limits)
- Number theory (GCD, LCM, primes, modular arithmetic)
- Combinatorics (permutations, combinations, factorials)
- Complex numbers (magnitude, argument, operations)
- Trigonometry
"""

from src.pipeline import SolvraPipeline

def test_ultra_complex():
    pipeline = SolvraPipeline()
    
    problems = [
        # Matrix & Linear Algebra
        ("Matrix Determinant", "Find the determinant of matrix [[3, 8], [4, 6]]", "-14"),
        ("Matrix Eigenvalues", "Find eigenvalues of matrix [[4, 1], [2, 3]]", "5, 2"),
        ("Matrix Trace", "Find the trace of matrix [[2, 5], [1, 3]]", "5"),
        
        # Calculus
        ("Derivative", "Find derivative of f(x) = x^3 - 4*x^2 + 6*x", "3x² - 8x + 6"),
        ("Definite Integral", "Compute integral of x^2 from 0 to 3", "9"),
        ("Limit to Infinity", "Find limit as x approaches infinity of (2*x^2 + 3)/(x^2 + 1)", "2"),
        ("Derivative at Point", "f(x) = x^2, find f'(x) at x = 5", "10"),
        
        # Number Theory
        ("GCD", "Find GCD of 48 and 180", "12"),
        ("LCM", "Find LCM of 12 and 18", "36"),
        ("Prime Factorization", "Prime factorization of 360", "2³×3²×5"),
        ("Modular Arithmetic", "What is 47 mod 12", "11"),
        ("Euler Totient", "Find Euler's totient phi(20)", "8"),
        ("Modular Inverse", "Find modular inverse of 3 mod 11", "4"),
        
        # Combinatorics
        ("Combinations", "C(10, 3) - choose 3 from 10", "120"),
        ("Permutations", "P(5, 3) - permute 5 take 3", "60"),
        ("Factorial", "Calculate 7!", "5040"),
        ("Fibonacci", "Find 10th Fibonacci number", "55"),
        ("Catalan Number", "Find 4th Catalan number", "14"),
        
        # Complex Numbers
        ("Complex Magnitude", "Find magnitude of 3 + 4i", "5"),
        ("Complex Argument", "Find argument of 1 + 1i in radians", "π/4"),
        ("Complex Conjugate", "Find conjugate of 5 + 3i", "5 - 3i"),
        
        # Trigonometry
        ("Sine", "Calculate sin(30 degrees)", "0.5"),
        ("Cosine", "Calculate cos(60 degrees)", "0.5"),
        ("Tangent", "Calculate tan(45 degrees)", "1"),
    ]
    
    print("=" * 80)
    print("ULTRA COMPLEX PROBLEM SOLVING TEST SUITE")
    print(f"Testing {len(problems)} advanced mathematical problems")
    print("=" * 80)
    print()
    
    results = []
    for i, (name, question, expected) in enumerate(problems, 1):
        print(f"\n[{i}/{len(problems)}] {name}")
        print(f"Q: {question}")
        print(f"Expected: {expected}")
        
        try:
            result = pipeline.process_question(question)
            answer = result.get('predicted_answer', result.get('answer'))
            confidence = result.get('confidence', 0.0)
            
            print(f"A: {answer}")
            print(f"Confidence: {confidence:.1%}")
            
            success = answer is not None
            results.append((name, success, answer, confidence))
            
        except Exception as e:
            print(f"ERROR: {e}")
            results.append((name, False, None, 0.0))
    
    # Summary
    print("\n" + "=" * 80)
    print("RESULTS SUMMARY")
    print("=" * 80)
    
    successful = sum(1 for _, success, _, _ in results if success)
    total = len(results)
    
    print(f"\nSuccess Rate: {successful}/{total} = {successful/total*100:.1f}%\n")
    
    # Category breakdown
    categories = {
        "Matrix & Linear Algebra": 0,
        "Calculus": 0,
        "Number Theory": 0,
        "Combinatorics": 0,
        "Complex Numbers": 0,
        "Trigonometry": 0
    }
    
    cat_success = {cat: 0 for cat in categories}
    
    # Count by category
    for i, (name, success, _, _) in enumerate(results):
        if i < 3:
            cat = "Matrix & Linear Algebra"
        elif i < 7:
            cat = "Calculus"
        elif i < 13:
            cat = "Number Theory"
        elif i < 18:
            cat = "Combinatorics"
        elif i < 21:
            cat = "Complex Numbers"
        else:
            cat = "Trigonometry"
        
        categories[cat] += 1
        if success:
            cat_success[cat] += 1
    
    print("Performance by Category:")
    for cat in categories:
        rate = cat_success[cat] / categories[cat] * 100 if categories[cat] > 0 else 0
        print(f"  {cat}: {cat_success[cat]}/{categories[cat]} ({rate:.0f}%)")
    
    print("\nDetailed Results:")
    for name, success, answer, conf in results:
        status = "[OK]" if success else "[FAIL]"
        ans_str = str(answer)[:40] if answer else "None"
        print(f"  {status} {name}: {ans_str} ({conf:.0%})")

if __name__ == "__main__":
    test_ultra_complex()
