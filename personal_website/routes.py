from personal_website.build_index import result as home_page

from personal_website.build_resume import result as resume_page
from personal_website.build_about import result as about_page

def attach_routes(app):

    @app.route('/')
    def root():
        return home_page

    @app.route('/home/')
    def home():
        return home_page

    @app.route('/blog/')
    def blog():
        return 'Blog'

    @app.route('/resume/')
    def resume():
        return resume_page

    @app.route('/about/')
    def about():
        return about_page
