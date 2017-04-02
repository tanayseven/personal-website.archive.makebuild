.DELETE_ON_ERROR:

export SHELL:=/bin/bash

NODE:=$(or $(shell which node), /usr/bin/node)
NPM:=$(or $(shell which npm), /usr/bin/npm)
MARKDOWN:=$(or $(shell which markdown), /usr/bin/markdown)

POST_FILES:=$(shell find posts/ -name "*.md")

.PHONY: build
build:  www/blog/2016-03-27-hello-world.html

www/blog/%.html:posts/%.md
	$(MARKDOWN) $@ @^

clean:
	rm -rf www/