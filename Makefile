test:
	pytest --cov=src ./

test-coverage:
	pytest --cov=src ./ --cov-report=xml
