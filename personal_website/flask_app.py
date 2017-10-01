from flask import Flask

from personal_website.process_static.compile_files import combine_static_text
from personal_website.process_static.process_images import process_images
from personal_website.render_pages.main_pages_render import save_blog_entries_to_db
from personal_website.routes import attach_routes

app = Flask(__name__)


def process_static():
    save_blog_entries_to_db()
    css_file = combine_static_text(app, 'raw_static/css', 'static/css', 'css')
    process_images()
    return css_file


if __name__ == '__main__':
    app.run(debug=True)
