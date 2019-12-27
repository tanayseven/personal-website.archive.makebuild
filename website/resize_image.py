import click

from PIL import Image

MAX_HEIGHT = 800
MAX_WIDTH = 800
NON_IMAGE_TYPES = ('json','svg')

@click.command()
@click.option('--input', default=None, help='input image file to be resized')
@click.option('--output', default=None, help='output image file to be resized')
def resize(input, output):
    input_ = input
    if input_.split('.')[-1] in NON_IMAGE_TYPES:
        _ignore_image_resize(input_, output)
    else:
        _perform_resize_operation(input_, output)


def _ignore_image_resize(input_, output):
    with open(input_) as input_file:
        data = input_file.read()
        with open(output, 'w') as output_file:
            output_file.write(data)


def _perform_resize_operation(input_, output):
    image = Image.open(input_)
    width, height = image.size
    ratio = 1
    if height > width and height > MAX_HEIGHT:
        ratio = MAX_HEIGHT / height
    elif width < height and width > MAX_WIDTH:
        ratio = MAX_WIDTH / width
    width, height = int(width * ratio), int(height * ratio)
    image = image.resize((width, height), Image.ANTIALIAS)
    image.save(output)


if __name__ == '__main__':
    resize()
