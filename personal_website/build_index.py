from jinja2 import Environment, FileSystemLoader

from personal_website.combine_static import get_css_file

with open('css.txt') as f:
    css_file_path = f.read()
css_file_path = '/' + '/'.join(css_file_path.split('/')[1:])
template = Environment(loader=FileSystemLoader('personal_website/pages/')).get_template('index.html')


def result(static_files=None):
    if static_files is None:
        static_files = [css_file_path]
    return template.render(
        css_file_path=get_css_file(static_files),
        page_title='Home',
        nav_button='home',
    )


if __name__ == '__main__':
    print(result)
