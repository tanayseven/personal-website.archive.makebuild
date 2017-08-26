import hashlib
import sqlite3
import sys

from css_html_js_minify import css_minify, html_minify, js_minify

from personal_website.constants import CSS, JS, HTML, STATIC_PATH, SOURCE_ROOT
from personal_website.utils.file_utils import get_all_sub_files

minify = {
    CSS: css_minify,
    JS: js_minify,
    HTML: html_minify,
}


def create_css():
    sub_files = sorted(get_all_sub_files(SOURCE_ROOT + STATIC_PATH + CSS, CSS))
    content = ''
    for input_file in sub_files:
        with open(input_file) as f:
            content += f.read()
    content = minify['css'](content)
    content_hash = hashlib.sha1(content.encode('utf-8')).hexdigest()
    destination_path = SOURCE_ROOT + STATIC_PATH + content_hash[:12] + '.' + CSS
    with open(destination_path, 'w') as f:
        f.write(content)
    return STATIC_PATH + content_hash[:12] + '.' + 'css'


def main():
    sub_files = sorted(get_all_sub_files(sys.argv[1], sys.argv[2]))
    content = ''
    for input_file in sub_files:
        with open(input_file) as f:
            content += f.read()
    content = minify[sys.argv[2]](content)
    content_hash = hashlib.sha1(content.encode('utf-8')).hexdigest()
    destination_path = content_hash[:12] + '.' + sys.argv[2]
    with open(sys.argv[3] + sys.argv[4] + destination_path, 'w') as f:
        f.write(content)
    with open('./' + sys.argv[2] + '.txt', 'w') as f:
        f.write('/' + sys.argv[4] + destination_path)


def compute_static_files():
    return [create_css()]


def get_css_file(static_files):
    for file_name in static_files:
        if file_name.endswith(CSS):
            return file_name


def get_js_file(static_files):
    for file_name in static_files:
        if file_name.endswith(JS):
            return file_name


if __name__ == '__main__':
    main()
