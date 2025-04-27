# Makefile app/ (Python/Poetry)

PYTHON_EXEC=poetry run python

install:
	poetry install

update:
	poetry update

lock:
	poetry lock

test:
	$(PYTHON_EXEC) -m pytest

lint:
	poetry run flake8 .

clean:
	find . -type d -name '__pycache__' -exec rm -r {} +
	rm -rf .mypy_cache .pytest_cache *.pyc *.pyo *.pyd .coverage htmlcov