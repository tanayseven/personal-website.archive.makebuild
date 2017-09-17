import os
from glob import glob

from bs4 import BeautifulSoup

from constants import OUTPUT_PATH, BLOG_PATH

PATH_ROOT = 'personal_website/'


def file_exists(file_name, dir_name):
    return os.path.isfile(PATH_ROOT + dir_name + file_name)


def run_command(command):
    os.system(command)


def soup_for_html(file_path, attach_path_root=True):
    path_root = PATH_ROOT if attach_path_root else ''
    with open(path_root + file_path) as file:
        file_contents = file.read()
        soup = BeautifulSoup(file_contents, 'html.parser')
    return soup


def all_files_in_dir(path, file_extension):
    return [y for x in os.walk(path) for y in glob(os.path.join(x[0], '*.' + file_extension))]


def blog_output_files():
    return [name for name in all_files_in_dir(OUTPUT_PATH, 'html') if not name.endswith('index.html')]


def blog_source_files():
    return [name for name in all_files_in_dir(BLOG_PATH, 'html') if name.endswith('html')]


