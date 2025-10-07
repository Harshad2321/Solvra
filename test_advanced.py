"""
Test suite for advanced mathematical problem solving
Tests 10 complex problem types from competition-level mathematics
"""

from src.pipeline import SolvraPipeline

def test_all_advanced_problems():
    pipeline = SolvraPipeline()
    
    problems = [
        {
            "name": "1. Nested Radicals",
            "question": "Evaluate exactly: sqrt(6 + 2*sqrt(5)) + sqrt(6 - 2*sqrt(5))",
            "expected": "Should simplify to a simple form"
        },
        {
            "name": "2. Parametric Equation",
            "question": "Find all real x (in terms of parameter m) that satisfy x^4 - 4*m*x^2 + 4*m^2 - 1 = 0",
            "expected": "Solutions in terms of m"
        },
        {
            "name": "3. Circle Segment",
            "question": "In circle with radius R, a chord of length L subtends an angle theta at the center. Express the area of the circular segment cut off by the chord in terms of R and L only.",
            "expected": "Area formula in R and L"
        },
        {
            "name": "4. Work Rate Problem",
            "question": "Two painters, A and B, working together can paint a fence in 6 hours. Painter A alone takes 4 hours less than painter B alone. How long does each take individually?",
            "expected": "A: 10 hours, B: 14 hours (approximately)"
        },
        {
            "name": "5. Logic Puzzle (Knights/Knaves)",
            "question": """On an island of knights (always truth) and knaves (always lie) three people say:
P: "I am a knave."
Q: "P is a knight."
R: "Exactly two of us are knights."
Determine the types (knight/knave) of P,Q,R.""",
            "expected": "P: Knight, Q: Knight, R: Knight"
        },
        {
            "name": "6. Inequality Proof",
            "question": "Prove for all real x that (x^2 + 1)/(x^2 + 2) <= 1 - 1/(x^2 + 2)^2. Decide when equality holds.",
            "expected": "Equality conditions"
        },
        {
            "name": "7. Non-homogeneous Recurrence",
            "question": "Sequence defined by b_0 = 0, b_1 = 1, and for n >= 2: b_n = 3*b_(n-1) - 2*b_(n-2) + 2^n. Find closed form for b_n.",
            "expected": "Closed form with 2^n terms"
        },
        {
            "name": "8. Diophantine Equation",
            "question": "Find all integer solutions (x, y) to x^2 - 5*y^2 = 4",
            "expected": "Integer solution pairs"
        },
        {
            "name": "9. Hyperbola Locus",
            "question": "Fixed segment AB length 10. Let P move such that |PA| - |PB| = 6. Describe the locus of P and give its equation in Cartesian coordinates if A = (0,0), B = (10,0).",
            "expected": "Hyperbola equation"
        },
        {
            "name": "10. Constrained Optimization",
            "question": "Find the maximum value of f(x,y) = x^2*y subject to x^2 + 2*y^2 = 8 with real x, y.",
            "expected": "Maximum value"
        }
    ]
    
    print("=" * 80)
    print("ADVANCED MATHEMATICAL PROBLEM SOLVING TEST SUITE")
    print("=" * 80)
    print()
    
    results = []
    for i, prob in enumerate(problems, 1):
        print(f"\n{'=' * 80}")
        print(f"{prob['name']}")
        print(f"{'=' * 80}")
        print(f"Question: {prob['question'][:100]}...")
        print(f"Expected: {prob['expected']}")
        print()
        
        try:
            result = pipeline.process_question(prob['question'])
            answer = result.get('predicted_answer', result.get('answer'))
            confidence = result.get('confidence', 0.0)
            steps = result.get('steps', [])
            
            print(f"Answer: {answer}")
            print(f"Confidence: {confidence:.2%}")
            
            # Get trace for steps
            if 'trace_id' in result:
                print(f"Trace ID: {result['trace_id']}")
            
            results.append({
                'problem': prob['name'],
                'answer': answer,
                'confidence': confidence,
                'success': answer is not None
            })
        except Exception as e:
            print(f"ERROR: {e}")
            results.append({
                'problem': prob['name'],
                'answer': None,
                'confidence': 0.0,
                'success': False
            })
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    successful = sum(1 for r in results if r['success'])
    print(f"Successful: {successful}/{len(results)}")
    print(f"Success Rate: {successful/len(results)*100:.1f}%")
    print()
    print("Results by problem:")
    for r in results:
        status = "[OK]" if r['success'] else "[FAIL]"
        print(f"  {status} {r['problem']}: {r['answer']} (conf: {r['confidence']:.2%})")

if __name__ == "__main__":
    test_all_advanced_problems()
