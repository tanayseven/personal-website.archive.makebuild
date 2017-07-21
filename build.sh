#!/usr/bin/env bash

# List of all the global paths needed for the build
export PAGES_PATH='src/pages/'
export SCRIPT_PATH='src/'
export OUTPUT_PATH='www/'
BLOG='blog/'
RES='res/'
FONTS='fonts/'
IMAGES='images/'
export BLOG_PATH="$OUTPUT_PATH$BLOG"
export RES_PATH="$OUTPUT_PATH$RES"
export FONTS_PATH="$OUTPUT_PATH$FONTS"
export RESUME_PATH=$OUTPUT_PATH"resume/"
export ABOUT_PATH=$OUTPUT_PATH"about/"
export IMAGE_PATH="$OUTPUT_PATH$RES$IMAGES"

# Create the output directories
mkdir -p "$BLOG_PATH" "$FONTS_PATH" "$RES_PATH" "$RESUME_PATH" "$ABOUT_PATH" "$IMAGE_PATH"

# Build all the static files into one single file
python ./src/combine_static.py ./src/static/ css "$OUTPUT_PATH" "$RES"
cp ./src/static/fonts/* "$FONTS_PATH"
cp -r ./src/static/images/* "$IMAGE_PATH"
cp ./src/.htaccess "$OUTPUT_PATH"

# Build the home page which is the index.html page
INDEX='index.html'
python src/build_index.py >"$OUTPUT_PATH$INDEX"
python src/build_resume.py >$RESUME_PATH"index.html"
python src/build_about.py >$ABOUT_PATH"index.html"
# Build all the pages from the blog
for filename in src/pages/posts/*.html; do
    ./blog-build.sh "$filename" &
done
wait
python ./src/generate_blog_page.py > $BLOG_PATH"index.html"
