from flask import Flask

from personal_website.process_static.combine_static import compute_static_files
from personal_website.render_pages.main_pages_render import save_blog_entries_to_db
from personal_website.routes import attach_routes

app = Flask(__name__)


def process_static():
    save_blog_entries_to_db()


process_static()
attach_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
