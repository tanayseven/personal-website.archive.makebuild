#!/usr/bin/env python
from fnmatch import fnmatch
import os

from jinja2 import Environment, PackageLoader, select_autoescape


def get_full_path(path_list):
    paths = []
    for path in path_list:
        paths.extend(
            [path[0] + '/' + file_name for file_name in path[2]]
        )
    return paths


pages = tuple(
    filter(
        lambda filename: filename.endswith('html'),
        get_full_path(
            [
                path
                for path
                in os.walk('src')
            ]
        )
    )
)
print(pages)
