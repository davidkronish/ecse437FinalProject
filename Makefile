run:
	python3 main.py

test:
	py.test tests

setup: requirements.txt
	pip install -r requirements.txt

clean:
	rm -rf __pycache__

