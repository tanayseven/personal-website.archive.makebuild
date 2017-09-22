from flask import Flask

from personal_website.process_static.combine_static import compute_static_files
from personal_website.process_static.compile_files import combine_static_text
from personal_website.render_pages.main_pages_render import save_blog_entries_to_db
from personal_website.routes import attach_routes

app = Flask(__name__)

css_file = ''


def process_static():
    global css_file
    save_blog_entries_to_db()
    css_file = combine_static_text(app, 'raw_static/css', 'static/css', 'css')


process_static()
attach_routes(app, css_file)

if __name__ == '__main__':
    app.run(debug=True)
