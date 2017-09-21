from jinja2 import Environment, FileSystemLoader

from personal_website.combine_static import get_css_file

template = Environment(loader=FileSystemLoader('personal_website/pages/')).get_template('about.html')


def result(static_files, css_file):
    return template.render(
        css_file_path=css_file,
        page_title='About',
        nav_button='about',
    )


if __name__ == '__main__':
    print(result)
