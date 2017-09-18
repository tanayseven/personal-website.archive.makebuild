import csv

from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

desc = {}
tags = {}
titles = {}

with open('desc.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        desc[row[0]] = ','.join(row[1:])

with open('tags.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        tags[row[0]] = row[1:]

with open('titles.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        titles[row[0]] = ','.join(row[1:])

template = Environment(loader=FileSystemLoader('personal_website/pages/')).get_template('blog.html')


def result(static_files, css_file=''):
    return template.render(
        css_file_path=css_file,
        nav_button='blog',
        title='Blog',
        titles=titles,
        description=desc,
        tags=tags,
    )


if __name__ == '__main__':
    print(result)
