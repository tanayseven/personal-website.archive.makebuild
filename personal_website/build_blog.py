import fcntl
import sys

from jinja2 import Environment, FileSystemLoader

from constants import give_blank_string

sys.path.append('.')

from personal_website.blog_path import generate_path

jinja_file_name = '/'.join(sys.argv[1].split('/')[-2:])
# html_file_name = generate_path(sys.argv[1], '/blog/', 'personal_website/pages/posts/')
# print(html_file_name.split('/')[2:][:3])


# def write_tags(tags):
#     with open('tags.csv', 'a') as f:
#         fcntl.fcntl(f.fileno(), fcntl.LOCK_EX)
#         f.write(html_file_name + ',' + ','.join(tags) + '\n')
#     return ''
#
#
# def write_description(desc):
#     with open('desc.csv', 'a') as f:
#         fcntl.fcntl(f.fileno(), fcntl.LOCK_EX)
#         f.write(html_file_name + ',' + desc + '\n')
#     return ''
#
#
# def write_title(title):
#     with open('titles.csv', 'a') as f:
#         fcntl.fcntl(f.fileno(), fcntl.LOCK_EX)
#         f.write(html_file_name + ',' + title + '\n')
#     return ''


with open('css.txt') as f:
    css_file_path = f.read()
css_file_path = '/' + '/'.join(css_file_path.split('/')[1:])
# date_list = html_file_name.split('/')[2:][:3]


def result(jinja_file_name=jinja_file_name, css_file_path=''):
    template = Environment(loader=FileSystemLoader('personal_website/pages/')).get_template(jinja_file_name)
    return template.render(
        css_file_path=css_file_path,
        nav_button='blog',
        write_title=give_blank_string,
        write_tags=give_blank_string,
        write_description=give_blank_string,
        date_list=give_blank_string,
    )


print(result)
