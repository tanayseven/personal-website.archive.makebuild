# export SHELLOPTS:=$(SHELLOPTS):pipefail

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
	$(PYTHON) $(COMPILE_SCRIPT) --template=$^ --file=blog_list.csv  > $@

.PRECIOUS: _build/%.css
_build/%.css: ./res/%.css
	cp $^ $@

.PRECIOUS: _build/%.js
_build/%.js: ./res/%.js
	cp $^ $@

.PRECIOUS: _build/contact_form.txt
_build/contact_form.txt: ./res/contact_form.txt
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
website: _build/index.html _build/blog/ sync_images _build/main.css _build/main.js _build/dracula.css _build/highlight.js $(BLOG_OUTPUT)

.PHONY: build
.ONESHELL:
build: _build/ website

.PHONY: serve
.ONESHELL:
serve: _build/ website
	cd _build/ \
	&& $(PYTHON) -m http.server 3000

.PHONY: clean
clean::
	$(RM) -rf _build/

.PHONY: verify
verify:
	$(VALIDATOR) --skip-non-html $(BUILT_FILES)

.PHONY: deploy
.ONESHELL:
deploy: $(GP_REPO_PATH)
	rsync -avzh _build/* $(GP_REPO_PATH)  && \
	cd $(GP_REPO_PATH) && \
	git add . && \
	git commit -m "$$(git status --porcelain)" && \
	git push

$(PYTHON):
	sudo apt-get install python3

help:
	@echo "MAKE TARGETS:"
	@echo "build  : will compile the website into a static website in the _build/ directory"
	@echo "clean  : will clean the _build/ directory"
	@echo "deploy : will deploy the website to the github pages hosting"
	@echo "serve  : will start a local server and start serving the files from _build/ directory as a static website"
	@echo "verify : will verify if the built website adheres to the HTML5 standard"
