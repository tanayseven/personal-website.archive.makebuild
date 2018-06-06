import csv

import click
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader(package_name=__name__.split('.')[0], package_path='../templates'),
    autoescape=select_autoescape(['html', 'xml']),
)


def extract_into_list(file_name):
    rows = []
    with open(file_name, newline='\n') as file:
        spamreader = csv.reader(file, delimiter=',')
        for i, row in enumerate(spamreader):
            if i != 0:
                rows.append({
                    "id": row[0],
                    "title": row[1],
                    "description": row[2],
                })
    return rows


@click.command()
@click.option('--template', default='index.html', help='template directory that is to be rendered')
@click.option('--file', default=None, help='csv file that has the necessary data in it')
def compile_(template, file):
    template = env.get_template(template[len('templates/'):])
    rows = []
    if file is not None:
        rows = extract_into_list(file)
    print(template.render(objs=rows))


if __name__ == '__main__':
    compile_()
