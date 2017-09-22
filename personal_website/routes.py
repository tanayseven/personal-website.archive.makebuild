from flask import send_from_directory

from personal_website.process_static.compile_files import combine_static
from personal_website.render_pages.build_about import result as about_page
from personal_website.render_pages.build_blog import result as blog_post_generate
from personal_website.render_pages.build_index import result as home_page
from personal_website.render_pages.build_resume import result as resume_page
from personal_website.render_pages.generate_blog_page import result as blog_page


def attach_routes(app):
    css_file = combine_static(app, 'static/css', 'css')

    @app.route('/fonts/<path:path>')
    def fonts(path):
        return send_from_directory('static/fonts/', path)

    @app.route('/res/images/<path:path>')
    def images(path):
        return send_from_directory('static/images/', path)

    @app.route('/')
    def root():
        return home_page(css_file)

    @app.route('/home/')
    def home():
        return home_page(css_file)

    @app.route('/blog/')
    def blog():
        return blog_page(css_file)

    @app.route('/blog/<year>/<month>/<day>/<name>.html')
    def blog_post(year, month, day, name):
        return blog_post_generate(
            jinja_file_name=('posts/' + year + '-' + month + '-' + day + '-' + name + '.html'),
            css_file_path=css_file
        )

    @app.route('/resume/')
    def resume():
        return resume_page(css_file)

    @app.route('/about/')
    def about():
        return about_page(css_file)
