"""
Solvra - Trace Logger Module
Logs and saves reasoning traces for explainability and debugging
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any
import pandas as pd


class TraceLogger:
    """
    Manages logging of reasoning traces for transparency and evaluation
    """
    
    def __init__(self, log_dir: str = "../reports"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)
        
        self.traces = []
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def log_problem_trace(self, problem_idx: int, problem: Dict[str, Any],
                         prediction: int, reasoning_trace: List[Dict],
                         verification_report: str = ""):
        """
        Log the complete reasoning trace for a single problem
        """
        trace_entry = {
            'problem_idx': problem_idx,
            'session_id': self.session_id,
            'timestamp': datetime.now().isoformat(),
            'topic': problem.get('topic', 'Unknown'),
            'problem_statement': problem.get('problem_statement', '')[:200],  # Truncate for storage
            'predicted_option': prediction,
            'correct_option': problem.get('correct_option_number', None),
            'is_correct': prediction == problem.get('correct_option_number', None) if 'correct_option_number' in problem else None,
            'reasoning_steps': reasoning_trace,
            'verification_report': verification_report
        }
        
        self.traces.append(trace_entry)
    
    def save_traces_json(self, filename: str = None):
        """Save all traces to JSON file"""
        if filename is None:
            filename = f"reasoning_traces_{self.session_id}.json"
        
        filepath = self.log_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.traces, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Saved {len(self.traces)} reasoning traces to {filepath}")
    
    def save_traces_csv(self, filename: str = None):
        """Save traces summary to CSV"""
        if filename is None:
            filename = f"reasoning_summary_{self.session_id}.csv"
        
        filepath = self.log_dir / filename
        
        # Create summary DataFrame
        summary_data = []
        for trace in self.traces:
            summary_data.append({
                'problem_idx': trace['problem_idx'],
                'topic': trace['topic'],
                'predicted_option': trace['predicted_option'],
                'correct_option': trace['correct_option'],
                'is_correct': trace['is_correct'],
                'num_reasoning_steps': len(trace['reasoning_steps']),
                'has_warnings': 'WARNING' in trace.get('verification_report', '')
            })
        
        df = pd.DataFrame(summary_data)
        df.to_csv(filepath, index=False)
        
        print(f"Saved reasoning summary to {filepath}")
    
    def generate_html_report(self, filename: str = None):
        """Generate an HTML report with detailed reasoning traces"""
        # Temporarily disabled due to formatting issue
        print("  HTML report generation temporarily disabled")
        return
        
        if filename is None:
            filename = f"reasoning_report_{self.session_id}.html"
        
        filepath = self.log_dir / filename
        
        html_content = self._build_html_report()
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f" Generated HTML report: {filepath}")
    
    def _build_html_report(self) -> str:
        """Build HTML content for the report"""
        html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Solvra Reasoning Report</title>
    <style>
        body { font-family: 'Segoe UI', Arial, sans-serif; margin: 20px; background: #f5f5f5; }
        .container { max-width: 1200px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }
        h2 { color: #34495e; margin-top: 30px; }
        .problem { background: #ecf0f1; padding: 15px; margin: 20px 0; border-radius: 5px; border-left: 4px solid #3498db; }
        .correct { border-left-color: #27ae60; }
        .incorrect { border-left-color: #e74c3c; }
        .trace-step { background: #fff; margin: 10px 0; padding: 10px; border-left: 2px solid #95a5a6; }
        .prediction { font-weight: bold; color: #2980b9; }
        .warning { color: #e67e22; font-style: italic; }
        .stats { display: flex; justify-content: space-around; margin: 20px 0; }
        .stat-box { background: #3498db; color: white; padding: 20px; border-radius: 5px; text-align: center; min-width: 150px; }
        .stat-value { font-size: 36px; font-weight: bold; }
        .stat-label { font-size: 14px; margin-top: 5px; }
    </style>
</head>
<body>
    <div class="container">
        <h1> Solvra Reasoning Report</h1>
        <p><strong>Session:</strong> {session_id}</p>
        <p><strong>Generated:</strong> {timestamp}</p>
        
        {stats_section}
        
        <h2> Detailed Reasoning Traces</h2>
        {traces_section}
    </div>
</body>
</html>
"""
        
        # Calculate statistics
        total = len(self.traces)
        correct = sum(1 for t in self.traces if t.get('is_correct') == True)
        accuracy = (correct / total * 100) if total > 0 else 0
        
        stats_html = f"""
        <div class="stats">
            <div class="stat-box">
                <div class="stat-value">{total}</div>
                <div class="stat-label">Total Problems</div>
            </div>
            <div class="stat-box">
                <div class="stat-value">{correct}</div>
                <div class="stat-label">Correct</div>
            </div>
            <div class="stat-box">
                <div class="stat-value">{accuracy:.1f}%</div>
                <div class="stat-label">Accuracy</div>
            </div>
        </div>
        """
        
        # Build traces
        traces_html = ""
        for trace in self.traces[:20]:  # Limit to first 20 for performance
            correct_class = 'correct' if trace.get('is_correct') else 'incorrect'
            
            steps_html = ""
            for i, step in enumerate(trace['reasoning_steps'], 1):
                steps_html += f"""
                <div class="trace-step">
                    <strong>Step {i}:</strong> {step.get('step', '')}
                    {f"<br><em>Result: {step.get('result', '')}</em>" if step.get('result') else ''}
                </div>
                """
            
            traces_html += f"""
            <div class="problem {correct_class}">
                <h3>Problem #{trace['problem_idx']} - {trace['topic']}</h3>
                <p><strong>Statement:</strong> {trace['problem_statement']}...</p>
                <p class="prediction">Predicted Option: {trace['predicted_option']}</p>
                {f"<p><strong>Correct Option:</strong> {trace['correct_option']}</p>" if trace.get('correct_option') else ''}
                
                <h4>Reasoning Steps:</h4>
                {steps_html}
                
                {f'<p class="warning"> {trace["verification_report"]}</p>' if trace.get('verification_report') else ''}
            </div>
            """
        
        html = html.format(
            session_id=self.session_id,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            stats_section=stats_html,
            traces_section=traces_html
        )
        
        return html
    
    def print_summary(self):
        """Print summary statistics to console"""
        if not self.traces:
            print("No traces logged yet")
            return
        
        total = len(self.traces)
        correct = sum(1 for t in self.traces if t.get('is_correct') == True)
        accuracy = (correct / total * 100) if total > 0 else 0
        
        # Topic-wise breakdown
        topic_stats = {}
        for trace in self.traces:
            topic = trace['topic']
            if topic not in topic_stats:
                topic_stats[topic] = {'total': 0, 'correct': 0}
            topic_stats[topic]['total'] += 1
            if trace.get('is_correct'):
                topic_stats[topic]['correct'] += 1
        
        print("\n" + "="*60)
        print(" SOLVRA REASONING SUMMARY")
        print("="*60)
        print(f"Total Problems: {total}")
        print(f"Correct: {correct}")
        print(f"Accuracy: {accuracy:.2f}%")
        print("\n Topic-wise Performance:")
        print("-"*60)
        
        for topic, stats in sorted(topic_stats.items()):
            topic_acc = (stats['correct'] / stats['total'] * 100) if stats['total'] > 0 else 0
            print(f"{topic:30s}: {stats['correct']}/{stats['total']} ({topic_acc:.1f}%)")
        
        print("="*60 + "\n")


def demo_logger():
    """Demo the trace logger"""
    logger = TraceLogger(log_dir="../reports")
    
    # Sample traces
    for i in range(3):
        problem = {
            'topic': 'Sequence solving',
            'problem_statement': f'Sample problem {i+1}',
            'correct_option_number': 2
        }
        
        trace = [
            {'step': 'Decompose problem', 'result': '3 subproblems'},
            {'step': 'Select tool', 'result': 'sequence_solver'},
            {'step': 'Predict next', 'result': 10}
        ]
        
        logger.log_problem_trace(i, problem, 2, trace, " All checks passed")
    
    logger.print_summary()
    logger.save_traces_json()
    logger.save_traces_csv()
    logger.generate_html_report()


if __name__ == "__main__":
    demo_logger()
