run: setup
	python3 blackjack/main.py

runtest: setup
	(cd blackjack/tests && pytest test.py)

build: setup
	pyinstaller blackjack/main.py

setup: requirements.txt
	python3 -m pip install -r requirements.txt
lint:
	python3 -m pylint --disable=C,R,E blackjack
clean:
	rm -rf __pycache__

