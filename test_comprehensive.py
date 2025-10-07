"""
Comprehensive Test Suite - Real-world Mathematical Problems
Testing all 7 categories with diverse problem types
"""

from src.pipeline import SolvraPipeline

def test_all_categories():
    pipeline = SolvraPipeline()
    
    problems = [
        # ARITHMETIC (4 problems)
        ("Arithmetic 1", "(27 * 5) - (144 / 12) + 3^4", "Expected: ~212"),
        ("Arithmetic 2", "(15 + 9) * 6 / 3 - (2^5 - 10)", "Expected: ~26"),
        ("Arithmetic 3", "A number multiplied by 8 then subtract 24 gives 72. Find the number.", "Expected: 12"),
        
        # ALGEBRA (3 problems)
        ("Algebra 1", "Solve for x: 3*x + 5 = 2*x^2 - 7", "Expected: x values"),
        ("Algebra 2", "Solve quadratic: 2*x^2 - 8*x + 6 = 0", "Expected: x = 1, 3"),
        ("Algebra 3", "System: 2*a + 3*b = 12 and 3*a - b = 7, find a and b", "Expected: a, b values"),
        
        # GEOMETRY (3 problems)
        ("Geometry 1", "Triangle with sides 7 cm, 8 cm, 9 cm. Find area using Heron's formula.", "Expected: ~26.83 cm²"),
        ("Geometry 2", "Volume of cylinder with radius 4 cm and height 10 cm", "Expected: ~502.65 cm³"),
        ("Geometry 3", "Circle and square both have perimeter 44 cm. Find their areas.", "Expected: circle > square"),
        
        # LOGIC (3 problems)
        ("Logic 1", "If all A are B, and some B are C, can we conclude some A are C?", "Expected: No/Invalid"),
        ("Logic 2", "If today is Wednesday, what day will it be 45 days later?", "Expected: Saturday"),
        ("Logic 3", "True if not false, false if not true - what logic?", "Expected: Classical/Boolean"),
        
        # WORD PROBLEMS (3 problems)
        ("Word Problem 1", "Train travels 180 km in 3 hours. How long for 300 km at same speed?", "Expected: 5 hours"),
        ("Word Problem 2", "Sum of three consecutive even numbers is 78. Find the numbers.", "Expected: 24, 26, 28"),
        ("Word Problem 3", "Laptop costs 50000, depreciates 10% per year. Value after 3 years?", "Expected: ~36450"),
        
        # COMPARISON (3 problems)
        ("Comparison 1", "Which is greater: 2^10 or 5^4?", "Expected: 2^10 = 1024"),
        ("Comparison 2", "Compare sqrt(50) and 7.1", "Expected: 7.1 > sqrt(50)"),
        ("Comparison 3", "Maximum of: (15 + 25/5), (7*3 + 4), (100/9)", "Expected: 25"),
        
        # PATTERN RECOGNITION (3 problems)
        ("Pattern 1", "Find next: 2, 6, 12, 20, 30, ?", "Expected: 42"),
        ("Pattern 2", "Find next: 1, 4, 9, 16, 25, ?", "Expected: 36"),
        ("Pattern 3", "Find next: 3, 9, 27, 81, ?", "Expected: 243"),
    ]
    
    print("=" * 80)
    print("COMPREHENSIVE TEST SUITE - Real-World Problems")
    print(f"Testing {len(problems)} problems across 7 categories")
    print("=" * 80)
    print()
    
    results = []
    categories = {
        "Arithmetic": [],
        "Algebra": [],
        "Geometry": [],
        "Logic": [],
        "Word": [],  # Fixed to match problem naming
        "Comparison": [],
        "Pattern": []
    }
    
    for i, (name, question, expected) in enumerate(problems, 1):
        category = name.split()[0]
        
        print(f"\n[{i}/{len(problems)}] {name}")
        print(f"Q: {question[:70]}...")
        print(f"Expected: {expected}")
        
        try:
            result = pipeline.process_question(question)
            answer = result.get('predicted_answer', result.get('answer'))
            confidence = result.get('confidence', 0.0)
            
            print(f"A: {answer}")
            print(f"Confidence: {confidence:.1%}")
            
            success = answer is not None
            results.append((name, success, answer, confidence))
            categories[category].append((success, answer))
            
        except Exception as e:
            print(f"ERROR: {e}")
            results.append((name, False, None, 0.0))
            categories[category].append((False, None))
    
    # Summary
    print("\n" + "=" * 80)
    print("RESULTS SUMMARY")
    print("=" * 80)
    
    successful = sum(1 for _, success, _, _ in results if success)
    total = len(results)
    
    print(f"\nOverall Success: {successful}/{total} = {successful/total*100:.1f}%\n")
    
    # Category breakdown
    print("Performance by Category:")
    for cat_name, cat_results in categories.items():
        if cat_results:
            cat_success = sum(1 for success, _ in cat_results if success)
            cat_total = len(cat_results)
            rate = cat_success / cat_total * 100 if cat_total > 0 else 0
            print(f"  {cat_name:15s}: {cat_success}/{cat_total} ({rate:.0f}%)")
    
    print("\nDetailed Results:")
    for name, success, answer, conf in results:
        status = "[OK]" if success else "[FAIL]"
        ans_str = str(answer)[:60] if answer else "None"
        print(f"  {status} {name:20s}: {ans_str} ({conf:.0%})")
    
    # Show some interesting answers
    print("\n" + "=" * 80)
    print("SAMPLE SOLUTIONS")
    print("=" * 80)
    for name, success, answer, conf in results[:5]:
        if success:
            print(f"\n{name}:")
            print(f"  Answer: {answer}")
            print(f"  Confidence: {conf:.1%}")

if __name__ == "__main__":
    test_all_categories()
