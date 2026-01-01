import os
import cv2
from .filters import *

def process_image(image_path, output_dir):
    img = cv2.imread(image_path)

    gray = grayscale(img)
    blur = gaussian_blur(gray)
    edge = sobel_edge(blur)
    sharp = sharpen(edge)
    bright = adjust_brightness(sharp)

    filename = os.path.basename(image_path)
    output_path = os.path.join(output_dir, filename)

    cv2.imwrite(output_path, bright)
    return filename