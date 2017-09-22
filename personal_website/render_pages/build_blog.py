import sys

from jinja2 import Environment, FileSystemLoader

from constants import give_blank_string

sys.path.append('.')

jinja_file_name = '/'.join(sys.argv[1].split('/')[-2:])


# with open('css.txt') as f:
#     css_file_path = f.read()
# css_file_path = '/' + '/'.join(css_file_path.split('/')[1:])


def result(jinja_file_name=jinja_file_name, css_file_path=''):
    template = Environment(loader=FileSystemLoader('personal_website/pages/')).get_template(jinja_file_name)
    return template.render(
        css_file_path=css_file_path,
        nav_button='blog',
        write_title=give_blank_string,
        write_tags=give_blank_string,
        write_description=give_blank_string,
        date_list=give_blank_string,
        show_comments=True,
    )

if __name__ == '__main__':
    print(result)
