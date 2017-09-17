#!/usr/bin/env python3
import os

from flask_frozen import Freezer
from manager import Manager

from constants import BLOG_PATH
from personal_website.blog_path import split_path
from personal_website.flask_app import app

manager = Manager()
freezer = Freezer(app)


@freezer.register_generator
def fonts():
    path = os.path.join(app.root_path, 'static/fonts') + '/'
    fonts_ = next(os.walk(path))[2]
    for font in fonts_:
        yield {'path': font}


@freezer.register_generator
def blog_post():
    files = next(os.walk(BLOG_PATH))[2]
    blog_posts = [file for file in files if file.endswith('.html')]
    for post in blog_posts:
        path = split_path('', '', post)[0]
        yield {
            'year': path[0],
            'month': path[1],
            'day': path[2],
            'name': path[3][:-5],
        }


@manager.command
def build():
    freezer.freeze()


@manager.command
def serve(host='0.0.0.0', port='8000'):
    build()
    print("Running a server on " + host + ":" + port)
    freezer.serve(host=host, port=int(port), debug=True)


@manager.command
def clean():
    os.system("rm -rf personal_website/build/*")


@manager.command
def test():
    clean()
    build()
    os.system("py.test; behave")


if __name__ == '__main__':
    manager.main()
