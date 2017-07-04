#!/usr/bin/env bash
MD=mdtrans
BASE_PATH="www/"
BLOG_PATH="blog/"
for filename in posts/*.md; do
    html=$($MD $filename)
    destination="$BASE_PATH$BLOG_PATH$(./blog_path.py $filename)"
    mkdir -p $(dirname "$destination")
    echo "$html" > "$destination"
done