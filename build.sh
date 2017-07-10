#!/usr/bin/env bash
export MD=mdtrans
export BASE_PATH="www/"
export BLOG_PATH="blog/"
export BLOG_LINKS_HEADINGS="blog-links-headings.txt"
export BLOG_LINKS_DESCRIPTIONS="blog-links-descriptions.txt"
mkdir -p "$BASE_PATH$BLOG_PATH"
for filename in posts/*.md; do
    ./blog-build.sh "$filename" &
done
wait
