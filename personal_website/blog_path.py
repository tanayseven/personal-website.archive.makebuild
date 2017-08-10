#!/usr/bin/env python3
import sys


def generate_path(src, destination_prefix, left_path_trim):
    to_be_formatted = destination_prefix.lstrip('/') + src.split(left_path_trim)[1]
    main_prefix, page_name = '/'.join(to_be_formatted.split('/')[:-1]), to_be_formatted.split('/')[-1]
    html_page_list = page_name.split('-')
    result = main_prefix + '/' + '/'.join(html_page_list[:3]) + '/' + '-'.join(html_page_list[3:])
    return ('/' if destination_prefix.startswith('/') else '/') + result


if __name__ == '__main__':
    print(generate_path(sys.argv[1], sys.argv[2], sys.argv[3]))
