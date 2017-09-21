#!/usr/bin/env python3
import sys


def generate_path(src, destination_prefix, left_path_trim):
    html_page_list, main_prefix = split_path(destination_prefix, left_path_trim, src)
    result = main_prefix + '/' + '/'.join(html_page_list[:3]) + '/' + '-'.join(html_page_list[3:])
    return ('/' if destination_prefix.startswith('/') else '') + result


def split_path(destination_prefix, left_path_trim, src):
    to_be_formatted = trim_left_path(src, left_path_trim, destination_prefix)
    main_prefix, page_name = '/'.join(to_be_formatted.split('/')[:-1]), to_be_formatted.split('/')[-1]
    html_page_list = page_name.split('-')
    name = '-'.join(html_page_list[3:])
    date = html_page_list[:3]
    html_page_list = date + [name]
    return html_page_list, main_prefix


def trim_left_path(src, left_path_trim, destination_prefix=''):
    if left_path_trim != '':
        to_be_formatted = (destination_prefix + src.split(left_path_trim)[1]).lstrip('/')
    else:
        to_be_formatted = (destination_prefix + src).lstrip('/')
    return to_be_formatted


if __name__ == '__main__':
    print(generate_path(sys.argv[1], sys.argv[2], sys.argv[3]))
