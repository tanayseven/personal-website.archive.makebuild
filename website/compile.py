import json
import sys

from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader(package_name=__name__.split('.')[0], package_path='../templates'),
    autoescape=select_autoescape(['html', 'xml']),
)

json_objs = None
if len(sys.argv) > 2:
    json_objs = json.loads(sys.argv[2])

template = env.get_template(sys.argv[1][len('templates/'):])
print(template.render(objs=json_objs))
