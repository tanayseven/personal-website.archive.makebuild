import click

from PIL import Image

MAX_HEIGHT = 800
MAX_WIDTH = 800


@click.command()
@click.option('--input', default=None, help='input image file to be resized')
@click.option('--output', default=None, help='output image file to be resized')
def resize(input, output):
    image = Image.open(input)
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
