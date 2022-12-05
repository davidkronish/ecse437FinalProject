run: setup
	python3 blackjack/main.py

runtest: setup
	(cd blackjack/tests && pytest test.py)

build: setup
	pyinstaller blackjack/main.py

setup: requirements.txt
	python -m pip install -r requirements.txt
lint:
	pylint blackjack
clean:
	rm -rf __pycache__

