# StatQuest Python Learning Project

This project is set up with Poetry for dependency management and includes configurations for Python development with VS Code.

## Setup

1. Make sure you have Poetry installed:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

## Project Structure

```
statquest/
├── src/
│   └── statquest/
│       └── __init__.py
├── tests/
├── notebooks/
├── data/
├── .vscode/
│   ├── launch.json
│   └── settings.json
├── pyproject.toml
└── README.md
```

## Development

- Run tests: `poetry run pytest`
- Format code: `poetry run black .`
- Lint code: `poetry run flake8`
- Type checking: `poetry run mypy src/`

## VS Code Integration

This project includes VS Code configurations for:
- Python debugging
- Integrated terminal with Poetry environment
- Code formatting and linting
- Jupyter notebook support
