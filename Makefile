export SHELLOPTS:=$(SHELLOPTS):pipefail

VALIDATOR:=$(or $(shell which html5validator), /usr/bin/html5validator)
PYTHON:=$(or $(shell which python3), /usr/bin/python3)
GP_REPO_PATH:=$(~/projects/tanayseven.github.io)

COMPILE_SCRIPT:=./website/compile.py

DEPENDENT_TEMPLATES:=./templates/base.html $(shell find ./templates/components/ -name "*.html") _build/main.css _build/main.js

_build/:
	mkdir -p _build/

.ONESHELL:
_build/%/: ./templates/%.html $(DEPENDENT_TEMPLATES)
	mkdir -p $@
	touch $(dir $@)
	$(PYTHON) $(COMPILE_SCRIPT) $^ > $@index.html

.ONESHELL:
_build/%.html: ./templates/%.html $(DEPENDENT_TEMPLATES)
	touch $(dir $@)
	$(PYTHON) $(COMPILE_SCRIPT) $^ > $@

.PRECIOUS: _build/main.%
_build/main.%: ./res/main.%
	cp $^ $@

.PHONY: website
website: _build/index.html _build/resume/ _build/blog/ _build/about/

.PHONY: build
.ONESHELL:
## Will compile all the newer changes and accordingly update the files in the _build/ directory
build: _build/ website

.PHONY: serve
.ONESHELL:
## Will start a server on a given port with the static site available for testing
serve: _build/ website
	cd _build/
	$(PYTHON) -m http.server

.PHONY: clean
## To remove all the generated files (DO NOT USE THIS GENERATED FILES ARE NEEDED FOR FASTER BUILDS)
clean::
	$(RM) -rf _build/

.PHONY: verify
## To verify if all the generated files follow the HTML5 standard or not
verify:
	$(VALIDATOR) --root _build/

.PHONY: deploy
.ONESHELL:
## To deploy the website on Github Pages
deploy:
	cp -rf _build/* $(GP_REPO_PATH)
	cd $(GP_REPO_PATH)
	git commit
	git pull --rebase
	git push

-include .makehelp/include/makehelp/Help.mak

ifeq "help" "$(filter help,$(MAKECMDGOALS))"
.makehelp/include/makehelp/Help.mak:
	git clone --depth=1 https://github.com/christianhujer/makehelp.git .makehelp
endif

$(VALIDATOR):
	pip install -U html5validator

$(PYTHON):
	sudo apt-get install python3
