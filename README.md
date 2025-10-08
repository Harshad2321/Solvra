# 🤖 Solvra - Agentic Reasoning System

**Ethos 2025 – Saptang Labs Machine Learning Challenge**

An advanced modular reasoning system that solves structured, logic-based problems through step-by-step agentic reasoning.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app.streamlit.app)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

## 🌐 Try It Live!

**[Launch Web App](https://your-app.streamlit.app)** - Interactive web interface

---

## 🎯 Project Overview

Solvra is an **Agentic Reasoning System** designed to tackle diverse reasoning challenges including:
- ✅ Optimization and planning
- ✅ Spatial reasoning (3D geometry, navigation)
- ✅ Sequence solving (patterns, progressions)
- ✅ Operation of mechanisms (gears, machines)
- ✅ Classic riddles and lateral thinking
- ✅ Logical traps and deduction

### Key Features

🧩 **Modular Architecture**: Specialized solvers for different reasoning types  
🔍 **Problem Decomposition**: Breaks complex problems into manageable subproblems  
🛠️ **Tool Selection**: Intelligently selects appropriate reasoning engines  
✔️ **Verification System**: Validates and corrects reasoning steps  
📝 **Explainable Reasoning**: Complete trace of decision-making process  
🚫 **No Proprietary LLMs**: Uses symbolic reasoning + small open models

---

## 📁 Project Structure

```
Solvra/
├── data/                          # Dataset directory
│   ├── train.csv                  # Training data (534 examples)
│   ├── test.csv                   # Test data (101 examples)
│   ├── output.csv                 # Expected output format
│   └── predictions.csv            # Generated predictions
│
├── src/                           # Source code
│   ├── preprocess.py             # Data preprocessing & feature extraction
│   ├── reasoning_agent.py        # Main reasoning orchestrator
│   ├── solver.py                 # Specialized solving engines
│   ├── verifier.py               # Reasoning verification & correction
│   ├── trace_logger.py           # Logging & explainability
│   └── main.py                   # Main pipeline orchestrator
│
├── models/                        # Model storage (for future ML components)
├── reports/                       # Generated reports & traces
│   ├── reasoning_traces_*.json   # Detailed reasoning traces
│   ├── reasoning_summary_*.csv   # Summary statistics
│   └── reasoning_report_*.html   # Interactive HTML report
│
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

---

## 🚀 Getting Started

### Quick Start - Web UI

The easiest way to use Solvra:

```bash
# Install dependencies
pip install -r requirements.txt

# Launch web interface
streamlit run app.py
```

Then open `http://localhost:8501` in your browser!

### Prerequisites

- Python 3.10 or higher
- pip package manager
- 4GB+ RAM recommended

### Installation

1. **Clone or navigate to the project directory**:
```bash
cd Solvra
```

2. **Create a virtual environment** (recommended):
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Download spaCy model** (if using NLP features):
```bash
python -m spacy download en_core_web_sm
```

---

## 🎮 Usage

### Quick Start - Run Full Pipeline

```bash
cd src
python main.py
```

This will:
1. Load and preprocess data
2. Analyze training examples
3. Generate predictions for test set
4. Create detailed reports and traces

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
    # ... other options
}

prediction, trace = agent.reason_step_by_step(problem)
print(f"Predicted: Option {prediction}")
print(agent.get_trace_summary())
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

---

## 🧠 System Architecture

### 1. Problem Decomposition
The system breaks down complex problems into smaller, manageable subproblems:
- Extract constraints and objectives
- Identify problem type (math, spatial, logic, etc.)
- Create execution plan

### 2. Tool Selection
Intelligently selects the appropriate solver:
- **MathSolver**: Arithmetic, algebra, optimization, TSP
- **LogicSolver**: Truth tables, deduction, riddles
- **SpatialSolver**: 3D geometry, cube problems, navigation
- **SequenceSolver**: Pattern recognition, progressions

### 3. Reasoning Execution
Executes reasoning steps sequentially:
- Symbolic computation (SymPy)
- Rule-based logic
- Heuristic search
- Pattern matching

### 4. Verification & Correction
Validates reasoning and applies corrections:
- Numerical consistency checks
- Logical consistency verification
- Domain-specific validation
- Heuristic correction strategies

### 5. Trace Logging
Maintains complete reasoning trace:
- Step-by-step decisions
- Intermediate results
- Verification warnings
- Final predictions

---

## 📊 Evaluation

### Metrics

The system is evaluated on:
- **Accuracy**: Percentage of correct predictions
- **Topic-wise Performance**: Breakdown by problem type
- **Consistency**: Verification pass rate

### Viewing Results

After running the pipeline, check:

1. **Console Output**: Real-time progress and summary
2. **HTML Report**: `reports/reasoning_report_*.html` - Interactive visualization
3. **CSV Summary**: `reports/reasoning_summary_*.csv` - Tabular data
4. **JSON Traces**: `reports/reasoning_traces_*.json` - Complete traces

