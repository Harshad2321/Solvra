# Solvra - Agentic Reasoning System

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Accuracy](https://img.shields.io/badge/accuracy-96%25-brightgreen)](#-performance-results)
[![F1 Score](https://img.shields.io/badge/F1--Score-95.71%25-brightgreen)](#-performance-results)

> **Ethos 2025 – Saptang Labs Machine Learning Challenge**

An advanced modular reasoning system that solves logic-based problems through autonomous problem decomposition, intelligent tool selection, and step-by-step reasoning — without relying on proprietary large language models.

---

##  Table of Contents

- [About This Project](#-about-this-project)
- [Performance Results](#-performance-results)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Getting Started](#-getting-started)
- [Project Structure](#-project-structure)
- [Usage](#-usage)
- [Reasoning Strategies](#-reasoning-strategies)
- [Customization](#-customization)
- [Results & Reports](#-results--reports)
- [Troubleshooting](#-troubleshooting)
- [Future Improvements](#-future-improvements)
- [Team & Acknowledgments](#-team--acknowledgments)

---

##  About This Project

This is our submission for the **Ethos 2025 ML Challenge**. We built a system that can solve different types of reasoning problems by breaking them down into smaller steps and using specialized solvers for each type.

The idea was to create something that can handle various kinds of logic puzzles — from math problems to spatial reasoning to riddles — without needing a huge language model. We wanted to keep it explainable so you can actually see how it arrives at each answer.

### What Problems Does It Solve?

Our system can handle these types of problems:

- ✅ **Optimization and planning** (scheduling, resource allocation)
- ✅ **Spatial reasoning** (3D geometry, navigation, cube problems)
- ✅ **Sequence solving** (finding patterns in numbers or sequences)
- ✅ **Operation of mechanisms** (gears, machines, how things work)
- ✅ **Classic riddles and lateral thinking**
- ✅ **Logical traps and deduction problems**

---

##  Performance Results

We tested our system on the training data and achieved these results:

| Metric | Value |
|--------|-------|
| **Overall Accuracy** | 96% (48 out of 50 correct) |
| **F1 Score (Macro)** | 95.71% |
| **Processing Speed** | ~0.0002 seconds per problem |
| **Throughput** | 8,534+ problems per second |

### Performance by Problem Type

| Problem Type | Accuracy |
|--------------|----------|
| Spatial reasoning | 100% |
| Sequence solving | 100% |
| Operation of mechanisms | 100% |
| Lateral thinking | 100% |
| Logic traps | 100% |
| Optimization | 88.9% |
| Riddles | 83.3% |

*Note: We're still working on improving riddle solving, which requires more lateral thinking.*

---

##  Key Features

-  **Modular Architecture**: Specialized solvers for different reasoning types
-  **Problem Decomposition**: Breaks complex problems into manageable subproblems
-  **Intelligent Tool Selection**: Automatically picks the right solver for each problem
-  **Verification System**: Validates and self-corrects reasoning steps
-  **Explainable AI**: Complete trace of the decision-making process
-  **ML Enhancement**: Learns patterns from training data without losing explainability
-  **No Proprietary LLMs**: Uses symbolic reasoning and small open models
-  **High Performance**: Processes thousands of problems per second

---

##  System Architecture

### How It Works

Our system follows a multi-stage pipeline:

#### 1. **Preprocessing**
- Extracts features from each problem
- Identifies problem type (math, spatial, logic, etc.)
- Cleans and normalizes the data

#### 2. **Pattern Matching**
- Recognizes over 65 common problem patterns
- Matches problems against known solution templates
- Identifies arithmetic, geometric, and polynomial sequences

#### 3. **Reasoning Agent**
- Coordinates the entire solving process
- Breaks problems down into smaller steps
- Selects the appropriate solver for each problem type

#### 4. **Specialized Solvers**
Different solvers for different problem types:

- **MathSolver**: Arithmetic, algebra, optimization (uses SymPy for symbolic computation)
- **LogicSolver**: Truth tables, deduction, logical puzzles
- **SpatialSolver**: 3D geometry, navigation, cube transformations
- **SequenceSolver**: Pattern recognition in numerical sequences

#### 5. **Verification**
- Checks if answers are in valid range (1-5)
- Verifies numerical and logical consistency
- Applies domain-specific validation rules
- Corrects obvious errors before finalizing

#### 6. **Trace Logging**
- Records every decision step
- Saves intermediate results
- Documents verification warnings
- Creates detailed reports for analysis

---

##  Getting Started

### Requirements

- **Python 3.10 or higher**
- **pip** package manager
- **4GB+ RAM** recommended

### Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd Solvra
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

That's it! No API keys or special setup needed.

---

##  Project Structure

```
Solvra/
├── data/
│   ├── train.csv              # Training data (384 examples)
│   ├── test.csv               # Test data (96 examples)
│   ├── predictions.csv        # Generated predictions
│   └── output.csv             # Expected output format
│
├── src/
│   ├── main.py                # Main script to run everything
│   ├── preprocess.py          # Data preprocessing & feature extraction
│   ├── reasoning_agent.py     # Main reasoning orchestrator
│   ├── solver.py              # Specialized solving engines
│   ├── verifier.py            # Reasoning verification & correction
│   ├── pattern_matcher.py     # Pattern recognition
│   ├── ml_enhancer.py         # ML components
│   └── trace_logger.py        # Logging & explainability
│
├── reports/
│   ├── reasoning_traces_*.json    # Detailed reasoning traces
│   ├── reasoning_summary_*.csv    # Summary statistics
│   └── performance_metrics.txt    # Performance results
│
└── requirements.txt           # Python dependencies
```

---

##  Usage

### Quick Start

To train the system and generate predictions:

```bash
cd src
python main.py
```

This will:
1. Load and preprocess the training data
2. Train the reasoning system
3. Generate predictions for the test data
4. Save results to `data/predictions.csv`
5. Create detailed reports in the `reports/` folder

**The entire process takes less than a minute to run!**

### Step-by-Step Usage

#### 1. Data Preprocessing

```python
from preprocess import DataPreprocessor

preprocessor = DataPreprocessor(data_dir="../data")
train_df, test_df = preprocessor.load_data()
train_df = preprocessor.preprocess_training_data()
test_df = preprocessor.preprocess_test_data()
```

#### 2. Reasoning on a Single Problem

```python
from reasoning_agent import ReasoningAgent

agent = ReasoningAgent()

problem = {
    'topic': 'Sequence solving',
    'problem_statement': 'Find next: 2, 5, 10, 17, 26, ?',
    'answer_option_1': '35',
    'answer_option_2': '37',
    'answer_option_3': '39',
    'answer_option_4': '41',
    'answer_option_5': '43'
}

prediction, trace = agent.reason_step_by_step(problem)
print(f"Predicted: Option {prediction}")
```

#### 3. Running with Verification

```python
from reasoning_agent import ReasoningAgent
from verifier import ReasoningVerifier

agent = ReasoningAgent()
verifier = ReasoningVerifier()

prediction, trace = agent.reason_step_by_step(problem)
corrected = verifier.apply_correction_heuristics(problem, prediction, trace)
print(verifier.get_verification_report())
```

### Example: Solving a Sequence Problem

**Problem:** "Find the next number: 2, 5, 10, 17, 26, ?"

**Solvra's process:**
1. Extracts the sequence: [2, 5, 10, 17, 26]
2. Calculates differences: [3, 5, 7, 9]
3. Notices the differences increase by 2 each time
4. Predicts next difference: 11
5. Calculates answer: 26 + 11 = 37
6. Verifies it makes sense

**Answer:** 37  
**Time:** 0.0002 seconds

---

##  Reasoning Strategies

### For Optimization Problems
1. Extract all constraints from the problem
2. Identify optimization objective (minimize/maximize)
3. Evaluate all feasible solutions
4. Apply greedy or exhaustive search

### For Spatial Problems
1. Visualize the spatial configuration
2. Extract dimensions and positions
3. Apply geometric formulas
4. Validate against physical constraints

### For Sequence Problems
1. Extract the numerical sequence
2. Test common patterns (arithmetic, geometric, recursive)
3. Apply polynomial fitting if simple patterns don't work
4. Verify the prediction makes sense

### For Logic Problems
1. Extract logical statements
2. Build truth tables
3. Apply deductive reasoning
4. Check for contradictions

---

##  Customization

### Adjusting Training Size

Edit `main.py`:
```python
pipeline.run_full_pipeline(
    train_samples=533,  
    generate_test_predictions=True
)
```



### Modifying Solvers

In `solver.py`, adjust solving strategies for each problem type.

### Customizing Verification Rules

In `verifier.py`, add custom verification logic:
```python
def verify_custom_rule(self, problem, prediction):
    # Your verification logic
    return is_valid
```

---

##  Results & Reports

After running the system, you'll find:

### 1. Console Output
Shows real-time progress and a summary at the end with accuracy by topic.

### 2. Predictions File
`data/predictions.csv` - Final predictions in the required format

### 3. JSON Traces
`reports/reasoning_traces_*.json` - Complete reasoning traces showing every step the system took for each problem

### 4. CSV Summary
`reports/reasoning_summary_*.csv` - Tabular summary with one row per problem showing the prediction, actual answer (if known), and key metrics

### 5. Performance Metrics
`reports/performance_metrics.txt` - Detailed statistics including:
- Overall accuracy
- Topic-wise breakdown
- Inference time distribution
- System configuration

---

##  Troubleshooting

### Import Errors
```bash
pip install --upgrade -r requirements.txt
```

### Out of Memory
Reduce the number of training samples in `main.py`

### Slow Performance
The system should be fast (< 1 second for all 96 test problems). If it's slow:
- Check if you're running in debug mode
- Make sure tqdm progress bars aren't slowing things down
- Try running from command line instead of an IDE

### Low Accuracy on Specific Topics
- Check reasoning traces for that topic in the `reports/` folder
- Adjust solver logic in `solver.py`
- Add topic-specific rules in `reasoning_agent.py`

---

##  Technical Details

### Pattern Matching

We implemented patterns for:
- Arithmetic sequences (constant difference)
- Geometric sequences (constant ratio)
- Polynomial sequences
- Fibonacci-like sequences
- Spatial transformations
- Common riddle structures

### Symbolic Computation

Using SymPy, we can solve:
- Algebraic equations
- Optimization problems
- Geometric calculations
- Number theory problems

### Machine Learning

We use scikit-learn for:
- Feature engineering
- Pattern classification
- Confidence estimation
- Ensemble predictions

### Verification Rules

We check for:
- Answer in valid range (1-5)
- Numerical consistency
- Logical contradictions
- Domain-specific constraints

---

##  Our Approach

We tried different approaches and combined what worked best:

### 1. Pattern Recognition
Many problems follow common patterns, so we built a pattern matcher to recognize these quickly.

### 2. Rule-Based Reasoning
For logic and math problems, we use symbolic computation and predefined rules.

### 3. Verification
We added a verification step to catch obvious mistakes before finalizing answers.

### 4. ML Enhancement
We use machine learning for pattern recognition where pure rules don't work well.

### What We Tried

1. **Pure Rule-Based** - Started with just rules and pattern matching. It worked okay but wasn't flexible enough.

2. **Pure Machine Learning** - Tried using just ML models but they weren't very accurate with our small dataset and weren't explainable.

3. **Hybrid Approach** *(what we ended up with)* - Combined pattern matching, symbolic reasoning, and ML. This gave us the best accuracy while keeping things explainable.

---

##  What Makes This Different

Most approaches either:
- Use big language models (expensive, not always accurate, hard to explain)
- Use pure ML (needs lots of data, black box)
- Use pure rules (rigid, doesn't generalize well)

**We combined the best of all three:**
- Pattern matching for common cases
- Symbolic reasoning for exact problems
- ML for learning from examples
- Complete explainability through logging

---

##  Challenges We Faced

1. **Spatial Reasoning** - These problems are tricky because you need to visualize 3D shapes and transformations. We're still working on improving this.

2. **Ambiguous Problems** - Some problems can be interpreted in multiple ways. We had to add logic to pick the most reasonable interpretation.

3. **Riddles** - These often require lateral thinking that doesn't follow normal patterns. Our accuracy here is lower (83%) compared to other problem types.

4. **Small Dataset** - With only 384 training examples, we couldn't rely purely on ML. That's why we focused on patterns and rules.

5. **Speed vs Accuracy** - We had to balance thorough checking (which takes time) with fast inference. We optimized the critical paths.

---

##  Future Improvements

Things we'd like to add if we had more time:

- Better spatial reasoning (maybe add visualization)
- More sophisticated pattern matching
- Integration with a small language model for natural language understanding
- More comprehensive test coverage
- Support for more problem types
- Interactive demo/web interface

---

##  Dependencies

Main libraries we use:

- `pandas` - Data manipulation
- `numpy` - Numerical operations
- `sympy` - Symbolic mathematics
- `scikit-learn` - ML utilities
- `tqdm` - Progress bars
- `colorama` - Colored console output

See `requirements.txt` for the complete list with versions.

---

##  Team & Acknowledgments

This project was built for the **Ethos 2025 challenge**. We're students interested in AI and reasoning systems.

### Acknowledgments

Thanks to **Saptang Labs** for organizing this challenge and providing an interesting problem set. It was fun to work on!

---

##  License

This project was created for the Ethos 2025 hackathon.

---

##  Quick Start Guide

If you just want to run it quickly:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the system
cd src
python main.py

# Check your predictions
# Your predictions are now in data/predictions.csv
```

That's it! The system will process everything and generate your predictions file.

---

**For questions or issues, check the reasoning traces in the reports folder to see what the system was thinking.**

---
