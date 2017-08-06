#!/usr/bin/env python3
from manager import Manager
from multiprocessing import Pool

manager = Manager()


def func(period):
    from time import sleep
    sleep(period)


@manager.command
def build(threads=1):
    pool = Pool(threads)
    print("Starting a build with %d threads ..." % threads)
    pool.map(func, [1, 1, 1, 1, 1])


@manager.command
def clean():
    pass


if __name__ == '__main__':
    manager.main()
