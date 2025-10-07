# Contributing to Solvra

Thank you for your interest in contributing to Solvra! This document provides guidelines and best practices.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [Development Workflow](#development-workflow)
4. [Commit Guidelines](#commit-guidelines)
5. [Testing](#testing)
6. [Pull Request Process](#pull-request-process)
7. [Code Style](#code-style)

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Welcome newcomers and help them learn

## Getting Started

### Fork and Clone

```bash
# Fork the repo on GitHub, then:
git clone https://github.com/YOUR_USERNAME/Solvra.git
cd Solvra

# Add upstream remote
git remote add upstream https://github.com/Harshad2321/Solvra.git
```

### Set Up Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate it
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install dev dependencies
pip install pytest pytest-cov black flake8 isort
```

### Run Tests

```bash
# Unit tests
pytest tests/ -v

# Integration tests
python run_tests.py

# Check coverage
pytest tests/ --cov=src --cov-report=html
```

## Development Workflow

### 1. Create a Feature Branch

Use descriptive branch names following this pattern:

```bash
# Feature branches
git checkout -b feature/matrix-solver
git checkout -b feature/api-documentation

# Bug fix branches
git checkout -b bugfix/arithmetic-overflow
git checkout -b bugfix/unicode-handling

# Enhancement branches
git checkout -b enhance/performance-optimization
git checkout -b enhance/better-logging

# Documentation branches
git checkout -b docs/api-reference
git checkout -b docs/architecture-diagram
```

### 2. Make Changes

- Write clear, readable code
- Add docstrings to functions/classes
- Include inline comments for complex logic
- Update tests as needed

### 3. Test Your Changes

```bash
# Run relevant tests
python run_tests.py [category]

# Check for errors
python -c "from src.pipeline import SolvraPipeline; p = SolvraPipeline(); print(p.process_question('test question'))"
```

## Commit Guidelines

Follow [Conventional Commits](https://www.conventionalcommits.org/) format:

### Types

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting, no logic change)
- `refactor:` Code refactoring
- `test:` Adding/updating tests
- `chore:` Maintenance tasks

### Examples

```bash
# Good commit messages
git commit -m "feat: add matrix determinant solver"
git commit -m "fix: correct order of operations in arithmetic solver"
git commit -m "docs: update README with installation steps"
git commit -m "test: add test cases for quadratic equations"
git commit -m "refactor: extract common logic to helper function"

# Bad commit messages (avoid these)
git commit -m "update"
git commit -m "fix bugs"
git commit -m "changes"
```

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

Example:
```
feat(solver): add support for calculus problems

- Implemented derivative calculator
- Added integral solver with basic functions
- Included limit evaluation

Closes #42
```

## Testing

### Writing Tests

Place tests in the `tests/` directory:

```python
# tests/test_new_feature.py
import pytest
from src.solver import MathSolver

def test_matrix_determinant():
    solver = MathSolver()
    question = "Find determinant of [[1,2],[3,4]]"
    result = solver.solve(question, {'type': 'arithmetic'})
    assert result['answer'] == -2

def test_invalid_input():
    solver = MathSolver()
    with pytest.raises(ValueError):
        solver.solve("", {'type': 'invalid'})
```

### Running Specific Tests

```bash
# Single test file
pytest tests/test_solver.py -v

# Single test function
pytest tests/test_solver.py::test_matrix_determinant -v

# With coverage
pytest tests/ --cov=src --cov-report=term-missing
```

## Pull Request Process

### 1. Update Your Branch

```bash
# Fetch latest changes
git fetch upstream

# Rebase on main
git rebase upstream/main

# Resolve conflicts if any, then:
git add .
git rebase --continue
```

### 2. Push Your Branch

```bash
git push origin feature/your-feature-name
```

### 3. Create Pull Request

On GitHub:
1. Click "New Pull Request"
2. Select your branch
3. Fill in the template:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-reviewed code
- [ ] Commented complex sections
- [ ] Updated documentation
- [ ] No new warnings
- [ ] Added tests
- [ ] All tests pass
```

### 4. Code Review

- Address reviewer comments
- Make requested changes
- Push updates to same branch

### 5. Merge

Once approved, maintainers will merge your PR.

## Code Style

### Python Style Guide

Follow [PEP 8](https://pep8.org/) with these additions:

```python
# Line length: 100 characters max
# Use Black for formatting
black src/ --line-length 100

# Sort imports with isort
isort src/

# Check with flake8
flake8 src/ --max-line-length=100
```

### Docstring Format

Use Google-style docstrings:

```python
def solve_quadratic(a, b, c):
    """Solve quadratic equation ax^2 + bx + c = 0.
    
    Args:
        a (float): Coefficient of x^2
        b (float): Coefficient of x
        c (float): Constant term
        
    Returns:
        tuple: Two solutions (x1, x2)
        
    Raises:
        ValueError: If a = 0 (not a quadratic equation)
        
    Example:
        >>> solve_quadratic(1, -5, 6)
        (3.0, 2.0)
    """
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero")
    
    discriminant = b**2 - 4*a*c
    x1 = (-b + discriminant**0.5) / (2*a)
    x2 = (-b - discriminant**0.5) / (2*a)
    
    return (x1, x2)
```

### Error Handling

Always handle errors gracefully:

```python
# Good
try:
    result = risky_operation()
except SpecificException as e:
    logger.error(f"Failed: {e}")
    return {'answer': None, 'error': str(e)}

# Bad
try:
    result = risky_operation()
except:
    pass
```

## Adding New Features

### 1. Solver Functions

Add to `src/solver.py`:

```python
def solve_new_type(self, question, plan):
    """Solve problems of new type.
    
    Args:
        question (str): The problem text
        plan (dict): Planning information
        
    Returns:
        dict: Answer and solving steps
    """
    steps = []
    
    # Your logic here
    steps.append("Step 1: Extract data")
    
    return {'answer': result, 'steps': steps}
```

### 2. Test Cases

Add to `test_cases.json` or create new category:

```json
{
  "new_category": [
    {
      "question": "Sample problem",
      "expected_answer": "Expected result",
      "type": "new_category",
      "difficulty": "medium"
    }
  ]
}
```

### 3. Documentation

Update:
- `PROBLEM_TYPES.md` - Add to supported types
- `README.md` - Update features list
- `CHANGELOG.md` - Document changes

## Questions?

- Open an issue for bugs or feature requests
- Start a discussion for questions
- Check existing docs in `docs/` folder

Thank you for contributing to Solvra! 🎉
