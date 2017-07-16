#!/usr/bin/env bash
export PAGES_PATH='src/pages'
export SCRIPT_PATH='src/'
export OUTPUT_PATH='www/'
export BLOG_PATH='blog/'
mkdir -p "$BASE_PATH$BLOG_PATH"
INDEX='index.html'
python src/build_index.py >"$OUTPUT_PATH$INDEX"
for filename in posts/*.md; do
    ./blog-build.sh "$filename" &
done
wait
