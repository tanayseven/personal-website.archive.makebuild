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
def serve(host='0.0.0.0', port='8000'):
    build()
    print("Running a server on " + host + ":" + port)
    freezer.serve(host=host, port=int(port), debug=True)


@manager.command
def clean():
    os.system("rm -rf personal_website/build/*")


@manager.command
def test():
    pass


if __name__ == '__main__':
    manager.main()
