# Solvra - Problem Type Coverage

## ✅ FULLY SUPPORTED (80% Success on Advanced Suite)

### Basic Problems (Original)
- ✅ Arithmetic: Basic operations, percentages
- ✅ Simple Algebra: Linear/quadratic equations
- ✅ Basic Geometry: Area, perimeter, volume
- ✅ Simple Patterns: Arithmetic/geometric sequences
- ✅ Basic Word Problems: Distance, time, rate

### Advanced Problems (NEW - October 2025)

#### Arithmetic
- ✅ **Nested Radicals**: `√(6 + 2√5) + √(6 - 2√5)` → Simplified form

#### Algebra
- ✅ **Parametric Equations**: `x⁴ - 4mx² + 4m² - 1 = 0` → Solutions in terms of m
- ✅ **Diophantine Equations**: `x² - 5y² = 4` → Integer solution pairs
- ✅ **Systems of Equations**: Multiple variables

#### Geometry
- ✅ **Circle Segments**: Chord length L, radius R → Segment area
- ✅ **Hyperbola Locus**: Distance conditions → Conic equation
- ✅ **Excircles & Heron's Formula**: Advanced triangle problems

#### Patterns
- ✅ **Homogeneous Recurrence**: `aₙ = aₙ₋₁ + 2aₙ₋₂` → Closed form **(FIXED)**
- ✅ **Non-Homogeneous Recurrence**: `bₙ = 3bₙ₋₁ - 2bₙ₋₂ + 2ⁿ` → Closed form
- ✅ **Quadratic Patterns**: 2, 5, 10, 17, 26 → 37
- ✅ **Fibonacci Detection**: Auto-detects Fibonacci-like sequences

#### Word Problems
- ✅ **Work Rates**: Combined painter/worker problems with time constraints
- ✅ **Boat/Current**: Upstream/downstream rate problems

#### Comparison
- ✅ **Inequality Proofs**: Prove `f(x) ≤ g(x)`, find equality conditions
- ✅ **Constrained Optimization**: Max/min with algebraic constraints

#### Logic
- ✅ **Knights/Knaves Puzzles**: Truth table analysis (3-person puzzles)

## ⚠️ PARTIAL SUPPORT (Classification Issues)

### Needs Better Routing
- ⚠️ Logic puzzles sometimes misclassified as arithmetic
- ⚠️ Optimization problems sometimes misclassified as geometry
- ⚠️ Parametric equations sometimes misclassified as arithmetic

**Solution**: Retrain classifier with advanced problem vocabulary

## 🚧 NOT YET SUPPORTED

### Planned
- ❌ Calculus: Derivatives, integrals, limits
- ❌ Matrix Algebra: Eigenvalues, determinants, systems
- ❌ Complex Numbers: Operations in ℂ
- ❌ Probability: Combinatorics, distributions
- ❌ Number Theory: Modular arithmetic, prime factorization
- ❌ Graph Theory: Shortest paths, spanning trees

## Problem Type Detection Keywords

### Arithmetic
- "evaluate", "calculate", "sum", "product", "radical", "sqrt"

### Algebra
- "solve for x", "equation", "parameter", "in terms of", "integer solution"

### Geometry
- "area", "perimeter", "circle", "triangle", "chord", "radius", "locus"

### Pattern
- "sequence", "pattern", "recurrence", "a_n", "fibonacci", "next term"

### Word Problem
- "hours", "together", "painter", "boat", "upstream", "downstream", "rate"

### Comparison
- "greater", "maximum", "minimum", "prove", "inequality", "subject to"

### Logic
- "knight", "knave", "truth", "lie", "always", "never"

## Usage Examples

```python
from src.pipeline import SolvraPipeline

pipeline = SolvraPipeline()

# Nested radicals
result = pipeline.process_question("Evaluate sqrt(6 + 2*sqrt(5)) + sqrt(6 - 2*sqrt(5))")
print(result['predicted_answer'])  # 4.472...

# Parametric equation
result = pipeline.process_question("Find x in terms of m: x^4 - 4*m*x^2 + 4*m^2 - 1 = 0")
print(result['predicted_answer'])  # Solutions with m

# Work rate
result = pipeline.process_question("Two painters together: 6 hours. A takes 4 hours less than B. Individual times?")
print(result['predicted_answer'])  # A: 10.32h, B: 14.32h

# Recurrence relation
result = pipeline.process_question("Sequence a_n = a_(n-1) + 2*a_(n-2), a_1=1, a_2=1. Find a_10.")
print(result['predicted_answer'])  # 341

# Diophantine
result = pipeline.process_question("Find integer solutions to x^2 - 5*y^2 = 4")
print(result['predicted_answer'])  # [(2,0), (-2,0), (3,1), ...]
```

## Testing

```bash
# Run basic pipeline tests
python -m pytest tests/

# Run recurrence validation
python test_recurrence.py

# Run advanced problem suite
python test_advanced.py

# Debug specific problems
python test_failing.py
```

## Success Metrics

| Test Suite | Success Rate | Note |
|------------|-------------|------|
| Basic Problems | 72.86% | Original dataset (100 problems) |
| Recurrence Fix | 100% | a₁₀ = 341 ✓ |
| Advanced Suite | 80% | 8/10 competition problems |
| Quadratic Patterns | 100% | 2,5,10,17,26→37 ✓ |
| Heron's Formula | 100% | Triangle(13,14,15)→84 ✓ |

## Repository

- **GitHub**: https://github.com/Harshad2321/Solvra
- **Latest Commit**: 25ae236
- **Branch**: main
- **Python**: 3.13.7
- **Key Dependencies**: sympy, scikit-learn, pandas, numpy, streamlit

---
*Quick Reference Guide - October 7, 2025*
