run:
	python3 -m src.main

cli:
	python3 -m src.cli

test:
	pytest

install:
	pip install -r requirements.txt
