#!/usr/bin/env bash
html=$($MD $1)
destination="$BASE_PATH$BLOG_PATH$(./blog_path.py $1)"
title=$($MD "--title" "$1")
echo "$destination $title" >> "$BASE_PATH$BLOG_PATH$BLOG_LINKS_HEADINGS"
description=$($MD "--description" "$1")
echo "$destination $description" >> "$BASE_PATH$BLOG_PATH$BLOG_LINKS_DESCRIPTIONS"
mkdir -p $(dirname "$destination")
echo "$html" > "$destination"
