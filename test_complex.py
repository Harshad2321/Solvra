import sys
sys.path.insert(0, '.')

from src.pipeline import SolvraPipeline

pipeline = SolvraPipeline()

print("=" * 60)
print("TESTING ENHANCED SOLVRA WITH COMPLEX PROBLEMS")
print("=" * 60)

test_cases = [
    ("Excircle Geometry", "In triangle ABC with AB equals 13 and AC equals 15 find the excircle radius opposite A in terms of altitude h"),
    ("Pattern with Recurrence", "Sequence a_n where a_1 equals 1 and a_2 equals 1 and a_n equals a_(n-1) plus 2 times a_(n-2) find a_10"),
    ("Quadratic Pattern", "Find next in sequence 2 5 10 17 26"),
    ("Fibonacci Pattern", "Continue sequence 1 1 2 3 5 8 13"),
    ("System of Equations", "Solve system x plus y equals 5 and x minus y equals 1"),
    ("Cubic Equation", "Solve cubic 2t^3 minus 9t plus 10 equals 0"),
    ("Boat Problem", "A boat travels 30 km upstream and downstream. Downstream speed is 12 km/h. Upstream takes 3 hours more than downstream. Find boat speed v and current speed c"),
    ("Heron Triangle", "Find area of triangle with sides 13, 14, 15 using Heron formula"),
]

for i, (name, question) in enumerate(test_cases, 1):
    print(f"\n{i}. {name}")
    print(f"Q: {question}")
    try:
        result = pipeline.process_question(question)
        print(f"A: {result['predicted_answer']}")
        print(f"Confidence: {result['confidence']:.1%}")
        print(f"Type: {pipeline.classifier.predict_type(question)}")
    except Exception as e:
        print(f"Error: {e}")

print("\n" + "=" * 60)
print("TESTING COMPLETE")
print("=" * 60)
