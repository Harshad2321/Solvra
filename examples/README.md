# Solvra Examples

This directory contains sample problems and their solutions to help you understand how Solvra works.

## Directory Structure

```
examples/
├── arithmetic_examples.json       # Arithmetic expression problems
├── algebra_examples.json          # Equation solving examples
├── geometry_examples.json         # Shape and measurement problems
├── word_problem_examples.json     # Real-world scenarios
├── pattern_examples.json          # Sequence recognition
├── sample_output/                 # Solution traces and results
│   ├── arithmetic_trace.json
│   ├── algebra_trace.json
│   └── geometry_trace.json
└── README.md                      # This file
```

## Quick Examples

### 1. Arithmetic Expression
```json
{
  "question": "Calculate: (45 + 23) * 2 - 18 / 3",
  "answer": 130,
  "explanation": "Order of operations: (68) * 2 = 136, then 136 - 6 = 130"
}
```

**Running this:**
```bash
python -c "from src.pipeline import SolvraPipeline; p = SolvraPipeline(); print(p.process_question('Calculate: (45 + 23) * 2 - 18 / 3'))"
```

### 2. Word Problem
```json
{
  "question": "A car travels at 60 km/h for 2.5 hours. How far does it go?",
  "answer": 150,
  "explanation": "Distance = Speed × Time = 60 × 2.5 = 150 km"
}
```

### 3. Algebra
```json
{
  "question": "Solve for x: 3x + 5 = 20",
  "answer": 5,
  "explanation": "3x = 15, therefore x = 5"
}
```

### 4. Geometry
```json
{
  "question": "Find the area of a circle with radius 7 cm",
  "answer": 153.94,
  "explanation": "Area = π × r² = π × 49 ≈ 153.94 cm²"
}
```

### 5. Pattern Recognition
```json
{
  "question": "Find the next number: 2, 4, 8, 16, 32, ?",
  "answer": 64,
  "explanation": "Each number is double the previous (geometric sequence, r=2)"
}
```

## Running Examples

### Method 1: Using the Test Runner
```bash
python run_tests.py
```

### Method 2: Using Python API
```python
from src.pipeline import SolvraPipeline

pipeline = SolvraPipeline()

# Single question
result = pipeline.process_question("What is 2^8 + 3^4?")
print(f"Answer: {result['predicted_answer']}")
print(f"Confidence: {result['confidence']}%")
```

### Method 3: Using the Web Interface
```bash
streamlit run app.py
```
Then open http://localhost:8501 and paste your question.

## Sample Output Structure

When you run a problem, Solvra returns:

```python
{
    'predicted_answer': 130.0,
    'confidence': 85.0,
    'question_type': 'arithmetic',
    'steps': [
        'Found expression: (45 + 23) * 2 - 18 / 3',
        'Evaluating with proper order of operations...',
        'Result: 130.0'
    ],
    'trace_id': 'abc123-def456-...'
}
```

## Trace Files

Check `data/reasoning_traces.json` to see the complete reasoning process for each problem, including:
- Classification decision
- Planning steps
- Solving strategy
- Verification results

## Adding Your Own Examples

Create a JSON file with this structure:

```json
{
  "category": "your_category",
  "problems": [
    {
      "question": "Your problem text",
      "expected_answer": "Expected result",
      "difficulty": "easy/medium/hard",
      "tags": ["tag1", "tag2"]
    }
  ]
}
```

Then run:
```bash
python -c "import json; from src.pipeline import SolvraPipeline; p = SolvraPipeline(); data = json.load(open('your_file.json')); [print(p.process_question(q['question'])) for q in data['problems']]"
```

## Common Use Cases

### Testing a New Problem Type
1. Add examples to the appropriate JSON file
2. Run: `python run_tests.py [category]`
3. Check accuracy and confidence scores

### Debugging Solver Behavior
1. Enable detailed logging: `export LOG_LEVEL=DEBUG` (Linux/Mac) or `$env:LOG_LEVEL="DEBUG"` (Windows)
2. Run your problem
3. Check `logs/system.log` for detailed trace

### Benchmarking Performance
```bash
time python run_tests.py  # Unix
Measure-Command { python run_tests.py }  # PowerShell
```

## Tips

- **Start simple**: Test basic problems before complex ones
- **Check logs**: `logs/system.log` shows classification and solving steps
- **Verify answers**: Compare with expected results in test files
- **Experiment**: Try variations of problems to understand solver behavior

## Need Help?

- Check `TESTING_GUIDE.md` for detailed testing instructions
- See `PROBLEM_TYPES.md` for all supported problem categories
- Read `SOLVER_IMPROVEMENTS.md` for recent enhancements
- Open an issue on GitHub for bugs or questions
