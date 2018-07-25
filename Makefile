export SHELLOPTS:=$(SHELLOPTS):pipefail

VALIDATOR:=java -jar ./bin/vnu.jar
BUILT_FILES:=$(shell find _build/ -name "*.html")
PYTHON:=$(or $(shell which python3), /usr/bin/python3)
GP_REPO_PATH:=tanayseven.github.io/

COMPILE_SCRIPT:=./website/compile.py
IMAGE_RESIZE_SCRIPT:=./website/resize_image.py
TABLE_TO_JSON:=./website/table_to_json.py

DEPENDENT_TEMPLATES:=./templates/base.html $(shell find ./templates/components/ -name "*.html") _build/main.css _build/main.js
BLOG_OUTPUT:=$(shell awk -F ',' '{if (NR!=1) {print "_build/blog/" $$1 ".html"}}' blog_list.csv)
IMAGES_PNG:=$(patsubst res/images/%, _build/out/images/%, $(shell find res/images -name "*.png" -or -name "*.jpg"))

$(GP_REPO_PATH):
	git clone git@github.com:tanayseven/tanayseven.github.io.git

_build/:
	mkdir -p _build/

.ONESHELL:
_build/%/: ./templates/%.html
	mkdir -p $@
	touch $(dir $@)
	$(PYTHON) $(COMPILE_SCRIPT) --template=$^ > $@/index.html

_build/blog/%.html: ./templates/blog/%.html
	$(PYTHON) $(COMPILE_SCRIPT) --title="$(shell awk -F ',' -v cmp="$*" '{if ($$1==cmp) {la=$$2}} END {print la}' blog_list.csv)" --template=$^ > $@

.ONESHELL:
_build/blog/: ./templates/blog.html
	mkdir -p $@
	touch $(dir $@)
	$(PYTHON) $(COMPILE_SCRIPT) --template=$^ --file=blog_list.csv > $@/index.html

.ONESHELL:
_build/%.html: ./templates/%.html
	touch $(dir $@)
	$(PYTHON) $(COMPILE_SCRIPT) --template=$^ > $@

.PRECIOUS: _build/main.%
_build/main.%: ./res/main.%
	cp $^ $@

_build/out/images/%: res/images/%
	mkdir -p $@
	rmdir $@
	$(PYTHON) $(IMAGE_RESIZE_SCRIPT) --input=$^ --output=$@

.PHONY: sync_images
ONESHELL:
sync_images: $(IMAGES_PNG)
	mkdir -p _build/res/images/
	rsync -avzh _build/out/images/* _build/res/images/

.PHONY: website
website: _build/index.html _build/resume/ _build/blog/ _build/about/ sync_images _build/main.css _build/main.js $(BLOG_OUTPUT)

.PHONY: build
.ONESHELL:
## Will compile all the newer changes and accordingly update the files in the _build/ directory
build: _build/ website

.PHONY: serve
.ONESHELL:
## Will start a server on a given port with the static site available for testing
serve: _build/ website
	cd _build/ \
	&& $(PYTHON) -m http.server

.PHONY: clean
## To remove all the generated files (DO NOT USE THIS GENERATED FILES ARE NEEDED FOR FASTER BUILDS)
clean::
	$(RM) -rf _build/

.PHONY: verify
## To verify if all the generated files follow the HTML5 standard or not
verify:
	$(VALIDATOR) $(BUILT_FILES)

.PHONY: deploy
.ONESHELL:
## To deploy the website on Github Pages
deploy: $(GP_REPO_PATH)
	rsync -avzh _build/* $(GP_REPO_PATH)
	cd $(GP_REPO_PATH)
	git add .
	git commit -m "$$(git status --porcelain)"
	git push

-include .makehelp/include/makehelp/Help.mak

ifeq "help" "$(filter help,$(MAKECMDGOALS))"
.makehelp/include/makehelp/Help.mak:
	git clone --depth=1 https://github.com/christianhujer/makehelp.git .makehelp
endif

$(PYTHON):
	sudo apt-get install python3
