# Contributing to CPC2-wrapper

Thank you for your interest in contributing to CPC2-wrapper! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for all contributors.

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed and expected**
- **Include screenshots if helpful**
- **Specify your environment** (OS, Python version, package versions)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the steps**
- **Describe the current behavior and expected behavior**
- **Explain why this enhancement would be useful**

### Pull Requests

1. **Fork the repository** and create your branch from `master`
2. **Make your changes** with clear commit messages
3. **Add tests** if you've added code that should be tested
4. **Update documentation** if you've changed functionality
5. **Ensure the test suite passes**
6. **Submit a pull request**

## Development Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

```bash
# Clone your fork
git clone https://github.com/your-username/CPC2-wrapper.git
cd CPC2-wrapper

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .[dev]
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=cpc2 tests/

# Run specific test file
pytest tests/test_compress.py
```

### Code Style

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to all public functions and classes
- Keep functions focused and concise (max 50 lines)
- Use type hints for better code documentation

### Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

## Project Structure

```
CPC2-wrapper/
├── CPC2.py              # Main entry point
├── cpc2/                # Package modules
│   ├── __init__.py
│   ├── compress.py      # File compression utilities
│   ├── seqio.py         # Sequence I/O utilities
│   └── data/            # Model and range files
├── tests/               # Test suite
├── docs/                # Documentation
├── requirements.txt     # Dependencies
├── setup.py            # Package setup
└── README.md           # Project overview
```

## Questions?

Feel free to open an issue with the label "question" or contact the maintainer at yuelong.chen.btr@gmail.com.

## License

By contributing, you agree that your contributions will be licensed under the GPL V3 License.
