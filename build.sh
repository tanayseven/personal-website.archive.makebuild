#!/usr/bin/env bash

# List of all the global paths needed for the build
export PAGES_PATH='src/pages'
export SCRIPT_PATH='src/'
export OUTPUT_PATH='www/'
BLOG='blog/'
RES='res/'
export BLOG_PATH="$OUTPUT_PATH$BLOG"
export RES_PATH="$OUTPUT_PATH$RES"

# Create the output directories
mkdir -p "$BLOG_PATH"

# Build all the static files into one single file
python ./src/combine_static.py ./src/static/ css www/res/

# Build the home page which is the index.html page
INDEX='index.html'
python src/build_index.py >"$OUTPUT_PATH$INDEX"

# Build all the pages from the blog here
for filename in posts/*.md; do
    ./blog-build.sh "$filename" &
done

wait
