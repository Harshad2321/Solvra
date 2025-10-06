import pytest
import sys
import pandas as pd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.pipeline import SolvraPipeline

def test_pipeline_initialization():
    pipeline = SolvraPipeline()
    assert pipeline is not None
    assert pipeline.classifier is not None
    assert pipeline.planner is not None
    assert pipeline.solver is not None
    assert pipeline.verifier is not None

def test_pipeline_process_question():
    pipeline = SolvraPipeline()
    
    question = "What is 15 + 25?"
    
    result = pipeline.process_question(question)
    
    assert result is not None
    assert 'question' in result
    assert 'predicted_answer' in result
    assert 'trace_id' in result
    assert 'confidence' in result

def test_pipeline_creates_output():
    pipeline = SolvraPipeline()
    
    test_data = pd.DataFrame({
        'question': ['What is 2 + 2?', 'What is 5 times 3?'],
        'type': ['arithmetic', 'arithmetic'],
        'answer': [4, 15]
    })
    
    test_csv = 'tests/temp_test.csv'
    output_csv = 'tests/temp_output.csv'
    
    Path('tests').mkdir(exist_ok=True)
    test_data.to_csv(test_csv, index=False)
    
    pipeline.run_pipeline(input_csv=test_csv, output_csv=output_csv)
    
    assert Path(output_csv).exists()
    
    output_df = pd.read_csv(output_csv)
    assert len(output_df) == 2
    assert 'question' in output_df.columns
    assert 'predicted_answer' in output_df.columns
    
    Path(test_csv).unlink()
    Path(output_csv).unlink()
