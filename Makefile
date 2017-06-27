.DELETE_ON_ERROR:

export SHELL:=/bin/bash

NODE:=$(or $(shell which node), /usr/bin/node)
NPM:=$(or $(shell which npm), /usr/bin/npm)
MD:=$(or $(shell which mdtrans), /usr/local/bin/mdtrans)

POSTS_SRC:=$(wildcard posts/*md)
OBJ_HTML:=$(patsubst posts/%.md, www/blog/%.html, $(POSTS_SRC))
RESULTANT_HTML:=$(dirname $(./blog_path www/blog/%.html))

.PHONY: all
all: clean build

.PHONY: build
build: checktools www/blog $(OBJ_HTML) $(RESULT_HTML)

www/blog/%.html: posts/%.md
	$(MD) makehtml -i $^ > $@
	#$(mkdir -p $(dirname $(./blog_path.py $@)))
	#$(echo $(./blog_path $@))
	#$(mkdir -p $(dirname $(./blog_path $@)))

www/blog:
	mkdir -p www/blog

todirectory(%): www/blog/%.html
	mkdir -p $(dir $(./blog_path.py $^))

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
