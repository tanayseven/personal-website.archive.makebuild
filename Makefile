.DELETE_ON_ERROR:

export SHELL:=/bin/bash

NODE:=$(or $(shell which node), /usr/bin/node)
NPM:=$(or $(shell which npm), /usr/bin/npm)
MD:=markdown

POSTS_SRC:=$(wildcard posts/"*md")
OBJ_HTML:=$(patsubst %.md, %.html, $(POSTS_SRC))

.PHONY: build
build: $(OBJ_HTML)

www/blog/%.html:posts/%.md
	$(MD) $@ $^

clean:
	rm -rf www/

