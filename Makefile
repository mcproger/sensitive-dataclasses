test:
	pytest -svv --cov . --cov-report xml tests/
lint:
	flake8 .
isort:
	isort .
types:
	mypy sensitive_dataclasses/
check:
	make lint isort types test
