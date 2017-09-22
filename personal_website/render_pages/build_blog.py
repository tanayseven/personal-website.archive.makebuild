import sys

from personal_website.render_pages.main_pages_render import get_template

jinja_file_name = '/'.join(sys.argv[1].split('/')[-2:])


def result(jinja_file_name=jinja_file_name, css_file_path=''):
    template = get_template(jinja_file_name)
    return template.render(
        css_file_path=css_file_path,
        nav_button='blog',
        show_comments=True,
    )


if __name__ == '__main__':
    print(result)
