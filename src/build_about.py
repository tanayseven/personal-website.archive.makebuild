from jinja2 import Environment, FileSystemLoader

with open('css.txt') as f:
    css_file_path = f.read()
css_file_path = '/'.join(css_file_path.split('/')[1:])
template = Environment(loader=FileSystemLoader('src/pages/')).get_template('about.html')

print(template.render(
    css_file_path=css_file_path,
    page_title='About',
    nav_button='about',
))
