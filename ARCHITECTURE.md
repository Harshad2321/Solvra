# Solvra Architecture Diagram

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                         SOLVRA REASONING SYSTEM                      ┃
┃                    Agentic Multi-Step Problem Solver                 ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

                              ┌─────────────┐
                              │   INPUT     │
                              │   Problem   │
                              └──────┬──────┘
                                     │
                                     ▼
                       ┌─────────────────────────┐
                       │   PREPROCESSING         │
                       │  - Text cleaning        │
                       │  - Number extraction    │
                       │  - Topic classification │
                       │  - Feature extraction   │
                       └───────────┬─────────────┘
                                   │
                                   ▼
                       ┌─────────────────────────┐
                       │   REASONING AGENT       │
                       │  Central Orchestrator   │
                       └───────────┬─────────────┘
                                   │
                   ┌───────────────┼───────────────┐
                   │               │               │
                   ▼               ▼               ▼
          ┌────────────┐  ┌────────────┐  ┌────────────┐
          │  PROBLEM   │  │    TOOL    │  │  SUBGOAL   │
          │DECOMPOSE   │  │ SELECTION  │  │  PLANNING  │
          └────────────┘  └────────────┘  └────────────┘
                   │               │               │
                   └───────────────┼───────────────┘
                                   │
                   ┌───────────────┴───────────────┐
                   │                               │
                   ▼                               ▼
       ┌───────────────────┐         ┌───────────────────┐
       │  SOLVER MODULES   │         │  KNOWLEDGE BASE   │
       └───────────────────┘         │  - Training data  │
                   │                 │  - Solution hints │
       ┌───────────┼───────────┐     └───────────────────┘
       │           │           │
       ▼           ▼           ▼
┌──────────┐ ┌──────────┐ ┌──────────┐
│   MATH   │ │  LOGIC   │ │ SPATIAL  │
│ SOLVER   │ │ SOLVER   │ │ SOLVER   │
└──────────┘ └──────────┘ └──────────┘
       │           │           │
       └───────────┼───────────┘
                   │
                   ▼
            ┌──────────┐
            │ SEQUENCE │
            │ SOLVER   │
            └─────┬────┘
                  │
                  ▼
       ┌────────────────────┐
       │  INTERMEDIATE      │
       │  RESULTS           │
       └─────────┬──────────┘
                 │
                 ▼
       ┌────────────────────┐
       │  VERIFIER          │
       │  - Consistency     │
       │  - Range check     │
       │  - Logic check     │
       │  - Correction      │
       └─────────┬──────────┘
                 │
                 ▼
       ┌────────────────────┐
       │  ANSWER EVALUATOR  │
       │  - Match options   │
       │  - Apply heuristics│
       │  - Select best     │
       └─────────┬──────────┘
                 │
      ┌──────────┴──────────┐
      │                     │
      ▼                     ▼
┌─────────────┐    ┌────────────────┐
│   OUTPUT    │    │  TRACE LOGGER  │
│ Prediction  │    │  - Steps       │
│ (Option 1-5)│    │  - Reasoning   │
└─────────────┘    │  - Verification│
                   └────────────────┘
```

## Detailed Component Breakdown

### 1. Preprocessing Module
```
Input: Raw problem text
├─► Text Cleaning
├─► Number Extraction
├─► Pattern Detection
└─► Feature Flags
Output: Structured problem
```

### 2. Reasoning Agent
```
Input: Structured problem
├─► Problem Decomposition
│   ├─► Identify constraints
│   ├─► Break into subproblems
│   └─► Create execution plan
├─► Tool Selection
│   ├─► Analyze problem type
│   ├─► Check keywords
│   └─► Select optimal solver
└─► Subgoal Planning
    ├─► Order subproblems
    └─► Define dependencies
Output: Reasoning plan
```

### 3. Solver Modules

#### Math Solver
```
Handles:
├─► Arithmetic operations
├─► Algebraic equations (SymPy)
├─► Optimization (TSP, scheduling)
├─► Rate problems
└─► Percentage calculations
```

#### Logic Solver
```
Handles:
├─► Truth tables
├─► Deductive reasoning
├─► Truth-teller/liar problems
├─► Riddles
└─► Logical constraints
```

#### Spatial Solver
```
Handles:
├─► 3D geometry
├─► Cube face counting
├─► Room navigation
├─► Distance calculations
└─► Spatial transformations
```

#### Sequence Solver
```
Handles:
├─► Arithmetic sequences
├─► Geometric sequences
├─► Recursive patterns
├─► Polynomial fitting
└─► Pattern prediction
```

### 4. Verifier Module
```
Input: Candidate answer
├─► Numerical Consistency
│   ├─► Range validation
│   └─► Magnitude check
├─► Logical Consistency
│   ├─► Step validation
│   └─► Contradiction check
├─► Domain-Specific Rules
│   ├─► Cube constraints
│   ├─► Sequence patterns
│   └─► Optimization bounds
└─► Correction Heuristics
    ├─► Pattern matching
    ├─► Fallback strategies
    └─► Confidence scoring
