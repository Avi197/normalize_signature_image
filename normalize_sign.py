from PIL import Image, ImageOps
import argparse
import glob
import os
from PIL import Image
import numpy as np
from skimage.io import imread
from skimage import filters, img_as_ubyte
from pathlib import Path


def get_text_area(img_file):
    blur_radius = 2
    blurred_image = filters.gaussian(img_file, blur_radius, preserve_range=True)
    threshold = filters.threshold_otsu(blurred_image)
    binarized_image = blurred_image > threshold

    r, c = np.where(binarized_image == 0)
    return r, c, threshold


def remove_background(img_file):
    r, c, threshold = get_text_area(img_file)
    # Crop the image with a tight box
    cropped_img = img_file[r.min(): r.max(), c.min(): c.max()]

    img_file[img_file > threshold] = 255
    cropped_img[cropped_img > threshold] = 255
    # convert_to_one_zero = img_file
    # convert_to_one_zero[convert_to_one_zero < 255] = 0
    return cropped_img


def make_square(img_path, canvas_size=(150, 150), fill_color=(255, 255, 255)):
    img_file = img_as_ubyte(imread(img_path, as_gray=True))
    im = remove_background(img_file)
    im = Image.fromarray(im)
    im = ImageOps.contain(im, canvas_size)
    x, y = im.size
    new_im = Image.new('RGB', canvas_size, fill_color)
    new_im.paste(im, (int((canvas_size[0] - x) / 2), int((canvas_size[0] - y) / 2)))
    return new_im


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_path', type=str, help='path to data folder, assume this folder contain train, val, test')
    parser.add_argument('output_path', type=str, help='path to desired output folder')
    args = parser.parse_args()
    input_path = args.input_path
    output_path = args.output_path

    os.makedirs(output_path, exist_ok=True)
    # create numpy data for data folder if

    canvas_size = (150, 150)

    all_image_files = glob.glob(f'{input_path}/*/*.png')
    print('running normalize data scripts')
    for idx, img_file in enumerate(all_image_files):
        img = make_square(img_file, canvas_size)
        print(f'done file {idx}')
        file_name = Path(img_file).stem + '.png'
        file_path = os.path.join(output_path, file_name)
        img.save(file_path)

