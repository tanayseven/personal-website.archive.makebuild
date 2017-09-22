from flask import Flask

from personal_website.process_static.combine_static import compute_static_files
from personal_website.routes import attach_routes

app = Flask(__name__)

static_files = compute_static_files()
attach_routes(app, static_files)

if __name__ == '__main__':
    app.run(debug=True)
