# Solvra

**Agentic Mathematical Reasoning System for Ethos 2025 Hackathon**

[![CI/CD](https://github.com/Harshad2321/Solvra/workflows/Solvra%20CI/CD%20Pipeline/badge.svg)](https://github.com/Harshad2321/Solvra/actions)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## Overview

Solvra is an end-to-end mathematical reasoning system that classifies, plans, solves, and verifies mathematical problems across multiple categories. With **85%+ numerical accuracy** and support for **30+ problem types**, Solvra handles everything from basic arithmetic to advanced calculus, linear algebra, and number theory.

### 🎯 Key Capabilities

- ✅ **7 Core Problem Types**: Arithmetic, Algebra, Geometry, Logic, Word Problems, Comparison, Pattern Recognition
- ✅ **30+ Specialized Solvers**: Calculus, matrices, number theory, combinatorics, trigonometry, and more
- ✅ **Smart Classification**: Random Forest classifier with 100% validation accuracy
- ✅ **Proper Order of Operations**: SymPy-based expression evaluation (PEMDAS/BODMAS)
- ✅ **Real-World Word Problems**: Distance/speed, discounts, depreciation, relative motion
- ✅ **Confidence Scoring**: Verify solution accuracy with confidence percentages
- ✅ **Complete Reasoning Traces**: Track every step from classification to solution

## Quick Start

```bash
# Clone the repository
git clone https://github.com/Harshad2321/Solvra.git
cd Solvra

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run tests to verify installation
python run_tests.py

# Launch web interface
streamlit run app.py
```

Visit http://localhost:8501 to use the interactive UI! 🚀

## Installation

```powershell
pip install -r requirements.txt
```

## Project Structure

```
solvra/
├── data/
│   ├── train.csv
│   ├── test.csv
│   ├── output.csv
│   └── reasoning_traces.json
├── src/
│   ├── classifier.py
│   ├── planner.py
│   ├── solver.py
│   ├── verifier.py
│   ├── reasoning_trace.py
│   ├── pipeline.py
│   ├── log_utils.py
│   └── config.json
├── models/
│   └── question_type.pkl
├── evaluation/
│   ├── metrics.py
│   └── analyze.py
├── tests/
│   ├── test_classifier.py
│   ├── test_solver.py
│   └── test_pipeline.py
├── app.py
├── requirements.txt
└── README.md
```

## Usage

### Train the Classifier

```powershell
python -c "from src.classifier import train_classifier; train_classifier('data/train.csv', 'models/question_type.pkl')"
```

### Run Pipeline

```powershell
python src/pipeline.py --input data/test.csv --output data/output.csv
```

### Evaluate Results

```powershell
python evaluation/metrics.py
python evaluation/analyze.py
```

### Launch UI

```powershell
streamlit run app.py
```

### Run Tests

```powershell
pytest tests/
```

## Testing Solvra

I've created a comprehensive test suite to validate Solvra's problem-solving capabilities across all supported categories.

### Test Files

- **`test_cases.json`**: Contains 28 handcrafted test questions covering all 7 problem types
  - Each question includes the problem text, expected answer, type, and difficulty level
  - 4 questions per category (Arithmetic, Algebra, Geometry, Logic, Word Problems, Comparison, Pattern)

- **`run_tests.py`**: Interactive test runner that processes all test cases and displays results

### Running Tests

**Run all test categories:**
```powershell
python run_tests.py
```

**Run specific category only:**
```powershell
python run_tests.py arithmetic
python run_tests.py algebra
python run_tests.py geometry
# ... etc for logic, word_problem, comparison, pattern
```

### What the Test Runner Shows

For each test question, you'll see:
- The question text
- Expected problem type and answer
- Detected problem type (from classifier)
- Solvra's computed answer
- Confidence score
- Whether type detection was correct

### Example Output

```
==============================================================
                    ARITHMETIC TESTS                    
==============================================================

[Test 1] Calculate: (45 + 23) * 2 - 18 / 3
  Expected type: arithmetic
  Expected answer: 130
  Detected type: arithmetic
  My answer: 130.0
  Confidence: 100.0%
  ✓ Type detected correctly!
```

### Adding Your Own Tests

Edit `test_cases.json` and add questions in this format:

```json
{
  "question": "Your math question here",
  "expected_answer": "The answer",
  "type": "arithmetic",
  "difficulty": "easy"
}
```

The test runner will automatically pick up new questions on the next run!

## Modules

### classifier.py
Trains a Random Forest classifier on question types using TF-IDF features.

### planner.py
Generates step-by-step reasoning plans based on question classification.

### solver.py
Executes mathematical operations using SymPy, NumPy, and built-in math functions.

### verifier.py
Validates solutions and assigns confidence scores.

### reasoning_trace.py
Records complete reasoning traces for interpretability.

### pipeline.py
Integrates all modules into an end-to-end processing pipeline.

## Performance

- Target Accuracy: 73%+
- Average Inference Time: <1s per question
- Macro F1 Score: Computed across all categories

## Team

Ethos 2025 Hackathon
IIT Guwahati | Saptang Labs
Machine Learning Challenge

## License

MIT