Output: Verified/corrected answer
```

### 5. Trace Logger
```
Captures:
├─► Decomposition steps
├─► Tool selection rationale
├─► Solver execution trace
├─► Intermediate results
├─► Verification results
└─► Final decision
Output: Complete reasoning trace
```

## Data Flow Example

### Example: Sequence Problem

```
INPUT:
"Find the next number: 2, 5, 10, 17, 26, ?"

    ↓

PREPROCESSING:
- Extract numbers: [2, 5, 10, 17, 26]
- Identify topic: Sequence solving
- Set flags: requires_sequence=True

    ↓

DECOMPOSITION:
1. Extract sequence
2. Identify pattern
3. Predict next value

    ↓

TOOL SELECTION:
Selected: SequenceSolver
Reason: Topic="sequence", numbers present

    ↓

SOLVING:
Step 1: Extract → [2, 5, 10, 17, 26]
Step 2: Check patterns
  - Differences: [3, 5, 7, 9]
  - Second differences: [2, 2, 2]
  - Pattern: Arithmetic with increasing diffs
Step 3: Predict
  - Next diff: 9 + 2 = 11
  - Next value: 26 + 11 = 37

    ↓

VERIFICATION:
✓ Numerical range: OK (within expected)
✓ Pattern consistency: OK (follows rule)
✓ Option exists: OK (option 2 = 37)

    ↓

OUTPUT:
Prediction: Option 2
Confidence: HIGH
Trace: Saved to JSON/HTML
```

## System Characteristics

### Strengths
```
✓ Modular: Easy to extend
✓ Explainable: Complete trace
✓ Verifiable: Built-in checks
✓ Efficient: No GPU needed
✓ Transparent: No black box
```

### Design Principles
```
1. Separation of Concerns
   - Each module has clear responsibility

2. Composability
   - Solvers can be combined

3. Extensibility
   - New solvers easily added

4. Testability
   - Each component independently testable

5. Explainability
   - Every decision logged and traceable
```

## Technology Stack

```
┌────────────────────────────────────┐
│     Application Layer              │
│  - main.py (orchestration)         │
│  - demo.py (presentation)          │
└────────────────────────────────────┘
              │
┌────────────────────────────────────┐
│     Reasoning Layer                │
│  - reasoning_agent.py              │
│  - verifier.py                     │
│  - trace_logger.py                 │
└────────────────────────────────────┘
              │
┌────────────────────────────────────┐
│     Solver Layer                   │
│  - solver.py (all solvers)         │
│  - preprocess.py                   │
└────────────────────────────────────┘
              │
┌────────────────────────────────────┐
│     Library Layer                  │
│  - SymPy (symbolic math)           │
│  - NumPy (numerical ops)           │
│  - Pandas (data handling)          │
└────────────────────────────────────┘
```

## Comparison with Alternatives

```
┌─────────────────┬───────────┬──────────┬─────────┬──────────┐
│ Approach        │ Solvra    │ GPT-4    │ Rules   │ Pure ML  │
├─────────────────┼───────────┼──────────┼─────────┼──────────┤
│ Transparency    │ ⭐⭐⭐⭐⭐   │ ⭐⭐      │ ⭐⭐⭐⭐⭐  │ ⭐⭐       │
│ Accuracy        │ ⭐⭐⭐⭐    │ ⭐⭐⭐⭐⭐   │ ⭐⭐⭐     │ ⭐⭐⭐⭐     │
│ Speed           │ ⭐⭐⭐⭐⭐   │ ⭐⭐⭐     │ ⭐⭐⭐⭐⭐  │ ⭐⭐⭐      │
│ Resources       │ ⭐⭐⭐⭐⭐   │ ⭐⭐      │ ⭐⭐⭐⭐⭐  │ ⭐⭐⭐      │
│ Explainability  │ ⭐⭐⭐⭐⭐   │ ⭐⭐      │ ⭐⭐⭐⭐   │ ⭐⭐       │
└─────────────────┴───────────┴──────────┴─────────┴──────────┘
```

---

**This architecture enables Solvra to achieve competitive accuracy while maintaining complete transparency and explainability.**
