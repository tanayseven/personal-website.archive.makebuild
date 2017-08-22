import os

from bs4 import BeautifulSoup

PATH_ROOT = 'personal_website/'


def file_exists(file_name, dir_name):
    return os.path.isfile(PATH_ROOT + dir_name + file_name)


def run_command(command):
    os.system(command)


def soup_for_html(file_path):
    with open(PATH_ROOT + file_path) as file:
        file_contents = file.read()
        soup = BeautifulSoup(file_contents, 'html.parser')
    return soup
