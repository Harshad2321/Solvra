# Solvra - Agentic Reasoning System# Solvra - Agentic Reasoning System



Ethos 2025 – Saptang Labs Machine Learning Challenge**Ethos 2025 – Saptang Labs Machine Learning Challenge**



## What is this?An advanced modular reasoning system that solves logic-based problems through autonomous problem decomposition, intelligent tool selection, and step-by-step reasoning.



This is our submission for the Ethos 2025 ML Challenge. We built a system that can solve different types of reasoning problems by breaking them down into smaller steps and using specialized solvers for each type.[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

[![Accuracy](https://img.shields.io/badge/accuracy-96%25-brightgreen)](PERFORMANCE_METRICS.md)

## Documentation[![F1 Score](https://img.shields.io/badge/F1--Score-95.71%25-brightgreen)](PERFORMANCE_METRICS.md)



- [Executive Summary](EXECUTIVE_SUMMARY.md) - Quick overview of our approach## 📚 Documentation

- [Performance Metrics](PERFORMANCE_METRICS.md) - How well our system performs

- [Submission Summary](SUBMISSION_SUMMARY.md) - Key points about our submission- **[Technical Report](TECHNICAL_REPORT.md)** - Complete 18-page technical documentation

- **[Executive Summary](EXECUTIVE_SUMMARY.md)** - Quick 2-page overview

## Project Overview- **[Performance Metrics](PERFORMANCE_METRICS.md)** - Detailed performance analysis



Solvra is a reasoning system designed to solve various types of logic problems including:---



- Optimization and planning problems## 🎯 Project Overview

- Spatial reasoning (3D geometry, navigation)

- Sequence solving (finding patterns and progressions)Solvra is an **Agentic Reasoning System** designed to tackle diverse reasoning challenges including:

- Operation of mechanisms (gears, machines, etc.)

- Classic riddles and lateral thinking- ✅ Optimization and planning

- Logical traps and deduction puzzles- ✅ Spatial reasoning (3D geometry, navigation)

- ✅ Sequence solving (patterns, progressions)

## Performance Results- ✅ Operation of mechanisms (gears, machines)

- ✅ Classic riddles and lateral thinking

- Accuracy: 96% on training set- ✅ Logical traps and deduction

- F1 Score: 95.71% (Macro)

- Processing speed: 8,534 problems/second### Performance Highlights

- Complete reasoning traces for every decision

- 🎯 **96% Accuracy** on training set

## Key Features- 📊 **95.71% F1 Score** (Macro)

- ⚡ **8,534 problems/second** throughput

- **Modular Architecture**: Different solvers for different problem types- 📝 **Complete reasoning traces** for every decision

- **Problem Decomposition**: Breaks complex problems into smaller parts

- **Tool Selection**: Picks the right solver for each problem### Key Features

- **Verification System**: Checks answers and fixes mistakes

- **Explainable Reasoning**: You can see how it arrived at each answer🧩 **Modular Architecture**: Specialized solvers for different reasoning types  

- **ML Enhancement**: Learns from training data while staying explainable🔍 **Problem Decomposition**: Breaks complex problems into manageable subproblems  

🛠️ **Tool Selection**: Intelligently selects appropriate reasoning engines  

## How It Works✔️ **Verification System**: Validates and corrects reasoning steps  

📝 **Explainable Reasoning**: Complete trace of decision-making process  

Our system follows these steps:🤖 **ML Enhancement**: Learns from training data without losing explainability



1. **Preprocessing**: Extracts features and identifies what type of problem it is## About This Project

2. **Pattern Matching**: Recognizes over 65 common problem patterns

3. **Reasoning Agent**: Breaks the problem down into stepsThis is our submission for the Ethos 2025 ML Challenge. We built a system that can solve different types of reasoning problems using:

4. **Specialized Solvers**: Uses the right strategy for each problem type

5. **Verification**: Double-checks the solution and corrects errors1. **Preprocessing**: Extract features and identify problem types

6. **ML Enhancement**: Learns patterns from the training data2. **Pattern Matching**: Recognize 65+ common problem patterns

3. **Reasoning Agent**: Break down problems into steps

## Project Structure4. **Specialized Solvers**: Apply domain-specific strategies

5. **Verification**: Self-check and correct solutions

```6. **ML Enhancement**: Learn patterns from training data

Solvra/

├── data/## Project Structure

│   ├── train.csv              # Training data (384 examples)

│   ├── test.csv               # Test data (96 examples)```

│   ├── predictions.csv        # Our predictionsSolvra/

│   └── output.csv             # Expected output format├── data/                    # Dataset files

├── src/│   ├── train.csv           # Training data (384 examples)

│   ├── main.py                # Main script to run everything│   ├── test.csv            # Test data (96 examples)  

│   ├── preprocess.py          # Data preprocessing

│   ├── reasoning_agent.py     # Main reasoning logic│   └── output.csv          # Output format🛠️ **Tool Selection**: Intelligently selects appropriate reasoning engines  

│   ├── solver.py              # Problem solvers

│   ├── verifier.py            # Solution verification│✔️ **Verification System**: Validates and corrects reasoning steps  

│   ├── pattern_matcher.py     # Pattern recognition

│   ├── ml_enhancer.py         # ML components├── src/                    # Source code📝 **Explainable Reasoning**: Complete trace of decision-making process  

│   └── trace_logger.py        # Logging utilities

├── reports/│   ├── main.py            # Main script to run everything🚫 **No Proprietary LLMs**: Uses symbolic reasoning + small open models

│   ├── reasoning_traces_*.json    # Detailed reasoning traces

│   ├── reasoning_summary_*.csv    # Summary statistics│   ├── preprocess.py      # Data preprocessing

│   └── performance_metrics.txt    # Performance results

└── requirements.txt           # Python dependencies│   ├── reasoning_agent.py # Main reasoning logic---

```

│   ├── solver.py          # Problem solvers

## Getting Started

│   ├── verifier.py        # Solution verification## 📁 Project Structure

### Requirements

│   ├── pattern_matcher.py # Pattern recognition

- Python 3.10 or higher

- pip package manager│   ├── ml_enhancer.py     # ML components```

- 4GB+ RAM recommended

│   └── trace_logger.py    # Logging utilitiesSolvra/

### Installation

│├── data/                          # Dataset directory

1. Clone or navigate to the project directory:

```bash└── requirements.txt       # Python dependencies│   ├── train.csv                  # Training data (534 examples)

cd Solvra

``````│   ├── test.csv                   # Test data (101 examples)



2. Create a virtual environment (optional but recommended):│   ├── output.csv                 # Expected output format

```bash

# Windows## Getting Started│   └── predictions.csv            # Generated predictions

python -m venv venv

venv\Scripts\activate│



# Linux/Mac### Installation├── src/                           # Source code

python -m venv venv

source venv/bin/activate│   ├── preprocess.py             # Data preprocessing & feature extraction

```

1. Clone this repository│   ├── reasoning_agent.py        # Main reasoning orchestrator

3. Install dependencies:

```bash2. Install dependencies:│   ├── solver.py                 # Specialized solving engines

pip install -r requirements.txt

``````bash│   ├── verifier.py               # Reasoning verification & correction



### Running the Codepip install -r requirements.txt│   ├── trace_logger.py           # Logging & explainability



To train and generate predictions:```│   └── main.py                   # Main pipeline orchestrator



```bash│

cd src

python main.py### Running the Code├── models/                        # Model storage (for future ML components)

```

├── reports/                       # Generated reports & traces

This will:

- Load and preprocess the training dataTo train and generate predictions:│   ├── reasoning_traces_*.json   # Detailed reasoning traces

- Train the reasoning system

- Generate predictions for the test data```bash│   ├── reasoning_summary_*.csv   # Summary statistics

- Save results to `data/predictions.csv`

- Create detailed reports in the `reports/` folderpython src/main.py│   └── reasoning_report_*.html   # Interactive HTML report



## System Architecture```│



### 1. Problem Decomposition├── requirements.txt              # Python dependencies

The system breaks down complex problems into smaller subproblems:

- Extracts constraints and objectivesThis will:└── README.md                     # This file

- Identifies problem type (math, spatial, logic, etc.)

- Creates an execution plan- Load and preprocess the training data```



### 2. Tool Selection- Train the reasoning system

Picks the appropriate solver based on problem type:

- **MathSolver**: For arithmetic, algebra, optimization problems- Generate predictions for test data---

- **LogicSolver**: For truth tables, deduction, riddles

- **SpatialSolver**: For 3D geometry and navigation problems- Save results to `data/predictions.csv`

- **SequenceSolver**: For pattern recognition and progressions

## 🚀 Getting Started

### 3. Reasoning Execution

Executes reasoning steps one by one:## Requirements

- Uses symbolic computation (SymPy library)

- Applies rule-based logic### Quick Start - Web UI

- Uses heuristic search when needed

- Matches against known patterns- Python 3.8+



### 4. Verification and Correction- pandasThe easiest way to use Solvra:

Checks the reasoning and fixes errors:

- Verifies numerical consistency- numpy

- Checks logical consistency

- Validates against domain-specific rules- scikit-learn```bash

- Applies heuristic corrections

- Other dependencies in `requirements.txt`# Install dependencies

### 5. Trace Logging

Keeps track of the entire reasoning process:pip install -r requirements.txt

- Records each decision step

- Saves intermediate results## Approach

- Logs verification warnings

- Documents final predictions# Launch web interface



## Our ApproachWe tried different approaches and combined what worked best:streamlit run app.py



We tried different approaches and combined what worked best:```



1. **Pattern Recognition**: Many problems follow common patterns, so we built a pattern matcher to recognize these quickly.1. **Pattern Recognition**: We noticed that many problems follow common patterns, so we built a pattern matcher to recognize these



2. **Rule-Based Reasoning**: For logic and math problems, we use symbolic computation and predefined rules.2. **Rule-Based Reasoning**: For logic and math problems, we use symbolic computation and rulesThen open `http://localhost:8501` in your browser!



3. **Verification**: We added a verification step to catch obvious mistakes before finalizing answers.3. **Verification**: We added a verification step to catch obvious mistakes



4. **ML Enhancement**: We use machine learning for pattern recognition where pure rules don't work well.4. **ML Enhancement**: We use machine learning for pattern recognition where rules don't work well### Prerequisites



## Evaluation Metrics



The system is evaluated on:## Results- Python 3.10 or higher

- **Accuracy**: Percentage of correct predictions

- **Topic-wise Performance**: How well it does on each problem type- pip package manager

- **Consistency**: How often it passes verification checks

Our system works pretty well on the validation set. Different problem types have different accuracy:- 4GB+ RAM recommended

### Viewing Results

- Sequence problems: Good performance with pattern matching

After running the code, you can check:

- Logic puzzles: Rule-based approach works well### Installation

1. **Console Output**: Shows progress and final summary

2. **CSV Summary**: `reports/reasoning_summary_*.csv` - All results in a table- Spatial reasoning: Still improving this part

3. **JSON Traces**: `reports/reasoning_traces_*.json` - Complete reasoning traces

4. **Performance Metrics**: `reports/performance_metrics.txt` - Detailed metrics1. **Clone or navigate to the project directory**:



## Reasoning Strategies by Problem Type## Challenges We Faced```bash



### Optimization Problemscd Solvra

1. Extract all constraints from the problem

2. Identify what we're trying to minimize or maximize- Some problems need multiple reasoning steps which is tricky to handle```

3. Evaluate all feasible solutions

4. Use greedy or exhaustive search- Spatial reasoning problems are harder than we thought



### Spatial Problems- Balancing rule-based and ML approaches took some experimentation2. **Create a virtual environment** (recommended):

1. Visualize the spatial configuration

2. Extract dimensions and positions```bash

3. Apply geometric formulas

4. Check against physical constraints## Teampython -m venv venv



### Sequence Problems

1. Extract the numerical sequence

2. Test common patterns (arithmetic, geometric, recursive)Made by two students for the Ethos 2025 challenge.# Windows

3. Use polynomial fitting if simple patterns don't work

4. Verify the prediction makes sensevenv\Scripts\activate



### Logic Problems## Acknowledgments

1. Extract logical statements

2. Build truth tables# Linux/Mac

3. Apply deductive reasoning

4. Check for contradictionsThanks to Saptang Labs for organizing this challenge!source venv/bin/activate



## Customization```



### Changing Training Size3. **Install dependencies**:

```bash

Edit `main.py`:pip install -r requirements.txt

```python```

pipeline.run_full_pipeline(

    train_samples=100,  # Change this number4. **Download spaCy model** (if using NLP features):

    generate_test_predictions=True```bash

)python -m spacy download en_core_web_sm

``````



### Adding Custom Solvers---



1. Create a new solver in `solver.py`## 🎮 Usage

2. Integrate it in `reasoning_agent.py`

3. Add test cases to verify it works### Quick Start - Run Full Pipeline



### Modifying Verification Rules```bash

cd src

Edit `verifier.py` to add custom verification logic based on your observations.python main.py

```

## Performance Tips

This will:

1. Start with a small number of training samples (like 50) to test quickly1. Load and preprocess data

2. Check the reasoning traces to see if the logic makes sense2. Analyze training examples

3. Focus improvements on topics where accuracy is lower3. Generate predictions for test set

4. Monitor memory usage if processing large datasets4. Create detailed reports and traces



## Dependencies### Step-by-Step Usage



Main libraries we use:#### 1. Data Preprocessing

- `pandas` - For data manipulation

- `numpy` - For numerical operations```python

- `sympy` - For symbolic mathematicsfrom preprocess import DataPreprocessor

- `scikit-learn` - For ML utilities

- `tqdm` - For progress barspreprocessor = DataPreprocessor(data_dir="../data")

- `colorama` - For colored console outputtrain_df, test_df = preprocessor.load_data()

train_df = preprocessor.preprocess_training_data()

Full list is in `requirements.txt`test_df = preprocessor.preprocess_test_data()

```

## Challenges We Faced

#### 2. Reasoning on a Single Problem

- Some problems need multiple reasoning steps which is tricky to handle correctly

- Spatial reasoning problems were harder than we initially thought```python

- Balancing rule-based and ML approaches took experimentationfrom reasoning_agent import ReasoningAgent

- Getting the verification system to not be too strict or too lenient

agent = ReasoningAgent()

## Results by Problem Type

problem = {

Different problem types have different accuracy levels:    'topic': 'Sequence solving',

- Sequence problems: Good performance with pattern matching    'problem_statement': 'Find next: 2, 5, 10, 17, 26, ?',

- Logic puzzles: Rule-based approach works well    'answer_option_1': '35',

- Spatial reasoning: Still working on improving this    'answer_option_2': '37',

- Optimization: Works well for small search spaces    # ... other options

}

## What Makes Our System Different

prediction, trace = agent.reason_step_by_step(problem)

1. **Hybrid Reasoning**: Combines symbolic reasoning, rules, and MLprint(f"Predicted: Option {prediction}")

2. **Self-Verification**: Built-in checking and error correctionprint(agent.get_trace_summary())

3. **Explainable**: Complete reasoning trace for every decision```

4. **Modular Design**: Easy to add new reasoning modules

5. **No Black Box**: You can see exactly how it arrives at answers#### 3. Running with Verification



## Troubleshooting```python

from reasoning_agent import ReasoningAgent

### Import Errorsfrom verifier import ReasoningVerifier

```bash

pip install --upgrade -r requirements.txtagent = ReasoningAgent()

```verifier = ReasoningVerifier()



### Low Accuracy on Specific Topicsprediction, trace = agent.reason_step_by_step(problem)

- Check reasoning traces for that topic in the reports foldercorrected = verifier.apply_correction_heuristics(problem, prediction, trace)

- Adjust solver logic in `solver.py`print(verifier.get_verification_report())

- Add topic-specific rules in `reasoning_agent.py````



### Memory Errors---

- Reduce the `train_samples` parameter

- Process test set in smaller batches## 🧠 System Architecture

- Close other applications

### 1. Problem Decomposition

## Future ImprovementsThe system breaks down complex problems into smaller, manageable subproblems:

- Extract constraints and objectives

Things we want to work on:- Identify problem type (math, spatial, logic, etc.)

- Better handling of spatial reasoning problems- Create execution plan

- Add more pattern types to the pattern matcher

- Clean up the verification logic for edge cases### 2. Tool Selection

- Split up solver.py since it's getting longIntelligently selects the appropriate solver:

- Add more comprehensive test cases- **MathSolver**: Arithmetic, algebra, optimization, TSP

- **LogicSolver**: Truth tables, deduction, riddles

## Team- **SpatialSolver**: 3D geometry, cube problems, navigation

- **SequenceSolver**: Pattern recognition, progressions

Made by students for the Ethos 2025 challenge.

### 3. Reasoning Execution

## AcknowledgmentsExecutes reasoning steps sequentially:

- Symbolic computation (SymPy)

Thanks to Saptang Labs for organizing this challenge and providing an interesting problem set!- Rule-based logic

- Heuristic search

## License- Pattern matching



This project is created for the Ethos 2025 hackathon.### 4. Verification & Correction

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
