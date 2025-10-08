# 🚀 Solvra Quick Start Guide

Get Solvra up and running in 5 minutes!

---

## Step 1: Environment Setup (2 minutes)

### Open PowerShell in VS Code

```powershell
# Navigate to project directory
cd c:\Users\harsh\Desktop\Solvra

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# If you get execution policy error, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## Step 2: Install Dependencies (2 minutes)

```powershell
# Install all required packages
pip install -r requirements.txt

# Install spaCy language model (optional)
python -m spacy download en_core_web_sm
```

**Expected output**: All packages installed successfully

---

## Step 3: Quick Test (1 minute)

### Option A: Run Demo (Recommended for presentation practice)

```powershell
cd src
python demo.py
```

This shows an interactive 3-5 minute demo perfect for the hackathon presentation!

### Option B: Run Full Pipeline

```powershell
cd src
python main.py
```

This will:
1. Load and preprocess data
2. Analyze 50 training examples
3. Generate predictions for test set
4. Create detailed reports

**First run takes**: ~2-5 minutes

---

## Step 4: View Results

### Check Console Output
You'll see real-time progress and accuracy metrics.

### Open HTML Report
```powershell
# Navigate to reports folder
cd ..\reports

# Open the latest HTML report (replace timestamp)
start reasoning_report_*.html
```

The HTML report shows:
- Overall accuracy
- Detailed reasoning traces
- Step-by-step explanations

### Check Predictions
```powershell
# View predictions
cd ..\data
type predictions.csv | Select-Object -First 20
```

---

## Common Commands

### Run with Different Training Size

Edit `src/main.py`, line 93:
```python
pipeline.run_full_pipeline(
    train_samples=100,  # Change this number (max 534)
    generate_test_predictions=True
)
```

### Test Individual Component

```powershell
cd src

# Test preprocessing
python preprocess.py

# Test solvers
python solver.py

# Test reasoning agent
python reasoning_agent.py

# Test verifier
python verifier.py
```

---

## Troubleshooting

### Issue: "python is not recognized"
**Solution**: 
```powershell
# Check Python installation
py --version

# Use 'py' instead of 'python'
py -m venv venv
```

### Issue: Import errors
**Solution**:
```powershell
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### Issue: "Cannot load module"
**Solution**:
```powershell
# Make sure you're in the src directory
cd src
python main.py
```

### Issue: Memory error
**Solution**: Reduce training samples in `main.py` to 20-30

---

## File Locations

| What | Where |
|------|-------|
| Source code | `src/*.py` |
| Training data | `data/train.csv` |
| Test data | `data/test.csv` |
| Predictions | `data/predictions.csv` |
| Reports | `reports/*.html` |
| Traces | `reports/*.json` |

---

## Next Steps

1. ✅ Run quick test
2. ✅ Review sample output
3. ✅ Run demo for practice
4. ✅ Increase training samples
5. ✅ Review HTML report
6. ✅ Generate final predictions
7. ✅ Prepare presentation

---

## Presentation Checklist

- [ ] Run `python demo.py` and practice timing (aim for 3-4 minutes)
- [ ] Open HTML report in browser for showing results
- [ ] Have `predictions.csv` ready to show
- [ ] Prepare to explain system architecture diagram
- [ ] Ready to discuss novel features (explainability, verification)

---

## Quick Commands Cheat Sheet

```powershell
# Activate environment
.\venv\Scripts\Activate.ps1

# Run demo
cd src; python demo.py

# Run full pipeline
cd src; python main.py

# Run with more training data
# (Edit main.py first)
cd src; python main.py

# View results
cd ..\reports; start reasoning_report_*.html

# Check predictions
cd ..\data; type predictions.csv

# Deactivate environment
deactivate
```

---

## Performance Tips

### For Speed
- Use 20-50 training samples for testing
- Use 100-200 for development
- Use full 534 for final submission

### For Accuracy
- Review failed cases in HTML report
- Adjust heuristics in `verifier.py`
- Add domain rules in `solver.py`

### For Demo
- Run `demo.py` - it's optimized for presentation
- Practice the flow (3-5 minutes)
- Know your talking points

---

## Help & Support

If stuck:
1. Check this guide
2. Read README.md
3. Check code comments in `src/*.py`
4. Review error messages carefully

---

## Success Indicators

✅ All packages installed without errors  
✅ `python main.py` completes successfully  
✅ HTML report generated  
✅ `predictions.csv` has 101 rows  
✅ Demo runs smoothly  

---

## Final Submission Preparation

1. **Run full pipeline**:
```powershell
cd src
# Edit main.py: train_samples=534
python main.py
```

2. **Verify output**:
- Check `data/predictions.csv` has 101 predictions
- Review HTML report for quality
- Verify format matches `data/output.csv`

3. **Package submission**:
- `predictions.csv` (required)
- Technical report (generated in `reports/`)
- Demo video or live demo

4. **Practice presentation**:
- 3-5 minutes
- Show live demo
- Explain architecture
- Highlight novel features

---

**You're ready to win Ethos 2025! 🏆**

Good luck!
