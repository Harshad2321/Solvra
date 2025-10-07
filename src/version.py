"""Solvra version information."""

__version__ = "0.2.0"
__author__ = "Harshad"
__license__ = "MIT"
__description__ = "Agentic Mathematical Reasoning System"

# Version history
VERSION_INFO = {
    "0.2.0": {
        "date": "2025-10-07",
        "changes": [
            "Enhanced arithmetic solver with SymPy expression evaluation",
            "Added 6 specialized word problem handlers",
            "Proper order of operations (PEMDAS/BODMAS) support",
            "Comprehensive test suite with 28 test cases",
            "CI/CD pipeline with GitHub Actions",
            "Examples directory with sample problems"
        ]
    },
    "0.1.0": {
        "date": "2025-10-06",
        "changes": [
            "Initial release with core functionality",
            "7 problem type solvers",
            "30+ specialized problem handlers",
            "Streamlit web interface",
            "Random Forest classifier"
        ]
    }
}

def get_version():
    """Return current version string."""
    return __version__

def print_version_info():
    """Print version information."""
    print(f"Solvra v{__version__}")
    print(f"Author: {__author__}")
    print(f"License: {__license__}")
    print(f"\n{__description__}")

if __name__ == "__main__":
    print_version_info()
