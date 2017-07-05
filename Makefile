PYTEST = /usr/bin/env pytest
PYTHON = /usr/bin/env python2
PIP = /usr/bin/env pip2
.PHONY = clean deploy doc doc-server install requirements test

all: clean requirements doc test

clean:
	rm -rf .coverage
	rm -rf *.egg-info
	rm -rf build
	rm -rf cover
	rm -rf dist
	rm -rf homekeeper/*.pyc
	rm -rf homekeeper/__pycache__
	rm -rf lib

deploy: clean doc test
	${PYTHON} setup.py sdist upload -r homekeeper

doc:
	pydoc -w homekeeper

doc-server:
	pydoc -p 8080 -w homekeeper

install: clean requirements
	${PIP} install --upgrade .

requirements:
	${PIP} install -r requirements.txt

test:
	pytest --cov=homekeeper homekeeper/
