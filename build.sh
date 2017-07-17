#!/usr/bin/env bash

# List of all the global paths needed for the build
export PAGES_PATH='src/pages'
export SCRIPT_PATH='src/'
export OUTPUT_PATH='www/'
BLOG='blog/'
RES='res/'
FONTS='fonts/'
export BLOG_PATH="$OUTPUT_PATH$BLOG"
export RES_PATH="$OUTPUT_PATH$RES"
export FONTS_PATH="$OUTPUT_PATH$FONTS"

# Create the output directories
mkdir -p "$BLOG_PATH" "$FONTS_PATH"

# Build all the static files into one single file
python ./src/combine_static.py ./src/static/ css "$OUTPUT_PATH$RES"
cp ./src/static/fonts/* "$FONTS_PATH"
cp ./src/.htaccess "$OUTPUT_PATH"

# Build the home page which is the index.html page
INDEX='index.html'
python src/build_index.py >"$OUTPUT_PATH$INDEX"

# Build all the pages from the blog here
for filename in src/pages/posts/*.html; do
    echo "$filename"
    ./blog-build.sh "$filename"
done
wait
