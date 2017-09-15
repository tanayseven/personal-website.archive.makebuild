from jinja2 import Environment, FileSystemLoader

template = Environment(loader=FileSystemLoader('personal_website/pages/')).get_template('index.html')


def result(static_files=None, css_file=''):
    return template.render(
        css_file_path=css_file,
        page_title='Home',
        nav_button='home',
    )


if __name__ == '__main__':
    print(result)
