from jinja2 import Template

with open('src/pages/index.html') as f:
    template_str = f.read()
template = Template(template_str)
print(template.render())
