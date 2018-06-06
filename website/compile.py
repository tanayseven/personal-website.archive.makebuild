import csv
import json
import sys

from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader(package_name=__name__.split('.')[0], package_path='../templates'),
    autoescape=select_autoescape(['html', 'xml']),
)

rows = []
if len(sys.argv) > 2:
    delimiter = ','
    with open(sys.argv[2], newline='\n') as file:
        spamreader = csv.reader(file, delimiter=delimiter)
        for i, row in enumerate(spamreader):
            if i != 0:
                rows.append({
                    "id": row[0],
                    "title": row[1],
                    "description": row[2],
                })

template = env.get_template(sys.argv[1][len('templates/'):])
print(template.render(objs=rows))
