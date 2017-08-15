#!/usr/bin/env bash
BUILD_BLOG="personal_website/build_blog.py"
path=$(python personal_website/blog_path.py "$1" "www/" "personal_website/pages/posts/")
mkdir -p $(dirname "$path")
echo $path
python "$BUILD_BLOG" "$1" > "$path"