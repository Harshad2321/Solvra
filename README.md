# Solvra - Math Problem Solver

A machine learning-based mathematical reasoning system built for the Ethos 2025 Hackathon at IIT Guwahati.

## What is Solvra?

Solvra is an AI system that can solve different types of math problems automatically. It uses machine learning to understand what type of problem you're asking, then solves it step-by-step.

### Features

- Solves 7 types of math problems: Arithmetic, Algebra, Geometry, Logic, Word Problems, Comparisons, and Patterns
- Uses Random Forest classifier to identify problem types
- Handles expressions with proper order of operations (PEMDAS)
- Shows confidence scores for solutions
- Web interface built with Streamlit

## How to Run

### Setup

1. Clone this repository
2. Install required packages:
```bash
pip install -r requirements.txt
```

### Running the Application

**Web Interface:**
```bash
streamlit run app.py
```
Then open your browser to http://localhost:8501

**Run Tests:**
```bash
python run_tests.py
```

## Project Structure

```
Solvra/
├── src/                    # Core modules
│   ├── classifier.py       # Problem type classifier
│   ├── solver.py          # Math solver
│   ├── pipeline.py        # Main pipeline
│   └── ...
├── data/                   # Training & test data
├── models/                 # Trained models
├── tests/                  # Unit tests
├── examples/              # Example problems
├── app.py                 # Streamlit web app
└── requirements.txt
```

## Testing

We've created test cases to check if Solvra works correctly.

**Run all tests:**
```bash
python run_tests.py
```

**Run specific category:**
```bash
python run_tests.py arithmetic
python run_tests.py algebra
```

The test file (`test_cases.json`) contains sample problems for each category.

## How It Works

1. **Classifier** (`classifier.py`) - Identifies what type of math problem it is
2. **Planner** (`planner.py`) - Creates a plan to solve it
3. **Solver** (`solver.py`) - Performs the calculations using SymPy and NumPy
4. **Verifier** (`verifier.py`) - Checks the answer and gives a confidence score
5. **Pipeline** (`pipeline.py`) - Connects everything together

## Technologies Used

- Python 3.10+
- scikit-learn (Random Forest Classifier)
- SymPy (Symbolic mathematics)
- NumPy (Numerical computing)
- Pandas (Data handling)
- Streamlit (Web interface)

## Project Team

Created for Ethos 2025 Hackathon at IIT Guwahati

## License

MIT License
