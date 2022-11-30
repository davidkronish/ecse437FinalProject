run:
	python3 main.py

test:
	python3 -m test/unittest

setup: requirements.txt
	pip install -r requirements.txt

clean:
	rm -rf __pycache__

