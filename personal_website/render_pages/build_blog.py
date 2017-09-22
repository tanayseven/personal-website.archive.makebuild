import sys

from constants import give_blank_string
from personal_website.render_pages.main_pages_render import get_template

sys.path.append('.')

jinja_file_name = '/'.join(sys.argv[1].split('/')[-2:])


def result(jinja_file_name=jinja_file_name, css_file_path=''):
    template = get_template(jinja_file_name)
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
