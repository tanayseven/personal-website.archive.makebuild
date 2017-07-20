import hashlib
import sys

sys.path.append('.')

from src.utils.file_utils import get_all_sub_files


def main():
    sub_files = sorted(get_all_sub_files(sys.argv[1], sys.argv[2]))
    content = ''
    for input_file in sub_files:
        with open(input_file) as f:
            content += f.read()
    content_hash = hashlib.sha1(content.encode('utf-8')).hexdigest()
    destination_path = content_hash[:12] + '.' + sys.argv[2]
    with open(sys.argv[3] + sys.argv[4] + destination_path, 'w') as f:
        f.write(content)
    with open('./' + sys.argv[2] + '.txt', 'w') as f:
        f.write('/' + sys.argv[4] + destination_path)


if __name__ == '__main__':
    main()
