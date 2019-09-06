### Code quality readme file

Here are the list of tools used for code quality

Linting: pylava
Code complexity: radon
Unit test: Pytest
Code coverage: pytest-cov (coverage)

#### Run pytest, linting and coverage
python -m pytest --pylava --cov=. -v --cov-report=term-missing
Documentation: https://pytest-cov.readthedocs.io/en/latest/reporting.html

#### Run radon
radon cc <filename.py> -sa
Documentation: https://radon.readthedocs.io/en/latest/commandline.html
