#!/usr/bin/env python3
import shutil
from flask_frozen import Freezer
from manager import Manager

from personal_website.combine_static import create_css
from personal_website.db_repos import create_initial_database
from personal_website.flask_app import app

manager = Manager()


# def build_static_files():
#     create_initial_database()
#     create_css('./personal_website/static/css/main.css')


@manager.command
def build():
    # build_static_files()
    freezer = Freezer(app)
    freezer.freeze()


@manager.command
def run(port='8000'):
    # build_static_files()
    app.run(port=int(port), debug=True)


@manager.command
def clean():
    shutil.rmtree('personal_website/build/')


@manager.command
def test():
    pass


if __name__ == '__main__':
    manager.main()
