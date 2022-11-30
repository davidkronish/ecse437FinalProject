run:
	python3 main.py

runtest:
	(cd test;python3 -m unittest)

setup: requirements.txt
	pip install -r requirements.txt

clean:
	rm -rf __pycache__

