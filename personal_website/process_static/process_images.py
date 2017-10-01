import os

from PIL import Image

from constants import RAW_IMAGE_PATH, IMAGE_PATH, OPTIMIZED_IMAGE_WIDTH
from personal_website.utils.file_utils import generate_all_image_path


def _process(image_data):
    new_width = OPTIMIZED_IMAGE_WIDTH if image_data.width > OPTIMIZED_IMAGE_WIDTH else image_data.width
    quality_drop = (new_width / image_data.width)
    new_height = int(quality_drop * image_data.height)
    image_data = image_data.resize((new_width, new_height), Image.ANTIALIAS)
    return image_data, quality_drop


def process_images():
    image_paths = generate_all_image_path(RAW_IMAGE_PATH)
    for image_path in image_paths:
        image_data = Image.open(RAW_IMAGE_PATH + image_path)
        image_data, quality_drop = _process(image_data)
        os.makedirs(os.path.dirname(IMAGE_PATH + image_path), exist_ok=True)
        image_data.save(IMAGE_PATH + image_path, optimize=True, quality=95)
