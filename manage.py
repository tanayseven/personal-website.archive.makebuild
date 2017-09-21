#!/usr/bin/env python3
import os

from flask_frozen import Freezer
from manager import Manager

from personal_website.endpoint_generator import freeze_endpoints
from personal_website.flask_app import app

manager = Manager()
freezer = Freezer(app)
freeze_endpoints(freezer)


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
