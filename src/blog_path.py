#!/usr/bin/env python3
import sys


def generate_path(src, destination_prefix, left_path_trim):
    str_lst = src.split('-')
    result = str_lst[0] + '/' + str_lst[1] + '/' + str_lst[2] + '/' + '-'.join(str_lst[3:])
    result = destination_prefix + '/'.join(result.split('/')[int(left_path_trim):])
    result = '.'.join(result.split('.')[:-1] + ['html'])
    return result


if __name__ == '__main__':
    print(generate_path(sys.argv[1], sys.argv[2], sys.argv[3]))
