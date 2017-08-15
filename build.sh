#!/usr/bin/env bash

# List of all the global paths needed for the build
export PAGES_PATH='personal_website/pages/'
export SCRIPT_PATH='personal_website/'
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
python ./personal_website/combine_static.py ./personal_website/static/css/ css "$OUTPUT_PATH" "$RES"
cp ./personal_website/static/fonts/* "$FONTS_PATH"
cp -r ./personal_website/static/images/* "$IMAGE_PATH"
cp ./personal_website/.htaccess "$OUTPUT_PATH"

# Build the home page which is the index.html page
INDEX='index.html'
python personal_website/build_index.py >"$OUTPUT_PATH$INDEX"
python personal_website/build_resume.py >$RESUME_PATH"index.html"
python personal_website/build_about.py >$ABOUT_PATH"index.html"
# Build all the pages from the blog
for filename in personal_website/pages/posts/*.html; do
    ./blog-build.sh "$filename"
done
wait
python ./personal_website/generate_blog_page.py > $BLOG_PATH"index.html"
