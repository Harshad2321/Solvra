"""
Simple test runner for Solvra
Author: Learning by building!
Purpose: Load test cases and see if my solver works correctly
"""

import json
import sys
from src.pipeline import SolvraPipeline

# colors for terminal output - makes it easier to read
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

def load_questions(filename='test_cases.json'):
    """Load all test questions from JSON file"""
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        sys.exit(1)

def print_header(text):
    """Print a nice header"""
    print(f"\n{Colors.BOLD}{Colors.HEADER}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.HEADER}{text.center(60)}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.HEADER}{'='*60}{Colors.END}\n")

def run_single_test(pipeline, q_data, num):
    """
    Run one test question through the solver
    q_data = dictionary with question, expected_answer, type
    """
    question = q_data['question']
    expected = q_data['expected_answer']
    q_type = q_data['type']
    
    # show what we're testing
    print(f"{Colors.BLUE}[Test {num}]{Colors.END} {question}")
    print(f"  Expected type: {Colors.YELLOW}{q_type}{Colors.END}")
    print(f"  Expected answer: {Colors.YELLOW}{expected}{Colors.END}")
    
    # run it through my pipeline
    try:
        result = pipeline.process_question(question)
        
        # extract the answer and confidence
        answer = result.get('predicted_answer', result.get('answer', 'No answer'))
        confidence = result.get('confidence', 0)
        detected_type = result.get('question_type', 'unknown')
        
        # display results
        print(f"  Detected type: {Colors.GREEN}{detected_type}{Colors.END}")
        print(f"  My answer: {Colors.GREEN}{answer}{Colors.END}")
        print(f"  Confidence: {confidence:.1f}%")
        
        # check if type detection was correct
        if detected_type.lower() == q_type.lower():
            print(f"  {Colors.GREEN}✓ Type detected correctly!{Colors.END}")
        else:
            print(f"  {Colors.RED}✗ Type mismatch!{Colors.END}")
            
        return True
        
    except Exception as e:
        print(f"  {Colors.RED}ERROR: {str(e)}{Colors.END}")
        return False
    
    finally:
        print()  # blank line for spacing

def run_all_tests():
    """Main function - runs all tests category by category"""
    
    print_header("SOLVRA TEST RUNNER")
    print("Loading test cases...")
    
    # load questions from json
    test_data = load_questions()
    
    # initialize my pipeline
    print("Initializing Solvra pipeline...\n")
    pipeline = SolvraPipeline()
    
    # keep track of stats
    total_tests = 0
    successful_tests = 0
    
    # go through each category
    categories = ['arithmetic', 'algebra', 'geometry', 'logic', 
                  'word_problem', 'comparison', 'pattern']
    
    for category in categories:
        if category not in test_data:
            continue
            
        # print category header
        print_header(f"{category.upper().replace('_', ' ')} TESTS")
        
        questions = test_data[category]
        cat_success = 0
        
        # run each question in this category
        for i, q_data in enumerate(questions, 1):
            total_tests += 1
            if run_single_test(pipeline, q_data, total_tests):
                successful_tests += 1
                cat_success += 1
        
        # category summary
        print(f"{Colors.BOLD}Category Result: {cat_success}/{len(questions)} passed{Colors.END}")
    
    # final summary
    print_header("FINAL RESULTS")
    success_rate = (successful_tests / total_tests * 100) if total_tests > 0 else 0
    print(f"Total Tests Run: {total_tests}")
    print(f"Successful: {Colors.GREEN}{successful_tests}{Colors.END}")
    print(f"Failed: {Colors.RED}{total_tests - successful_tests}{Colors.END}")
    print(f"Success Rate: {Colors.BOLD}{success_rate:.1f}%{Colors.END}\n")

def run_category(category_name):
    """Run tests for just one category - useful for debugging"""
    test_data = load_questions()
    
    if category_name not in test_data:
        print(f"Category '{category_name}' not found!")
        print(f"Available: {', '.join(test_data.keys())}")
        return
    
    print_header(f"TESTING: {category_name.upper()}")
    pipeline = SolvraPipeline()
    
    questions = test_data[category_name]
    for i, q_data in enumerate(questions, 1):
        run_single_test(pipeline, q_data, i)

if __name__ == "__main__":
    # check if user wants to test specific category
    if len(sys.argv) > 1:
        category = sys.argv[1]
        run_category(category)
    else:
        # run all tests
        run_all_tests()
