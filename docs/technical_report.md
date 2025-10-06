# Solvra Technical Report

## System Architecture

### Overview
Solvra is a modular mathematical reasoning system composed of five core components that work in sequence to process mathematical questions.

### Component Pipeline

```
Input Question
    ↓
┌─────────────────┐
│  Classifier     │ → Predict question type
└─────────────────┘
    ↓
┌─────────────────┐
│  Planner        │ → Generate reasoning steps
└─────────────────┘
    ↓
┌─────────────────┐
│  Solver         │ → Execute mathematical operations
└─────────────────┘
    ↓
┌─────────────────┐
│  Verifier       │ → Validate and score solution
└─────────────────┘
    ↓
┌─────────────────┐
│  Trace Recorder │ → Log reasoning process
└─────────────────┘
    ↓
Output + Confidence
```

## Question Types

The system handles seven categories of mathematical problems:

1. **Arithmetic**: Basic operations (addition, subtraction, multiplication, division)
2. **Algebra**: Equation solving with variables
3. **Geometry**: Spatial calculations (area, perimeter, volume)
4. **Logic**: Boolean reasoning and logical operations
5. **Word Problems**: Real-world scenario translation
6. **Comparison**: Value comparison and ordering
7. **Pattern Recognition**: Sequence identification and prediction

## Classifier

### Model: Random Forest Classifier
- Features: TF-IDF vectorization (max 1000 features, bigrams)
- Estimators: 100 trees
- Training: 80/20 train-validation split with stratification

### Performance
- Cross-validation accuracy: 85%+
- Handles multi-class classification robustly

## Solver Strategies

### Arithmetic
- Regex-based number extraction
- Operation keyword detection
- Direct computation using NumPy

### Algebra
- SymPy symbolic parsing
- Equation solving with `sp.solve()`
- Variable isolation

### Geometry
- Shape-specific formula application
- Dimensional extraction
- Pi approximation handling

### Logic
- Boolean operator parsing
- Truth table evaluation
- Logical inference

### Word Problems
- Entity and relationship extraction
- Mathematical formulation
- Contextual interpretation

### Comparison
- Value normalization
- Ordering and ranking
- Min/max identification

### Pattern Recognition
- Arithmetic progression detection
- Geometric progression detection
- Difference analysis

## Verification

### Confidence Scoring
- Answer existence: baseline +0.5
- Numeric type validation: +0.25
- Magnitude sanity check: ±0.2
- Input-output consistency: +0.15
- Type-specific bonus: +0.1

### Validation Checks
1. Answer non-nullity
2. Type correctness
3. Magnitude reasonability
4. Step completeness

## Reasoning Traces

### Trace Structure
```json
{
  "trace_id": "uuid",
  "timestamp": "ISO-8601",
  "question": "string",
  "classification": {
    "type": "string",
    "steps_planned": ["array"]
  },
  "solution": {
    "answer": "numeric/boolean",
    "steps_executed": ["array"],
    "error": "string or null"
  },
  "verification": {
    "is_valid": "boolean",
    "confidence": "float",
    "checks": ["array"]
  }
}
```

## Evaluation Metrics

### Primary Metrics
1. **Accuracy**: Correct answers / Total questions
2. **Macro F1 Score**: Average F1 across all categories
3. **Average Inference Time**: Mean processing time per question

### Secondary Metrics
- Per-category accuracy
- Confidence distribution
- Average reasoning steps
- Error rate by type

## Dataset Specification

### Training Set
- Size: 500 samples
- Distribution: Balanced across 7 categories
- Difficulty: Grades 6-11 level

### Test Set
- Size: 100 samples
- Same distribution as training
- Unseen questions

### Format
```csv
question,type,answer
"What is 15 + 27?",arithmetic,42
```

## Performance Targets

- Overall Accuracy: ≥73%
- Macro F1 Score: ≥0.70
- Inference Time: <1.0s per question
- Confidence Calibration: Strong correlation with correctness

## Error Analysis

### Common Error Sources
1. Ambiguous question phrasing
2. Multiple valid interpretations
3. Unit conversion requirements
4. Complex multi-step reasoning
5. Implicit domain knowledge

### Mitigation Strategies
- Robust keyword detection
- Multiple solver strategies
- Confidence-based fallbacks
- Explicit step recording

## Future Enhancements

1. Large language model integration for better understanding
2. Multi-modal input support (images, diagrams)
3. Interactive clarification questions
4. Incremental learning from corrections
5. Explainable AI techniques for trace interpretation

## Technical Stack

- **Language**: Python 3.8+
- **ML Library**: scikit-learn
- **Symbolic Math**: SymPy
- **Numerical**: NumPy, pandas
- **UI**: Streamlit
- **Testing**: pytest

## Hackathon Context

**Event**: Ethos 2025
**Track**: Machine Learning Challenge
**Organizer**: Saptang Labs
**Venue**: IIT Guwahati

## Conclusion

Solvra demonstrates that modular, interpretable reasoning systems can achieve competitive performance on mathematical problems while maintaining full transparency through reasoning traces. The system balances accuracy, speed, and explainability for educational and assessment applications.
