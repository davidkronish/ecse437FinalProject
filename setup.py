from setuptools import setup

setup(
    name='437Blackjack',
    version='1.0.0',
    author='David Kronish',
    author_email='david.kronish@mail.mcgill.ca',
    packages=['blackjack', 'blackjack.tests'],
    setup_requires = ['pytest-runner','pytest-pylint'],
    install_requires = ["pytest", "pylint"],
    scripts=['bin/blackjack_script.py'],
)