#!/usr/bin/env python3
from manager import Manager

manager = Manager()


@manager.command
def build(threads=1):
    print("Starting a build with %d threads ..." % threads)

@manager.command
def clean():
    pass

if __name__ == '__main__':
    manager.main()
