#!/usr/bin/env bash
BUILD_BLOG="src/build_blog.py"
path=$(python src/blog_path.py "$1" "www/blog/" "3")
mkdir -p $(dirname "$path")
python "$BUILD_BLOG" "$1" > "$path"