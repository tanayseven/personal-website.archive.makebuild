from personal_website.render_pages.main_pages_render import get_template

template = get_template('index.html')


def result(css_file=''):
    return template.render(
        css_file_path=css_file,
        page_title='Home',
        nav_button='home',
    )
