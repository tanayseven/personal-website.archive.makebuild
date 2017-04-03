.DELETE_ON_ERROR:

export SHELL:=/bin/bash

NODE:=$(or $(shell which node), /usr/bin/node)
NPM:=$(or $(shell which npm), /usr/bin/npm)
MARKDOWN:=$(or $(shell which markdown))

POST_FILES:=$(shell find posts/ -name "*.md")

www/blog/%.html:posts/%.md
	echo "$@ @^"

build:
	$(patsubst posts/%.md, www/blog/%.html, $(POST_FILES))

clean:
	rm -rf www/

