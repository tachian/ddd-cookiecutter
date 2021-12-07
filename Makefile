clean:
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	rm -f .coverage

test: clean
	pytest tests/ -s -v

coverage: clean
	pytest tests/ -s -v --cov=lists --cov-branch --cov-report=term --cov-report=html --junitxml=test_reports/junit.xml
