#!/usr/bin/env bash
html=$($MD $1)
destination="$BASE_PATH$BLOG_PATH$(./blog_path.py $1)"
echo "$destination" >> "$BASE_PATH$BLOG_PATH$BLOG_LINKS_LIST"
mkdir -p $(dirname "$destination")
echo "$html" > "$destination"
