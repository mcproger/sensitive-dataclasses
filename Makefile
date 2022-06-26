test:
	pytest -svv tests/
lint:
	flake8 .
check:
	make lint test
