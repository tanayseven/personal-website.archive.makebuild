import sys

from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader(package_name=__name__.split('.')[0], package_path='../templates'),
    autoescape=select_autoescape(['html', 'xml']),
)

template = env.get_template(sys.argv[1][len('templates/'):])
print(template.render())
