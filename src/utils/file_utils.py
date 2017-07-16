import os


def get_full_path(path_list):
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
            get_full_path(
                [
                    path
                    for path
                    in os.walk(path)
                ]
            )
        )
    )
