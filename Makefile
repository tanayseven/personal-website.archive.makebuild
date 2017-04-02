.DELETE_ON_ERROR:

export SHELL:=/bin/bash

NODE:=$(or $(shell which node), /usr/bin/node)
NPM:=$(or $(shell which npm), /usr/bin/npm)
MARKDOWN:=$(or $(shell which markdown), /usr/bin/markdown)

POST_FILES:=$(shell find posts/ -name "*.md")

.PHONY: build
build: |
	for POST in $POST_FILES; do \
		echo $$POST ; \
	done
