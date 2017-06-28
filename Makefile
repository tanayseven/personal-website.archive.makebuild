.DELETE_ON_ERROR:

export SHELL:=/bin/bash

NODE:=$(or $(shell which node), /usr/bin/node)
NPM:=$(or $(shell which npm), /usr/bin/npm)
MD:=$(or $(shell which mdtrans), /usr/local/bin/mdtrans)

POSTS_SRC:=$(wildcard posts/*md)
OBJ_HTML:=$(patsubst posts/%.md, www/blog/%.html, $(POSTS_SRC))
RESULTANT_HTML:=$(patsubst www/blog/%.html, $(./blog_path www/blog/%.html), $(OBJ_HTML))

.PHONY: all
all: build

.PHONY: build
build: $(OBJ_HTML) $(RESULTANT_HTML)

www/blog/%.html: posts/%.md www/blog
	$(MD) $^ > $@

www/blog:
	mkdir -p www/blog

$(./blog_path www/blog/%.html): www/blog/%.html
	mkdir -p $(dirname $(./blog_path.py $@))
	mv $^ $@

.PHONY: todirectory(%)
todirectory(%): www/blog/%.html
	mkdir -p $(dirname $(./blog_path.py $^))
	mv $^ $(./blog_path.py S^)

.PHONY: clean
clean:
	rm -rf www/

.PHONY: checktools
checktools: $(NODE) $(NPM) $(MD)

$(NODE):
	sudo apt-get install nodejs-legacy

$(NPM):
	sudo apt-get install npm

$(MD):
	npm install -g mdtrans

deploy: deploy.sh
	$(SHELL) deploy.sh
