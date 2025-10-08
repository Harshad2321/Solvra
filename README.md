# Solvra - Agentic Reasoning System# Solvra - Agentic Reasoning System# Solvra - Agentic Reasoning System



Ethos 2025 - Saptang Labs Machine Learning Challenge



## About This ProjectEthos 2025 – Saptang Labs Machine Learning Challenge**Ethos 2025 – Saptang Labs Machine Learning Challenge**



This is our submission for the Ethos 2025 ML Challenge. We built a system that solves different types of reasoning problems by breaking them down into smaller steps and using different solvers for each problem type.



The idea was to create something that can handle various kinds of logic puzzles - from math problems to spatial reasoning to riddles - without needing a huge language model. We wanted to keep it explainable so you can actually see how it arrives at each answer.## What is this?An advanced modular reasoning system that solves logic-based problems through autonomous problem decomposition, intelligent tool selection, and step-by-step reasoning.



## What Problems Does It Solve?



Our system can handle these types of problems:This is our submission for the Ethos 2025 ML Challenge. We built a system that can solve different types of reasoning problems by breaking them down into smaller steps and using specialized solvers for each type.[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)



- Optimization and planning (like scheduling or resource allocation)[![Accuracy](https://img.shields.io/badge/accuracy-96%25-brightgreen)](PERFORMANCE_METRICS.md)

- Spatial reasoning (3D geometry, navigation, cube problems)

- Sequence solving (finding patterns in numbers or sequences)## Documentation[![F1 Score](https://img.shields.io/badge/F1--Score-95.71%25-brightgreen)](PERFORMANCE_METRICS.md)

- Mechanism operations (gears, machines, how things work)

- Classic riddles and lateral thinking puzzles

- Logical traps and deduction problems

- [Executive Summary](EXECUTIVE_SUMMARY.md) - Quick overview of our approach## 📚 Documentation

## Performance

- [Performance Metrics](PERFORMANCE_METRICS.md) - How well our system performs

We tested it on the training data and got these results:

- [Submission Summary](SUBMISSION_SUMMARY.md) - Key points about our submission- **[Technical Report](TECHNICAL_REPORT.md)** - Complete 18-page technical documentation

- **Accuracy:** 96% (48 out of 50 correct)

- **F1 Score:** 95.71%- **[Executive Summary](EXECUTIVE_SUMMARY.md)** - Quick 2-page overview

- **Speed:** About 0.0002 seconds per problem

- **Throughput:** Around 8,500+ problems per second## Project Overview- **[Performance Metrics](PERFORMANCE_METRICS.md)** - Detailed performance analysis



Different problem types had different accuracy:

- Spatial reasoning: 100%

- Sequence solving: 100%Solvra is a reasoning system designed to solve various types of logic problems including:---

- Operations: 100%

- Lateral thinking: 100%

- Logic traps: 100%

- Optimization: 88.9%- Optimization and planning problems## 🎯 Project Overview

- Riddles: 83.3%

- Spatial reasoning (3D geometry, navigation)

We're still working on improving the riddle solving part.

- Sequence solving (finding patterns and progressions)Solvra is an **Agentic Reasoning System** designed to tackle diverse reasoning challenges including:

## How It Works

- Operation of mechanisms (gears, machines, etc.)

We built a pipeline with several components:

- Classic riddles and lateral thinking- ✅ Optimization and planning

1. **Preprocessing** - Cleans the data and extracts features from each problem

2. **Pattern Matching** - Checks if the problem matches any of 65+ known patterns- Logical traps and deduction puzzles- ✅ Spatial reasoning (3D geometry, navigation)

3. **Reasoning Agent** - Coordinates the whole solving process

4. **Specialized Solvers** - Different solvers for different problem types:- ✅ Sequence solving (patterns, progressions)

   - Math Solver (arithmetic, algebra, optimization)

   - Logic Solver (deduction, truth tables)## Performance Results- ✅ Operation of mechanisms (gears, machines)

   - Spatial Solver (3D geometry, navigation)

   - Sequence Solver (pattern recognition)- ✅ Classic riddles and lateral thinking

5. **Verifier** - Double-checks the answer and tries to catch mistakes

6. **ML Component** - Learns patterns from training data- Accuracy: 96% on training set- ✅ Logical traps and deduction



The system tries to pick the right tool for each problem and then verifies the answer makes sense before finalizing it.- F1 Score: 95.71% (Macro)



## Project Structure- Processing speed: 8,534 problems/second### Performance Highlights



```- Complete reasoning traces for every decision

Solvra/

├── data/- 🎯 **96% Accuracy** on training set

│   ├── train.csv              # Training data (384 problems)

│   ├── test.csv               # Test data (96 problems)## Key Features- 📊 **95.71% F1 Score** (Macro)

│   ├── predictions.csv        # Our predictions

│   └── output.csv             # Expected format- ⚡ **8,534 problems/second** throughput

│

├── src/- **Modular Architecture**: Different solvers for different problem types- 📝 **Complete reasoning traces** for every decision

│   ├── main.py                # Main script to run everything

│   ├── preprocess.py          # Data preprocessing- **Problem Decomposition**: Breaks complex problems into smaller parts

│   ├── reasoning_agent.py     # Coordinates the reasoning

│   ├── solver.py              # All the different solvers- **Tool Selection**: Picks the right solver for each problem### Key Features

│   ├── verifier.py            # Checks and corrects answers

│   ├── pattern_matcher.py     # Recognizes problem patterns- **Verification System**: Checks answers and fixes mistakes

│   ├── ml_enhancer.py         # Machine learning component

│   └── trace_logger.py        # Logs what the system is thinking- **Explainable Reasoning**: You can see how it arrived at each answer🧩 **Modular Architecture**: Specialized solvers for different reasoning types  

│

├── reports/- **ML Enhancement**: Learns from training data while staying explainable🔍 **Problem Decomposition**: Breaks complex problems into manageable subproblems  

│   ├── reasoning_traces_*.json    # Detailed logs of reasoning

│   ├── reasoning_summary_*.csv    # Summary of results🛠️ **Tool Selection**: Intelligently selects appropriate reasoning engines  

│   └── performance_metrics.txt    # Performance numbers

│## How It Works✔️ **Verification System**: Validates and corrects reasoning steps  

└── requirements.txt           # Python packages needed

```📝 **Explainable Reasoning**: Complete trace of decision-making process  



## Getting StartedOur system follows these steps:🤖 **ML Enhancement**: Learns from training data without losing explainability



### Requirements



- Python 3.10 or higher1. **Preprocessing**: Extracts features and identifies what type of problem it is## About This Project

- About 4GB of RAM

- The packages listed in requirements.txt2. **Pattern Matching**: Recognizes over 65 common problem patterns



### Installation3. **Reasoning Agent**: Breaks the problem down into stepsThis is our submission for the Ethos 2025 ML Challenge. We built a system that can solve different types of reasoning problems using:



1. Navigate to the project folder:4. **Specialized Solvers**: Uses the right strategy for each problem type

```bash

cd Solvra5. **Verification**: Double-checks the solution and corrects errors1. **Preprocessing**: Extract features and identify problem types

```

6. **ML Enhancement**: Learns patterns from the training data2. **Pattern Matching**: Recognize 65+ common problem patterns

2. Install the required packages:

```bash3. **Reasoning Agent**: Break down problems into steps

pip install -r requirements.txt

```## Project Structure4. **Specialized Solvers**: Apply domain-specific strategies



That's it. No API keys or special setup needed.5. **Verification**: Self-check and correct solutions



### Running the Code```6. **ML Enhancement**: Learn patterns from training data



To generate predictions:Solvra/



```bash├── data/## Project Structure

cd src

python main.py│   ├── train.csv              # Training data (384 examples)

```

│   ├── test.csv               # Test data (96 examples)```

This will:

- Load and preprocess the data│   ├── predictions.csv        # Our predictionsSolvra/

- Train on the training examples

- Generate predictions for the test set│   └── output.csv             # Expected output format├── data/                    # Dataset files

- Save everything to `data/predictions.csv`

- Create detailed reports in the `reports/` folder├── src/│   ├── train.csv           # Training data (384 examples)



The whole thing takes less than a minute to run.│   ├── main.py                # Main script to run everything│   ├── test.csv            # Test data (96 examples)  



## Our Approach│   ├── preprocess.py          # Data preprocessing



We tried a few different approaches before settling on this one:│   ├── reasoning_agent.py     # Main reasoning logic│   └── output.csv          # Output format🛠️ **Tool Selection**: Intelligently selects appropriate reasoning engines  



### What We Tried│   ├── solver.py              # Problem solvers



1. **Pure Rule-Based** - We started with just rules and pattern matching. It worked okay but wasn't flexible enough.│   ├── verifier.py            # Solution verification│✔️ **Verification System**: Validates and corrects reasoning steps  



2. **Pure Machine Learning** - We tried using just ML models but they weren't very accurate with our small dataset and you couldn't see why they made certain decisions.│   ├── pattern_matcher.py     # Pattern recognition



3. **Hybrid Approach** (what we ended up with) - We combined pattern matching, symbolic reasoning, and ML. This gave us the best accuracy while keeping things explainable.│   ├── ml_enhancer.py         # ML components├── src/                    # Source code📝 **Explainable Reasoning**: Complete trace of decision-making process  



### Key Ideas│   └── trace_logger.py        # Logging utilities



**Pattern Library:** We noticed many problems follow common patterns. For example, sequence problems often use arithmetic or geometric progressions. We built a library of 65+ patterns.├── reports/│   ├── main.py            # Main script to run everything🚫 **No Proprietary LLMs**: Uses symbolic reasoning + small open models



**Symbolic Math:** For math problems, we use the SymPy library to get exact answers instead of approximations. This eliminates rounding errors.│   ├── reasoning_traces_*.json    # Detailed reasoning traces



**Verification:** We added a verification step that catches obvious mistakes. For example, if an answer is supposed to be between 1 and 5 but we calculated 7, the verifier catches it.│   ├── reasoning_summary_*.csv    # Summary statistics│   ├── preprocess.py      # Data preprocessing



**Explainability:** Every decision is logged so you can trace through the reasoning. This helped us debug problems and understand where we were making mistakes.│   └── performance_metrics.txt    # Performance results



## System Architecture└── requirements.txt           # Python dependencies│   ├── reasoning_agent.py # Main reasoning logic---



### 1. Problem Decomposition```



When a problem comes in, we:│   ├── solver.py          # Problem solvers

- Extract the key information (numbers, constraints, objectives)

- Identify what type of problem it is## Getting Started

- Create a plan for solving it

│   ├── verifier.py        # Solution verification## 📁 Project Structure

### 2. Solver Selection

### Requirements

Based on the problem type, we pick the right solver:

- **Math problems** -> Math Solver (uses SymPy for symbolic computation)│   ├── pattern_matcher.py # Pattern recognition

- **Logic puzzles** -> Logic Solver (builds truth tables)

- **Spatial problems** -> Spatial Solver (geometric formulas)- Python 3.10 or higher

- **Sequences** -> Sequence Solver (pattern detection)

- pip package manager│   ├── ml_enhancer.py     # ML components```

### 3. Reasoning Process

- 4GB+ RAM recommended

The solver works through the problem step by step:

- Applies domain-specific strategies│   └── trace_logger.py    # Logging utilitiesSolvra/

- Uses heuristics where exact solutions aren't possible

- Keeps track of intermediate steps### Installation



### 4. Verification│├── data/                          # Dataset directory



Before finalizing an answer:1. Clone or navigate to the project directory:

- Check if it's in the valid range

- Verify logical consistency```bash└── requirements.txt       # Python dependencies│   ├── train.csv                  # Training data (534 examples)

- Apply domain-specific checks

- Try to correct obvious errorscd Solvra



### 5. Logging``````│   ├── test.csv                   # Test data (101 examples)



Everything gets logged:

- Which solver was used

- What steps were taken2. Create a virtual environment (optional but recommended):│   ├── output.csv                 # Expected output format

- Why certain decisions were made

- Any warnings or corrections```bash



## Example# Windows## Getting Started│   └── predictions.csv            # Generated predictions



Here's how it solves a simple sequence problem:python -m venv venv



**Problem:** "Find the next number: 2, 5, 10, 17, 26, ?"venv\Scripts\activate│



**Solvra's process:**

1. Extracts the sequence: [2, 5, 10, 17, 26]

2. Calculates differences: [3, 5, 7, 9]# Linux/Mac### Installation├── src/                           # Source code

3. Notices the differences increase by 2 each time

4. Predicts next difference: 11python -m venv venv

5. Calculates answer: 26 + 11 = 37

6. Verifies it makes sensesource venv/bin/activate│   ├── preprocess.py             # Data preprocessing & feature extraction



**Answer:** 37```

**Time:** 0.0002 seconds

1. Clone this repository│   ├── reasoning_agent.py        # Main reasoning orchestrator

## Challenges We Faced

3. Install dependencies:

Some things that were harder than we expected:

```bash2. Install dependencies:│   ├── solver.py                 # Specialized solving engines

1. **Spatial Reasoning** - These problems are tricky because you need to visualize 3D shapes and transformations. We're still working on improving this.

pip install -r requirements.txt

2. **Ambiguous Problems** - Some problems can be interpreted in multiple ways. We had to add logic to pick the most reasonable interpretation.

``````bash│   ├── verifier.py               # Reasoning verification & correction

3. **Riddles** - These often require lateral thinking that doesn't follow normal patterns. Our accuracy here is lower (83%) compared to other problem types.



4. **Small Dataset** - With only 384 training examples, we couldn't rely purely on ML. That's why we focused on patterns and rules.

### Running the Codepip install -r requirements.txt│   ├── trace_logger.py           # Logging & explainability

5. **Speed vs Accuracy** - We had to balance thorough checking (which takes time) with fast inference. We optimized the critical paths.



## What Makes This Different

To train and generate predictions:```│   └── main.py                   # Main pipeline orchestrator

Most approaches either:

- Use big language models (expensive, not always accurate, hard to explain)

- Use pure ML (needs lots of data, black box)

- Use pure rules (rigid, doesn't generalize well)```bash│



We combined the best of all three:cd src

- Pattern matching for common cases

- Symbolic reasoning for exact problemspython main.py### Running the Code├── models/                        # Model storage (for future ML components)

- ML for learning from examples

- Complete explainability through logging```



## Technical Details├── reports/                       # Generated reports & traces



### Pattern MatchingThis will:



We implemented patterns for:- Load and preprocess the training dataTo train and generate predictions:│   ├── reasoning_traces_*.json   # Detailed reasoning traces

- Arithmetic sequences (constant difference)

- Geometric sequences (constant ratio)- Train the reasoning system

- Polynomial sequences

- Fibonacci-like sequences- Generate predictions for the test data```bash│   ├── reasoning_summary_*.csv   # Summary statistics

- Spatial transformations

- Common riddle structures- Save results to `data/predictions.csv`



### Symbolic Computation- Create detailed reports in the `reports/` folderpython src/main.py│   └── reasoning_report_*.html   # Interactive HTML report



Using SymPy, we can solve:

- Algebraic equations

- Optimization problems## System Architecture```│

- Geometric calculations

- Number theory problems



### Machine Learning### 1. Problem Decomposition├── requirements.txt              # Python dependencies



We use scikit-learn for:The system breaks down complex problems into smaller subproblems:

- Feature engineering

- Pattern classification- Extracts constraints and objectivesThis will:└── README.md                     # This file

- Confidence estimation

- Ensemble predictions- Identifies problem type (math, spatial, logic, etc.)



### Verification Rules- Creates an execution plan- Load and preprocess the training data```



We check for:

- Answer in valid range (1-5)

- Numerical consistency### 2. Tool Selection- Train the reasoning system

- Logical contradictions

- Domain-specific constraintsPicks the appropriate solver based on problem type:



## Files Generated- **MathSolver**: For arithmetic, algebra, optimization problems- Generate predictions for test data---



After running the code, you'll get:- **LogicSolver**: For truth tables, deduction, riddles



1. **predictions.csv** - Your final predictions in the required format- **SpatialSolver**: For 3D geometry and navigation problems- Save results to `data/predictions.csv`

2. **reasoning_traces_[timestamp].json** - Detailed logs of every decision

3. **reasoning_summary_[timestamp].csv** - Summary table- **SequenceSolver**: For pattern recognition and progressions

4. **performance_metrics.txt** - Performance statistics

## 🚀 Getting Started

## Customization

### 3. Reasoning Execution

If you want to modify the system:

Executes reasoning steps one by one:## Requirements

### Change Training Size

- Uses symbolic computation (SymPy library)

In `main.py`, find this line and change the number:

```python- Applies rule-based logic### Quick Start - Web UI

pipeline.run_full_pipeline(train_samples=50, ...)

```- Uses heuristic search when needed



### Add New Patterns- Matches against known patterns- Python 3.8+



In `pattern_matcher.py`, add your pattern to the list:

```python

def detect_new_pattern(self, sequence):### 4. Verification and Correction- pandasThe easiest way to use Solvra:

    # Your pattern detection logic

    passChecks the reasoning and fixes errors:

```

- Verifies numerical consistency- numpy

### Modify Solvers

- Checks logical consistency

In `solver.py`, you can adjust the solving strategies for each problem type.

- Validates against domain-specific rules- scikit-learn```bash

### Adjust Verification

- Applies heuristic corrections

In `verifier.py`, you can add custom verification rules.

- Other dependencies in `requirements.txt`# Install dependencies

## Dependencies

### 5. Trace Logging

Main libraries we use:

- **pandas** - Data handlingKeeps track of the entire reasoning process:pip install -r requirements.txt

- **numpy** - Numerical operations

- **sympy** - Symbolic mathematics- Records each decision step

- **scikit-learn** - Machine learning

- **tqdm** - Progress bars- Saves intermediate results## Approach

- **colorama** - Colored terminal output

- Logs verification warnings

See `requirements.txt` for the complete list with versions.

- Documents final predictions# Launch web interface

## Results and Reports



The system generates detailed reports after each run:

## Our ApproachWe tried different approaches and combined what worked best:streamlit run app.py

### Console Output

Shows real-time progress and a summary at the end with accuracy by topic.



### JSON TracesWe tried different approaches and combined what worked best:```

Complete reasoning traces in `reports/reasoning_traces_*.json`. These show every step the system took for each problem.



### CSV Summary

Tabular summary in `reports/reasoning_summary_*.csv` with one row per problem showing the prediction, actual answer (if known), and key metrics.1. **Pattern Recognition**: Many problems follow common patterns, so we built a pattern matcher to recognize these quickly.1. **Pattern Recognition**: We noticed that many problems follow common patterns, so we built a pattern matcher to recognize these



### Performance Metrics

Detailed statistics in `reports/performance_metrics.txt` including:

- Overall accuracy2. **Rule-Based Reasoning**: For logic and math problems, we use symbolic computation and predefined rules.2. **Rule-Based Reasoning**: For logic and math problems, we use symbolic computation and rulesThen open `http://localhost:8501` in your browser!

- Topic-wise breakdown

- Inference time distribution

- System configuration

3. **Verification**: We added a verification step to catch obvious mistakes before finalizing answers.3. **Verification**: We added a verification step to catch obvious mistakes

## Troubleshooting



### Import Errors

```bash4. **ML Enhancement**: We use machine learning for pattern recognition where pure rules don't work well.4. **ML Enhancement**: We use machine learning for pattern recognition where rules don't work well### Prerequisites

pip install --upgrade -r requirements.txt

```



### Out of Memory## Evaluation Metrics

Reduce the number of training samples in main.py



### Slow Performance

The system should be fast (< 1 second for all 96 test problems). If it's slow:The system is evaluated on:## Results- Python 3.10 or higher

- Check if you're running in debug mode

- Make sure tqdm progress bars aren't slowing things down- **Accuracy**: Percentage of correct predictions

- Try running from command line instead of an IDE

- **Topic-wise Performance**: How well it does on each problem type- pip package manager

## Future Improvements

- **Consistency**: How often it passes verification checks

Things we'd like to add if we had more time:

Our system works pretty well on the validation set. Different problem types have different accuracy:- 4GB+ RAM recommended

- Better spatial reasoning (maybe add visualization)

- More sophisticated pattern matching### Viewing Results

- Integration with a small language model for natural language understanding

- More comprehensive test coverage- Sequence problems: Good performance with pattern matching

- Support for more problem types

- Interactive demo/web interfaceAfter running the code, you can check:



## Team- Logic puzzles: Rule-based approach works well### Installation



This project was built for the Ethos 2025 challenge. We're students interested in AI and reasoning systems.1. **Console Output**: Shows progress and final summary



## Acknowledgments2. **CSV Summary**: `reports/reasoning_summary_*.csv` - All results in a table- Spatial reasoning: Still improving this part



Thanks to Saptang Labs for organizing this challenge and providing an interesting problem set. It was fun to work on!3. **JSON Traces**: `reports/reasoning_traces_*.json` - Complete reasoning traces



## License4. **Performance Metrics**: `reports/performance_metrics.txt` - Detailed metrics1. **Clone or navigate to the project directory**:



This project was created for the Ethos 2025 hackathon.



---## Reasoning Strategies by Problem Type## Challenges We Faced```bash



## Quick Start Guide



If you just want to run it quickly:### Optimization Problemscd Solvra



```bash1. Extract all constraints from the problem

# Install dependencies

pip install -r requirements.txt2. Identify what we're trying to minimize or maximize- Some problems need multiple reasoning steps which is tricky to handle```



# Run the system3. Evaluate all feasible solutions

cd src

python main.py4. Use greedy or exhaustive search- Spatial reasoning problems are harder than we thought



# Check your predictions

cd ../data

# Your predictions are now in predictions.csv### Spatial Problems- Balancing rule-based and ML approaches took some experimentation2. **Create a virtual environment** (recommended):

```

1. Visualize the spatial configuration

That's it! The system will process everything and generate your predictions file.

2. Extract dimensions and positions```bash

---

3. Apply geometric formulas

For questions or issues, check the reasoning traces in the reports folder to see what the system was thinking.

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
