import hashlib
import sys

from css_html_js_minify import css_minify, html_minify, js_minify

sys.path.append('.')

from personal_website.utils.file_utils import get_all_sub_files

minify = {
    'css': css_minify,
    'js': js_minify,
    'html': html_minify,
}

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
