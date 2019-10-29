.PHONY: help prepare-dev test lint

VENV_NAME?=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python3

.DEFAULT: help
help:
	@echo "make prepare-dev"
	@echo "    Create python virtual environment and install dependencies."
	@echo "make lint"
	@echo "    Run list on project."
	@echo "make test"
	@echo "    Run tests on project."
	@echo "make run"
	@echo "    Run server."
	@echo "make clean"
	@echo "    Remove python artifacts and virtualenv."
	@echo "make build"
	@echo "    Creates debian package."
	@echo "make install"
	@echo "    Installs package in your system."

prepare-dev: 
	which python3 || apt install -y python3 python3-pip
	which virtualenv || python3 -m pip install virtualenv
	make venv

# Requirements are in setup.py, so whenever setup.py is changed, re-run installation of dependencies.
venv: 
	cp .secrets.toml.sample .secrets.toml
	test -d $(VENV_NAME) || virtualenv -p python3 $(VENV_NAME)
	pip install -r requirements.txt
	touch $(VENV_NAME)/bin/activate


test: venv
	${PYTHON} -m pytest -vv tests

lint: venv
	${PYTHON} -m pylint client 

doc: venv
	$(VENV_ACTIVATE) && cd docs; make html

clean: 
	rm -rf $(VENV_NAME) *.eggs *.egg-info dist build docs/_build .cache