import os

from constants import RAW_IMAGE_PATH, IMAGE_PATH
from personal_website.utils.file_utils import generate_all_image_path


def _process(image_data):
    return image_data


def process_images():
    image_paths = generate_all_image_path(RAW_IMAGE_PATH)
    for image_path in image_paths:
        with open(RAW_IMAGE_PATH + image_path, 'rb') as f:
            image_data = f.read()
        image_data = _process(image_data)
        os.makedirs(os.path.dirname(IMAGE_PATH + image_path), exist_ok=True)
        with open(IMAGE_PATH + image_path, 'wb') as f:
            f.write(image_data)
