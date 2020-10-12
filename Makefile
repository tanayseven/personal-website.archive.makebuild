# All the power to build the website
# May the force be with you

# Tools needed for building
VALIDATOR:=java -jar ./bin/vnu.jar
BUILT_FILES:=$(shell find _build/ -name "*.html")
PYTHON:=$(or $(shell which python3), /usr/bin/python3)

# Self written python scripts that take some actions
COMPILE_SCRIPT:=./website/compile.py
IMAGE_RESIZE_SCRIPT:=./website/resize_image.py

# Create dir script which creates directory for a path without the file at the end of the path
CREATE_DIR = mkdir -p `echo $@ | sed -r "s/(.+)\/.+/\1/"`

# Source directories
DEPENDENT_TEMPLATES:=./templates/base.html.j2 $(shell find ./templates/components/ -name "*.html.j2") _build/main.css _build/main.js
BLOG_OUTPUT:=$(shell awk -F ',' '{if (NR!=1) {print "_build/blog/" $$1 ".html"}}' blog_list.csv)
IMAGES_LIST:=$(patsubst res/images/%, _build/out/images/%, $(shell find res/images -name "*.png" -or -name "*.jpg" -or -name "*.json" -or -name "*.svg"))

# Destination directories
FILES_TO_BE_BUILT := _build/index.html _build/blog/ _build/main.css _build/main.js _build/dracula.css _build/highlight.js _build/.nojekyll $(BLOG_OUTPUT)
GP_REPO_PATH:=tanayseven.github.io/

all: ## will clean the _build/ directory"
	make clean && make build && make verify

$(GP_REPO_PATH):
	git clone git@github.com:tanayseven/tanayseven.github.io.git

.ONESHELL:
_build/%/: ./templates/%.html.j2
	mkdir -p $@
	touch $(dir $@)
	$(PYTHON) $(COMPILE_SCRIPT) --template=$^ > $@/index.html

_build/blog/%.html: ./templates/blog/%.html.j2
	$(PYTHON) $(COMPILE_SCRIPT) --title="$(shell awk -F ',' -v cmp="$*" '{if ($$1==cmp) {la=$$2}} END {print la}' blog_list.csv)" --template=$^ > $@

.ONESHELL:
_build/blog/: ./templates/blog.html.j2
	mkdir -p $@ 
	$(PYTHON) $(COMPILE_SCRIPT) --template=$^ --file=blog_list.csv > $@/index.html

.ONESHELL:
_build/%.html: ./templates/%.html.j2
	$(CREATE_DIR) && $(PYTHON) $(COMPILE_SCRIPT) --template=$^ --file=blog_list.csv  > $@

.PRECIOUS: _build/%.css
_build/%.css: ./res/%.css
	$(CREATE_DIR) && cp $^ $@

.PRECIOUS: _build/%.js
_build/%.js: ./res/%.js
	$(CREATE_DIR) && cp $^ $@

.PRECIOUS: _build/contact_form.txt
_build/contact_form.txt: ./res/contact_form.txt
	$(CREATE_DIR) && cp $^ $@

.PRECIOUS: _build/.nojekyll
_build/.nojekyll:
	$(CREATE_DIR) touch _build/.nojekyll

_build/out/images/%: res/images/%
	$(CREATE_DIR) && $(PYTHON) $(IMAGE_RESIZE_SCRIPT) --input=$^ --output=$@

.PHONY: sync_images
.ONESHELL:
sync_images: $(IMAGES_LIST)
	mkdir -p _build/res/images/
	rsync -avzh _build/out/images/* _build/res/images/

.PHONY: build
.ONESHELL:
build: $(FILES_TO_BE_BUILT) sync_images  ## will compile the website into a static website in the _build/ directory"

.PHONY: buildWatch
.ONESHELL:
buildWatch:
	watch make build

.PHONY: serve
.ONESHELL:
serve: build  ## will start a local server and start serving the files from _build/ directory as a static website
	cd _build/ \
	&& $(PYTHON) -m http.server 3000

.PHONY: clean
clean::
	$(RM) -rf _build/

.PHONY: verify
verify:   ## will verify if the built website adheres to the HTML5 standard
	$(VALIDATOR) --skip-non-html $(BUILT_FILES)

.PHONY: deploy
.ONESHELL:
deploy: $(GP_REPO_PATH) build verify  ## will deploy the website to the github pages hosting
	rsync -avzh _build/* $(GP_REPO_PATH)  && \
	cd $(GP_REPO_PATH) && \
	git add . && \
	git commit -m "$$(git status --porcelain)" || echo "Nothing new in the branch, nothing will be deployed" && \
	git push

help:   ## will print this help
	@echo '** Make targets **'
	@grep '^[a-zA-Z]' $(MAKEFILE_LIST) | \
    sort | \
    awk -F ':.*?## ' 'NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'
