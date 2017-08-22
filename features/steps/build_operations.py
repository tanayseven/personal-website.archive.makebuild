import os

PATH_ROOT = 'personal_website/'


def file_exists(file_name, dir_name):
    return os.path.isfile(PATH_ROOT + dir_name + file_name)


def run_command(command):
    os.system(command)
