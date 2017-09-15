import hashlib
import os

import css_html_js_minify

from personal_website.constants import SOURCE_ROOT


def combine_static(app, src_directory_path, file_extension) -> str:
    src_directory_path = (src_directory_path if src_directory_path.endswith('/') else src_directory_path + '/')
    path = os.path.join(app.root_path, src_directory_path)
    files = next(os.walk(path))[2]
    content = ''
    for file_name in files:
        with open(SOURCE_ROOT + src_directory_path + file_name) as f:
            content += f.read()
    content = css_html_js_minify.css_minify(content)
    content_hash = hashlib.sha1(content.encode('utf-8')).hexdigest()[:8]
    dest_directory_path = '/'.join(src_directory_path.rsplit('/')[:-2])
    dest_directory_path = (dest_directory_path if dest_directory_path.endswith('/') else dest_directory_path + '/')
    print(dest_directory_path)
    with open(SOURCE_ROOT + dest_directory_path + content_hash + '.' + file_extension, 'w') as f:
        f.write(content)
    print(dest_directory_path, src_directory_path)
    return '/' + dest_directory_path + content_hash + '.' + file_extension
