# Changelog

All notable changes to Solvra will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- GitHub Actions CI/CD pipeline for automated testing
- Comprehensive error handling in solver modules
- Examples directory with sample problems
- API documentation
- Version tagging and changelog

## [0.2.0] - 2025-10-07

### Added
- Enhanced arithmetic solver with SymPy expression evaluation
- Proper order of operations (PEMDAS/BODMAS) support
- Specialized word problem handlers:
  - Distance/Speed/Time calculations
  - Relative motion (two trains/objects)
  - Discount and percentage problems
  - Depreciation calculations
  - Multi-step arithmetic problems
  - Consecutive numbers solver
- Classification forwarding mechanism
- Comprehensive test suite with 28 test cases
- Interactive test runner (`run_tests.py`)
- Detailed testing guide (TESTING_GUIDE.md)
- Solver improvements documentation

### Changed
- Arithmetic solver now uses SymPy for expression evaluation
- Word problem solver with 6 specialized handlers
- Improved numerical accuracy from ~50% to ~85%

### Fixed
- Order of operations in arithmetic expressions
- Distance/speed/time calculations in word problems
- Discount calculations
- Multi-step word problems

## [0.1.0] - 2025-10-06

### Added
- Base Solvra architecture with modular design
- Question classifier using Random Forest (100% validation accuracy)
- Planning module for step-by-step reasoning
- Core solver with 7 problem types:
  - Arithmetic
  - Algebra
  - Geometry
  - Logic
  - Word Problems
  - Comparison
  - Pattern Recognition
- Solution verifier with confidence scoring
- Reasoning trace recorder
- Streamlit web interface
- Advanced problem solvers:
  - Nested radicals
  - Heron's formula for triangles
  - Parametric equations
  - Circle segment areas
  - Work rate problems
  - Logic puzzles with constraints
  - Inequality proofs
  - Non-homogeneous recurrence relations
  - Diophantine equations
  - Hyperbola locus problems
  - Constrained optimization
- Ultra-complex solvers:
  - Matrix operations (determinant, eigenvalues, trace)
  - Calculus (derivatives, integrals, limits)
  - Number theory (GCD, LCM, primes, modular arithmetic)
  - Combinatorics (permutations, combinations)
  - Complex numbers (magnitude, argument)
  - Trigonometry (sin, cos, tan)
- Comprehensive documentation:
  - README with quickstart
  - PROBLEM_TYPES.md (30+ problem types)
  - ENHANCEMENTS.md
  - ADVANCED_ENHANCEMENTS.md
  - PROJECT_COMPLETE.md
  - Technical report

### Changed
- Fixed recurrence relation bug (a_10 = 341 vs 512)

### Performance
- Classifier: 100% validation accuracy
- Test dataset: 72.86% accuracy on 100 samples
- Ultra-complex tests: 100% success rate (24/24 problems)
- Advanced tests: 80% success rate (8/10 problems)

## [0.0.1] - 2025-10-05

### Added
- Initial project setup
- Basic dataset with 600 samples
- Train/test split (500/100)
- Core module structure

---

## Version Numbering

- **MAJOR** version: Incompatible API changes
- **MINOR** version: New functionality in backwards-compatible manner
- **PATCH** version: Backwards-compatible bug fixes

## Links

- [GitHub Repository](https://github.com/Harshad2321/Solvra)
- [Issues](https://github.com/Harshad2321/Solvra/issues)
- [Pull Requests](https://github.com/Harshad2321/Solvra/pulls)
