# 🤖 Solvra - Agentic Reasoning System

[![Ethos 2025](https://img.shields.io/badge/Ethos-2025-blue)](https://github.com/Harshad2321/Solvra)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Solvra** is an explainable agentic reasoning system designed for the **Ethos 2025 – Saptang Labs ML Challenge**. Unlike black-box AI models, Solvra solves complex reasoning problems through transparent, step-by-step logic using specialized reasoning modules.

🌐 **[View Live Demo](https://harshad2321.github.io/Solvra/)**

---

## ✨ Key Features

- 🧩 **Modular Architecture** - Four specialized solvers for different problem types
- 🔍 **Complete Transparency** - Every decision is logged and traceable
- ✅ **Self-Verification** - Built-in error checking and correction
- 🚫 **No Proprietary LLMs** - Uses symbolic math and rule-based logic
- ⚡ **Fast & Efficient** - Runs locally without GPU requirements
- 📊 **Rich Reporting** - Generates detailed HTML reports

---

## 🎯 Problem Types Solved

| Type | Examples |
|------|----------|
| **Optimization** | Task scheduling, resource allocation, TSP |
| **Spatial Reasoning** | 3D cube problems, navigation, geometry |
| **Sequence Solving** | Pattern recognition, progressions |
| **Logic Puzzles** | Truth-teller/liar, deduction, riddles |
| **Classic Riddles** | Lateral thinking problems |
| **Operations** | Mechanism understanding |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- pip package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/Harshad2321/Solvra.git
cd Solvra

# Install dependencies
pip install -r requirements.txt
```

### Run Solvra

```bash
# Navigate to source directory
cd src

# Run the main pipeline
python main.py
```

This will:
1. Load and preprocess data (384 training + 96 test examples)
2. Analyze training examples
3. Generate predictions for test set
4. Create detailed HTML reports in `reports/`
5. Save predictions to `data/predictions.csv`

### View Results

Open `reports/reasoning_report_*.html` in your browser to see:
- Complete reasoning traces
- Step-by-step explanations
- Performance metrics
- Topic-wise analysis

---

## 📁 Project Structure

```
Solvra/
├── data/                      # Dataset files
│   ├── train.csv             # 384 training examples
│   ├── test.csv              # 96 test examples
│   └── predictions.csv       # Generated predictions
├── src/                      # Source code
│   ├── preprocess.py         # Data preprocessing
│   ├── solver.py             # Specialized solvers
│   ├── reasoning_agent.py    # Main orchestrator
│   ├── verifier.py           # Verification system
│   ├── trace_logger.py       # Logging & reporting
│   ├── main.py               # Pipeline runner
│   ├── demo.py               # Interactive demo
│   └── test_interactive.py   # Debug tool
├── reports/                  # Generated reports
├── models/                   # Model storage
├── docs/                     # GitHub Pages website
└── README.md                 # This file
```

---

## 🏗️ Architecture

```
Input Problem
     ↓
Preprocessing (text cleaning, feature extraction)
     ↓
Reasoning Agent (problem decomposition, tool selection)
     ↓
┌────────────────────────────────────┐
│  Specialized Solvers               │
│  • MathSolver    • LogicSolver    │
│  • SpatialSolver • SequenceSolver │
└────────────────────────────────────┘
     ↓
Verifier (consistency checking, correction)
     ↓
Output + Reasoning Trace
```

### Core Components

1. **Preprocessing** - Extracts numbers, patterns, and problem characteristics
2. **Reasoning Agent** - Decomposes problems and coordinates solving
3. **Specialized Solvers**:
   - **MathSolver**: Optimization, TSP, rate problems (uses SymPy)
   - **LogicSolver**: Deduction, truth tables, riddles
   - **SpatialSolver**: 3D geometry, cube analysis, navigation
   - **SequenceSolver**: Pattern recognition (arithmetic, geometric, recursive)
4. **Verifier** - Validates answers and applies corrections
5. **Trace Logger** - Logs every reasoning step for explainability

---

## 🎬 Demo

### Run Interactive Demo

```bash
cd src
python demo.py
```

This shows a 3-5 minute interactive demonstration of:
- Sequence problem solving with step-by-step reasoning
- Spatial reasoning (3D cube problem)
- Optimization (task scheduling)

### Example: Sequence Problem

**Problem**: Find the next number: `2, 5, 10, 17, 26, ?`

**Solvra's Reasoning**:
1. **Extract**: Numbers = [2, 5, 10, 17, 26]
2. **Analyze**: Differences = [3, 5, 7, 9] → increasing by 2
3. **Predict**: Next difference = 11 → Answer = 37
4. **Verify**: ✓ Pattern consistent

**Answer**: 37

---

## 📊 Performance

- **Training Examples**: 384
- **Test Examples**: 96
- **Processing Speed**: 1-2 seconds per problem
- **Memory Usage**: <1GB
- **Verification Pass Rate**: ~85%

### Topic-wise Coverage

- Spatial reasoning: 94 examples
- Optimization: 83 examples
- Operations: 64 examples
- Sequence solving: 62 examples
- Lateral thinking: 35 examples
- Classic riddles: 33 examples
- Logical traps: 13 examples

---

## 🛠️ Usage Examples

### Test Individual Problems

```bash
cd src
python test_interactive.py
```

Commands:
- `train 0` - Test training problem 0
- `test 0` - Test test problem 0
- `random` - Test random problem
- `quit` - Exit

### Customize Training Size

Edit `src/main.py` line 93:

```python
pipeline.run_full_pipeline(
    train_samples=100,  # Change this (max 384)
    generate_test_predictions=True
)
```

---

## 🔬 Technical Details

### Reasoning Strategies

**For Optimization**:
1. Extract constraints and objectives
2. Evaluate feasible solutions
3. Apply greedy or exhaustive search

**For Sequences**:
1. Extract numerical sequence
2. Test patterns (arithmetic, geometric, recursive)
3. Apply polynomial fitting if needed
4. Verify prediction consistency

**For Spatial**:
1. Visualize configuration
2. Extract dimensions
3. Apply geometric formulas
4. Validate constraints

**For Logic**:
1. Extract logical statements
2. Build truth tables
3. Apply deductive reasoning
4. Check contradictions

### Technologies Used

- **SymPy** - Symbolic mathematics
- **NumPy** - Numerical operations
- **Pandas** - Data manipulation
- **Pure Python** - Rule-based logic

---

## 📚 Documentation

- **[README.md](README.md)** - This file
- **[QUICKSTART.md](QUICKSTART.md)** - 5-minute setup guide
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - System design details
- **[PRESENTATION.md](PRESENTATION.md)** - Demo script & talking points
- **[STATUS.md](STATUS.md)** - Current status & next steps
- **[reports/technical_report.md](reports/technical_report.md)** - Technical analysis

---

## 🎯 What Makes Solvra Unique?

### vs GPT-4 / Claude
- ✅ **Transparent**: See every reasoning step
- ✅ **Local**: No API costs or internet needed
- ✅ **Reproducible**: Same input → same output
- ✅ **Debuggable**: Can trace and fix any error

### vs Rule-Based Systems
- ✅ **Flexible**: Handles diverse problem types
- ✅ **Self-Correcting**: Verification catches errors
- ✅ **Modular**: Easy to extend with new solvers

### vs Pure ML
- ✅ **Explainable**: No black box
- ✅ **Efficient**: No training required
- ✅ **Reliable**: Logic-based guarantees

---

## 🏆 Hackathon Submission

**Challenge**: Ethos 2025 – Saptang Labs ML Challenge  
**Category**: Agentic Reasoning System  
**Submission Files**:
- `data/predictions.csv` - Test set predictions
- `reports/` - Detailed reasoning traces & reports
- Complete source code with documentation

---

## 🤝 Contributing

This project was created for Ethos 2025. Feel free to:
- Report issues
- Suggest improvements
- Fork and extend

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details

---

## 👥 Authors

- **Harsh** - Creator & Developer
- Built for **Ethos 2025 – Saptang Labs ML Challenge**

---

## 🙏 Acknowledgments

- Ethos 2025 organizers
- Saptang Labs for the challenge
- Open-source community

---

## 📞 Contact

- **GitHub**: [@Harshad2321](https://github.com/Harshad2321)
- **Repository**: [Solvra](https://github.com/Harshad2321/Solvra)
- **Issues**: [Report Issues](https://github.com/Harshad2321/Solvra/issues)

---

<div align="center">

**🏆 Solvra - Transparent, Explainable, Effective**

[🌐 Live Demo](https://harshad2321.github.io/Solvra/) • [📚 Documentation](docs/) • [🚀 Get Started](#-quick-start)

*Built with ❤️ for transparent and explainable AI*

</div>
