from src.log_utils import setup_logger

logger = setup_logger()

class ReasoningPlanner:
    def __init__(self, classifier):
        self.classifier = classifier
        self.plan_templates = {
            'arithmetic': [
                'identify_numbers',
                'identify_operation',
                'execute_calculation',
                'format_result'
            ],
            'algebra': [
                'parse_equation',
                'isolate_variable',
                'solve_for_unknown',
                'verify_solution'
            ],
            'geometry': [
                'identify_shape',
                'extract_dimensions',
                'apply_formula',
                'calculate_result'
            ],
            'logic': [
                'parse_conditions',
                'apply_logical_rules',
                'derive_conclusion',
                'verify_consistency'
            ],
            'word_problem': [
                'extract_entities',
                'identify_relationships',
                'formulate_equation',
                'solve_equation',
                'interpret_result'
            ],
            'comparison': [
                'extract_values',
                'normalize_units',
                'compare_values',
                'determine_result'
            ],
            'pattern': [
                'identify_sequence',
                'find_pattern_rule',
                'apply_rule',
                'predict_next'
            ]
        }
    
    def create_plan(self, question):
        question_type = self.classifier.predict_type(question)
        logger.info(f"Classified question as: {question_type}")
        
        steps = self.plan_templates.get(question_type, self.plan_templates['arithmetic'])
        
        plan = {
            'question': question,
            'type': question_type,
            'steps': steps,
            'current_step': 0
        }
        
        return plan
    
    def parse_question(self, question):
        tokens = question.lower().split()
        numbers = []
        operations = []
        
        for token in tokens:
            try:
                numbers.append(float(token))
            except ValueError:
                pass
            
            if token in ['add', 'sum', 'plus', '+']:
                operations.append('add')
            elif token in ['subtract', 'minus', 'difference', '-']:
                operations.append('subtract')
            elif token in ['multiply', 'times', 'product', '*']:
                operations.append('multiply')
            elif token in ['divide', 'quotient', '/']:
                operations.append('divide')
        
        return {
            'numbers': numbers,
            'operations': operations,
            'tokens': tokens
        }
