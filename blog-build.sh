#!/usr/bin/env bash
BUILD_BLOG="build_blog.py"
python "$SCRIPT_PATH$BUILD_BLOG" "$1"
#echo "$destination $title" >> "$BASE_PATH$BLOG_PATH$BLOG_LINKS_HEADINGS"
#description=$($MD "--description" "$1")
#echo "$destination $description" >> "$BASE_PATH$BLOG_PATH$BLOG_LINKS_DESCRIPTIONS"
#mkdir -p $(dirname "$destination")
#echo "$html" > "$destination"
