import json
import uuid
from pathlib import Path
from datetime import datetime
from src.log_utils import setup_logger

logger = setup_logger()

class ReasoningTraceRecorder:
    def __init__(self, trace_file="data/reasoning_traces.json"):
        self.trace_file = trace_file
        self.traces = []
        
    def create_trace(self, question, plan, solution, verification):
        trace_id = str(uuid.uuid4())
        
        trace = {
            'trace_id': trace_id,
            'timestamp': datetime.now().isoformat(),
            'question': question,
            'classification': {
                'type': plan.get('type'),
                'steps_planned': plan.get('steps', [])
            },
            'solution': {
                'answer': solution.get('answer'),
                'steps_executed': solution.get('steps', []),
                'error': solution.get('error')
            },
            'verification': {
                'is_valid': verification.get('is_valid'),
                'confidence': verification.get('confidence'),
                'checks': verification.get('checks', [])
            }
        }
        
        self.traces.append(trace)
        logger.info(f"Created trace {trace_id} for question")
        
        return trace_id
    
    def save_traces(self):
        Path(self.trace_file).parent.mkdir(parents=True, exist_ok=True)
        
        existing_traces = []
        if Path(self.trace_file).exists():
            with open(self.trace_file, 'r') as f:
                try:
                    existing_traces = json.load(f)
                except json.JSONDecodeError:
                    existing_traces = []
        
        all_traces = existing_traces + self.traces
        
        with open(self.trace_file, 'w') as f:
            json.dump(all_traces, f, indent=2)
        
        logger.info(f"Saved {len(self.traces)} traces to {self.trace_file}")
        self.traces = []
    
    def get_trace(self, trace_id):
        if Path(self.trace_file).exists():
            with open(self.trace_file, 'r') as f:
                traces = json.load(f)
                for trace in traces:
                    if trace['trace_id'] == trace_id:
                        return trace
        return None
