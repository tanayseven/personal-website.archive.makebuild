from flask import Flask

from personal_website.routes import attach_routes

app = Flask(__name__)

attach_routes(app)

extra_files = []

if __name__ == '__main__':
    app.run(extra_files=extra_files)
