# Example Problems

This folder contains sample math problems for testing Solvra.

## Files

- `arithmetic_examples.json` - Basic calculations
- `algebra_examples.json` - Equations to solve
- `pattern_examples.json` - Number sequences
- `word_problem_examples.json` - Real-world problems

## Sample Problem Format

```json
{
  "question": "Calculate: (45 + 23) * 2 - 18 / 3",
  "answer": 130
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
  "answer": 150
}
```

## How to Use These Examples

You can test these examples by running:

```bash
python run_tests.py
```

Or use them in the web app:

```bash
streamlit run app.py
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


