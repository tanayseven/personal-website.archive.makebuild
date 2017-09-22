from jinja2 import Environment, FileSystemLoader


def get_template(file_name):
    return Environment(loader=FileSystemLoader('personal_website/pages/')).get_template(file_name)
