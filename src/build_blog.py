import fcntl
from jinja2 import Environment, FileSystemLoader
import sys

sys.path.append('.')

from src.utils.file_utils import get_all_sub_files

html_file_name = '/'.join(sys.argv[1].split('/')[-2:])


def write_tags(tags):
    with open('tags.txt', 'a') as f:
        fcntl.lockf(f.fileno(), fcntl.LOCK_EX)
        f.write(html_file_name + ',' + ','.join(tags) + '\n')
        fcntl.lockf(f.fileno(), fcntl.F_UNLCK)
    return ''


with open('css.txt') as f:
    css_file_path = f.read()
css_file_path = '/'.join(css_file_path.split('/')[1:])
template = Environment(loader=FileSystemLoader('src/pages/')).get_template(html_file_name)

print(template.render(
    css_file_path=css_file_path,
    page_title='Home - Tanay PrabhuDesai',
    nav_button='home',
    write_tags=write_tags,
))
