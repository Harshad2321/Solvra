import sys
sys.path.insert(0, '.')

from src.solver import MathSolver

solver = MathSolver()

question = "Sequence a_n where a_1 equals 1 and a_2 equals 1 and a_n equals a_(n-1) plus 2 times a_(n-2) find a_10"
plan = {'type': 'pattern', 'steps': []}

print("=" * 60)
print("RECURRENCE RELATION: a_n = a_(n-1) + 2*a_(n-2)")
print("Given: a_1 = 1, a_2 = 1")
print("=" * 60)

result = solver.solve_pattern(question, plan)

print("\nSteps:")
for i, step in enumerate(result['steps'], 1):
    print(f"{i}. {step}")

print(f"\nAnswer: a_10 = {result['answer']}")
print("\nExpected: a_10 = 341")

print("\n" + "=" * 60)
print("VERIFICATION: Computing directly")
print("=" * 60)

a = [0, 1, 1]
for n in range(3, 11):
    a_n = a[n-1] + 2 * a[n-2]
    a.append(a_n)
    print(f"a_{n} = a_{n-1} + 2*a_{n-2} = {a[n-1]} + 2*{a[n-2]} = {a_n}")

print(f"\nDirect calculation: a_10 = {a[10]}")

print("\n" + "=" * 60)
print("CLOSED FORM")
print("=" * 60)
print("Characteristic equation: r² - r - 2 = 0")
print("Roots: r₁ = 2, r₂ = -1")
print("General form: a_n = α*2^(n-1) + β*(-1)^(n-1)")
print("\nFrom initial conditions:")
print("a_1 = 1: α + β = 1")
print("a_2 = 1: 2α - β = 1")
print("Solving: α = 2/3, β = 1/3")
print("\nClosed form: a_n = (2/3)*2^(n-1) + (1/3)*(-1)^(n-1)")
print(f"a_10 = (2/3)*2^9 + (1/3)*(-1)^9")
print(f"a_10 = (2/3)*512 + (1/3)*(-1)")
print(f"a_10 = 1024/3 - 1/3 = 1023/3 = 341")
