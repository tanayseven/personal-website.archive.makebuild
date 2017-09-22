from flask import Flask

from personal_website.process_static.combine_static import compute_static_files
from personal_website.routes import attach_routes

app = Flask(__name__)

attach_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
