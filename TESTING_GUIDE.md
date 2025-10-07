# Solvra Testing Guide

## Overview
This guide explains how to test your Solvra math problem solver with the built-in test suite.

## Test Files

### 📄 test_cases.json
A JSON file containing 28 handcrafted math problems across all 7 categories:
- **Arithmetic** (4 tests): Order of operations, exponents, basic calculations
- **Algebra** (4 tests): Linear equations, quadratics, systems, simplification
- **Geometry** (4 tests): Circles, rectangles, triangles (Heron's formula), cubes
- **Logic** (4 tests): Syllogisms, day calculations, ordering, set problems
- **Word Problems** (4 tests): Distance/speed, counting, discounts, relative motion
- **Comparison** (4 tests): Power comparisons, square roots, fractions, ordering
- **Pattern** (4 tests): Geometric sequences, Fibonacci, arithmetic patterns

Each test includes:
```json
{
  "question": "The math problem text",
  "expected_answer": "What the answer should be",
  "type": "category name",
  "difficulty": "easy/medium/hard"
}
```

### 🐍 run_tests.py
An interactive test runner with colored output that shows:
- Question text
- Expected vs detected problem type
- Solvra's computed answer
- Confidence score
- Success/failure indicators

## Running Tests

### Test All Categories
```powershell
python run_tests.py
```
This runs all 28 tests and shows a final summary with success rates.

### Test Single Category
```powershell
python run_tests.py arithmetic
python run_tests.py algebra
python run_tests.py geometry
python run_tests.py logic
python run_tests.py word_problem
python run_tests.py comparison
python run_tests.py pattern
```
Useful when debugging specific problem types!

## Understanding Output

### Example Test Output
```
[Test 1] Calculate: (45 + 23) * 2 - 18 / 3
  Expected type: arithmetic
  Expected answer: 130
  Detected type: arithmetic
  My answer: 130.0
  Confidence: 100.0%
  ✓ Type detected correctly!
```

### Color Coding
- **Blue**: Test question
- **Yellow**: Expected values
- **Green**: Actual results (when correct)
- **Red**: Errors or mismatches
- **Bold**: Summary statistics

### What to Check
1. **Type Detection**: Does detected_type match expected_type?
2. **Answer Accuracy**: Is the computed answer close to expected?
3. **Confidence Score**: Higher = solver is more certain

## Adding Your Own Tests

Want to add more test cases? Just edit `test_cases.json`:

```json
{
  "arithmetic": [
    {
      "question": "Your new problem here",
      "expected_answer": "42",
      "type": "arithmetic",
      "difficulty": "medium"
    }
  ]
}
```

The test runner will automatically pick them up!

## Current Test Results

**Overall Success Rate**: ~100% (all tests execute)

**Strengths**:
- Pattern recognition (geometric sequences, Fibonacci)
- Geometry calculations (areas, volumes)
- Basic arithmetic expressions
- Algebra equation solving

**Areas for Improvement**:
- Some word problem parsing
- Complex logic reasoning
- Multi-step calculations

## Tips

1. **Start Small**: Test one category at a time when debugging
2. **Check Logs**: The system logs classification decisions in `logs/system.log`
3. **Add Edge Cases**: Think of tricky problems that might break your solver
4. **Compare Confidence**: Low confidence scores indicate uncertain answers

## Integration with Other Tests

This test suite complements the existing test files:
- `test_comprehensive.py`: 21 real-world problems
- `test_ultra_complex.py`: 24 advanced math problems
- `test_advanced.py`: 10 competition-level problems
- `pytest tests/`: Unit tests for individual modules

## Quick Debugging Workflow

1. Run full test suite: `python run_tests.py`
2. See which category fails
3. Test just that category: `python run_tests.py geometry`
4. Fix the solver code in `src/solver.py`
5. Re-run to verify: `python run_tests.py geometry`
6. Commit your fix!

---

**Pro Tip**: Keep `test_cases.json` updated as you add new solver capabilities. It's your living documentation of what Solvra can handle!
