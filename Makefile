.DELETE_ON_ERROR:

export SHELL:=/bin/bash

NODE:=$(or $(shell which node), /usr/bin/node)
NPM:=$(or $(shell which npm), /usr/bin/npm)
MD:=$(or $(shell which showdown), /usr/local/bin/showdown)

POSTS_SRC:=$(wildcard posts/*md)
OBJ_HTML:=$(patsubst posts/%.md, www/blog/%.html, $(POSTS_SRC))

.PHONY: build
build: $(OBJ_HTML) | checktools

www/blog/%.html:posts/%.md
	mkdir -p $(dir $@)
	$(MD) makehtml -i $^ -o $@

.PHONY: clean
clean:
	rm -rf www/

.PHONY: checktools
checktools: | $(NODE) $(NPM) $(MD)

$(NODE):
	sudo apt-get install nodejs-legacy

$(NPM):
	sudo apt-get install npm

$(MD): # TODO fix this
	sudo npm install -g showdown@1.6.4

