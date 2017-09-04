#!/usr/bin/env python3
import os
import shutil

from flask_frozen import Freezer
from manager import Manager

from personal_website.flask_app import app

manager = Manager()
freezer = Freezer(app)


@freezer.register_generator
def fonts():
    path = os.path.join(app.root_path, 'static/fonts') + '/'
    fonts_ = next(os.walk(path))[2]
    for font in fonts_:
        yield {'path': font}


@manager.command
def build():
    freezer.freeze()


@manager.command
def run(port='8000'):
    freezer.serve(port=int(port), debug=True)


@manager.command
def clean():
    shutil.rmtree('personal_website/build/')


@manager.command
def test():
    pass


if __name__ == '__main__':
    manager.main()
