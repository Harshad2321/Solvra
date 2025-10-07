import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from src.pipeline import SolvraPipeline
import json

st.set_page_config(page_title="Solvra", page_icon="", layout="wide")

st.title("🧮 Solvra - Math Problem Solver")
st.subheader("AI-powered mathematical reasoning system")

@st.cache_resource
def load_pipeline():
    return SolvraPipeline()

pipeline = load_pipeline()

st.markdown("---")

question = st.text_area(
    "Enter your mathematical question:",
    placeholder="e.g., What is the sum of 45 and 78?",
    height=100
)

if st.button("Solve", type="primary"):
    if question.strip():
        with st.spinner("Processing..."):
            result = pipeline.process_question(question)
            
            st.success("Solution Complete!")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Answer", result['predicted_answer'])
            
            with col2:
                st.metric("Confidence", f"{result['confidence']:.2%}")
            
            st.markdown("---")
            st.subheader("Reasoning Trace")
            
            trace = pipeline.trace_recorder.get_trace(result['trace_id'])
            
            if trace:
                st.json(trace)
            else:
                st.info("Trace details will be saved after processing.")
            
            st.caption(f"Inference Time: {result['inference_time']:.4f}s")
    else:
        st.warning("Please enter a question.")

st.markdown("---")
st.markdown("""
### What can Solvra solve?
- **Arithmetic** - Basic math operations
- **Algebra** - Equations with variables
- **Geometry** - Areas, volumes, etc.
- **Logic** - Reasoning problems
- **Word Problems** - Real-world scenarios
- **Comparisons** - Max, min, greater/less
- **Patterns** - Number sequences
""")

st.caption("Made for Ethos 2025 Hackathon at IIT Guwahati")
