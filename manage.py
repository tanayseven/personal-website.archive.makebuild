#!/usr/bin/env python3
import shutil
from flask_frozen import Freezer
from manager import Manager

from personal_website.flask_app import app

manager = Manager()


@manager.command
def build():
    freezer = Freezer(app)
    freezer.freeze()


@manager.command
def run(port='8000'):
    app.run(port=int(port))


@manager.command
def clean():
    shutil.rmtree('personal_website/build/')


if __name__ == '__main__':
    manager.main()
