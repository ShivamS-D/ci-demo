# CI Demo — Learning Project

A simple Python calculator project that demonstrates a real CI pipeline using GitHub Actions.

## Project Structure

```
ci-demo/
├── .github/workflows/ci.yml   ← CI pipeline (runs on every push)
├── src/calculator.py          ← App code
├── tests/test_calculator.py   ← Tests
└── requirements.txt           ← Dependencies
```

## CI Pipeline

Every push to GitHub automatically runs:

1. **Lint** — flake8 checks code style
2. **Tests** — pytest runs all 9 tests
3. **Coverage** — fails if less than 80% of code is tested

## Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/

# Run tests with coverage
pytest tests/ --cov=src --cov-report=term-missing

# Run linter
flake8 src/ tests/
```
