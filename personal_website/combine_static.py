import hashlib
import sys
import sqlite3

from css_html_js_minify import css_minify, html_minify, js_minify

from personal_website.constants import DATABASE_NAME
from personal_website.utils.file_utils import get_all_sub_files

minify = {
    'css': css_minify,
    'js': js_minify,
    'html': html_minify,
}


def create_css(css_files=()):
    conn = sqlite3.connect(DATABASE_NAME)
    sub_files = sorted(get_all_sub_files(css_files, 'css'))
    content = ''
    for input_file in sub_files:
        with open(input_file) as f:
            content += f.read()
    content = minify['css'](content)
    content_hash = hashlib.sha1(content.encode('utf-8')).hexdigest()
    destination_path = content_hash[:12] + '.' + 'css'
    conn.close()


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


if __name__ == '__main__':
    main()
