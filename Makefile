test:
	pytest -svv tests/
lint:
	flake8 .
isort:
	isort .
check:
	make lint isort test
