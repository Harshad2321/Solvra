# Solvra Quick Start Guide

## Installation

```powershell
pip install -r requirements.txt
```

## Workflow

### 1. Train Classifier (Already Done)
```powershell
python train_model.py
```

### 2. Run Pipeline (Already Done)
```powershell
python src/pipeline.py --input data/test.csv --output data/output.csv
```

### 3. Evaluate Metrics (Already Done)
```powershell
python evaluation/metrics.py
python evaluation/analyze.py
```

### 4. Launch UI
```powershell
streamlit run app.py
```

## Current Results

- **Accuracy**: 72.86%
- **Macro F1 Score**: 72.86%
- **Average Inference Time**: 0.0174s
- **Valid Solutions**: 69/70 (98.6%)
- **Average Confidence**: 81.21%

### Per-Category Performance

| Category | Accuracy | Correct/Total |
|----------|----------|---------------|
| Pattern | 100.0% | 10/10 |
| Geometry | 90.0% | 9/10 |
| Arithmetic | 70.0% | 7/10 |
| Logic | 70.0% | 7/10 |
| Comparison | 70.0% | 7/10 |
| Word Problem | 60.0% | 6/10 |
| Algebra | 50.0% | 5/10 |

## Testing

```powershell
python -m pytest tests/ -v
```

## Files Generated

- `data/train.csv` - 500 training samples
- `data/test.csv` - 100 test samples
- `data/output.csv` - Model predictions
- `data/reasoning_traces.json` - Complete reasoning logs
- `models/question_type.pkl` - Trained classifier
- `logs/system.log` - System logs

## UI Features

The Streamlit app provides:
- Single question input
- Real-time answer generation
- Confidence scoring
- Complete reasoning trace display
- Response time metrics

## Command Reference

```powershell
python train_model.py
python src/pipeline.py
python evaluation/metrics.py
python evaluation/analyze.py
streamlit run app.py
python -m pytest tests/
```

## Project Complete

All components are functional:
- ✓ Dataset generated (600 samples)
- ✓ Classifier trained (100% validation accuracy)
- ✓ Pipeline operational
- ✓ Metrics evaluated (72.86% accuracy)
- ✓ Frontend ready (Streamlit)
- ✓ Repository cleaned
