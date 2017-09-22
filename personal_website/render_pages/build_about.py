from personal_website.render_pages.main_pages_render import get_template

template = get_template('about.html')


def result(css_file):
    return template.render(
        css_file_path=css_file,
        page_title='About',
        nav_button='about',
    )


if __name__ == '__main__':
    print(result)
