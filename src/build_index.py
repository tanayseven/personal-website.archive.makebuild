from jinja2 import Template

with open('src/pages/index.html') as f:
    template_str = f.read()
with open('css.txt') as f:
    css_file_path = f.read()
css_file_path = '/'.join(css_file_path.split('/')[1:])
template = Template(template_str)
print(template.render(css_file_path=css_file_path))
