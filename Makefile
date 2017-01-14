.PHONY: tests setup
SHELL := /usr/bin/env bash +e

.SILENT: all
all: setup run

clean:
	rm -rf ./env

init:
	virtualenv --no-site-packages env
	source ./env/bin/activate
	pip install --requirement requirements-dev.txt

setup: clean init install

help:
	python mpain/main.py --help

run:
	python mpain/main.py

%:
	python setup.py $*
