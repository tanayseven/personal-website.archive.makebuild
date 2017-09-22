import os
from glob import glob

from personal_website.utils.blog_path import trim_left_path


def _get_full_path(path_list):
    paths = []
    for path in path_list:
        paths.extend(
            [path[0] + '/' + file_name for file_name in path[2]]
        )
    return paths


def get_all_sub_files(path, ends_with='html'):
    return tuple(
        filter(
            lambda filename: filename.endswith(ends_with),
            _get_full_path(
                [
                    path
                    for path
                    in os.walk(path)
                ]
            )
        )
    )


def generate_all_image_path(base_path):
    image_dir_ = glob(base_path + '*')
    for image_dir in image_dir_:
        files = next(os.walk(image_dir))[2]
        for image_file in files:
            yield trim_left_path(image_dir + '/' + image_file, base_path)