---

## 🔧 Customization

### Adjusting Training Size

Edit `main.py`:
```python
pipeline.run_full_pipeline(
    train_samples=100,  # Change this number
    generate_test_predictions=True
)
```

### Adding Custom Solvers

1. Create solver in `solver.py`:
```python
class CustomSolver:
    def solve(self, problem):
        # Your logic here
        return result
```

2. Integrate in `reasoning_agent.py`:
```python
self.custom_solver = CustomSolver()
```

### Modifying Verification Rules

Edit `verifier.py` to add custom verification logic:
```python
def verify_custom_rule(self, problem, prediction):
    # Your verification logic
    return is_valid
```

---

## 🎯 Reasoning Strategies

### For Optimization Problems
1. Extract all constraints
2. Identify optimization objective (min/max)
3. Evaluate feasible solutions
4. Apply greedy or exhaustive search

### For Spatial Problems
1. Visualize the spatial configuration
2. Extract dimensions and positions
3. Apply geometric formulas
4. Validate against physical constraints

### For Sequence Problems
1. Extract numerical sequence
2. Test common patterns (arithmetic, geometric, recursive)
3. Apply polynomial fitting if needed
4. Verify prediction consistency

### For Logic Problems
1. Extract logical statements
2. Build truth tables
3. Apply deductive reasoning
4. Check for contradictions

---

## 📈 Performance Tips

1. **Start Small**: Test with 50 training samples first
2. **Monitor Traces**: Check HTML reports for reasoning quality
3. **Adjust Heuristics**: Modify verifier rules based on performance
4. **Topic Analysis**: Focus improvements on weak topic areas

---

## 🐛 Troubleshooting

### Issue: Import Errors
```bash
pip install --upgrade -r requirements.txt
```

### Issue: Low Accuracy on Specific Topics
- Check reasoning traces for that topic
- Adjust solver logic in `solver.py`
- Add topic-specific rules in `reasoning_agent.py`

### Issue: Memory Errors
- Reduce `train_samples` parameter
- Process test set in batches
- Close other applications

---

## 📚 Dependencies

Core libraries:
- `pandas` - Data manipulation
- `numpy` - Numerical operations
- `sympy` - Symbolic mathematics
- `transformers` - (Optional) Small language models
- `scikit-learn` - ML utilities
- `tqdm` - Progress bars

Full list in `requirements.txt`

---

## 🏆 Hackathon Submission

### Final Submission Checklist

- [ ] Run full pipeline with all 534 training examples
- [ ] Generate predictions for all 101 test examples
- [ ] Review HTML report for quality check
- [ ] Verify `predictions.csv` format matches `output.csv`
- [ ] Prepare 3-5 minute demo
- [ ] Document novel approaches in report

### Demo Script

1. **Show Problem Example** (30 sec)
   - Display a complex problem
   
2. **Show Decomposition** (60 sec)
   - How Solvra breaks it down
   
3. **Show Step-by-Step Reasoning** (90 sec)
   - Walk through reasoning trace
   
4. **Show Verification** (30 sec)
   - How system self-corrects
   
5. **Show Results** (30 sec)
   - Accuracy metrics and insights

---

## 🎨 Novel Features

1. **Hybrid Reasoning**: Combines symbolic + rule-based + heuristic approaches
2. **Self-Verification**: Built-in consistency checking and correction
3. **Explainable AI**: Complete reasoning trace for every decision
4. **Modular Design**: Easy to extend with new reasoning modules
5. **No Black Box**: Full transparency in decision-making

---

## 🤝 Contributing

For Ethos 2025 team members:

1. Create feature branch
2. Implement changes
3. Test thoroughly
4. Update documentation
5. Submit for review

---

## 📝 License

This project is created for the Ethos 2025 hackathon.

---

## 👥 Team

**Project**: Solvra  
**Challenge**: Ethos 2025 – Saptang Labs ML Challenge  
**Category**: Agentic Reasoning System

---

## 🎓 Technical Report

For detailed technical documentation, see `reports/technical_report.md` (generated after running pipeline).

Key sections:
- System Architecture
- Reasoning Strategies  
- Evaluation Results
- Novel Contributions
- Challenges & Solutions

---

## 📞 Support

For issues or questions:
1. Check reasoning traces in `reports/`
2. Review this README
3. Examine code comments in `src/`

---

## 🚀 Next Steps

1. **Run Initial Test**: `python src/main.py` with 50 samples
2. **Analyze Results**: Check HTML report
3. **Iterate**: Improve based on weak areas
4. **Full Run**: Use all 534 training samples
5. **Submit**: Generate final predictions

---

**Good luck with Ethos 2025! 🏆**

*Built with ❤️ for logical reasoning and explainable AI*
