from flask import send_from_directory

from personal_website.build_about import result as about_page
from personal_website.build_index import result as home_page
from personal_website.build_resume import result as resume_page
from personal_website.compile_files import combine_static
from personal_website.generate_blog_page import result as blog_page


def attach_routes(app, static_files):
    css_file = combine_static(app, 'static/css', 'css')

    @app.route('/fonts/<path:path>')
    def fonts(path):
        return send_from_directory('static/fonts/', path)

    @app.route('/')
    def root():
        return home_page(static_files, css_file)

    @app.route('/home/')
    def home():
        return home_page(static_files, css_file)

    @app.route('/blog/')
    def blog():
        return blog_page(static_files, css_file)

    # @app.route('/blog/<year>/<month>/<day>/<name>.html')
    # def blog_post(year, month, day, name):
    #     pass

    @app.route('/resume/')
    def resume():
        return resume_page(static_files, css_file)

    @app.route('/about/')
    def about():
        return about_page(static_files, css_file)
