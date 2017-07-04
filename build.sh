#!/usr/bin/env bash
export MD=mdtrans
export BASE_PATH="www/"
export BLOG_PATH="blog/"
export BLOG_LINKS_LIST="blog-links-list.txt"
mkdir -p "$BASE_PATH$BLOG_PATH"
for filename in posts/*.md; do
    ./build-blog.sh "$filename" &
done
wait
