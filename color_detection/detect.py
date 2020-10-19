from colorthief import ColorThief
from PIL import Image
import numpy as np
import colorsys
import cv2
import io


class Mask:
    def __init__(self, name, color_lower, color_upper):
        self.name = name
        self.color_lower = color_lower
        self.color_upper = color_upper

    def get_RGB(self):
        lower_rgb = colorsys.hsv_to_rgb(
            self.color_lower[0], self.color_lower[1], self.color_lower[2])
        upper_rgb = colorsys.hsv_to_rgb(
            self.color_upper[0], self.color_upper[1], self.color_upper[2])
        return lower_rgb, upper_rgb


def detect(frame, masks):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for mask in masks:
        temporal_mask = cv2.inRange(hsv, np.array(mask.color_lower),
                                    np.array(mask.color_upper))

        if(np.count_nonzero(temporal_mask) != 0):
            color = mask
            break

    return color


def detect_dominant(frame):
    """
    Takes a frame and returns the domint color. 
    """

    # Frame to image
    image = Image.fromarray(frame)

    # Image to file
    byte_object = io.BytesIO()
    image.save(byte_object, "JPEG")

    print("----------------------------")
    print(type(image))
    print(type(frame))
    print(type(byte_object))

    color_thief = ColorThief(byte_object)
    dominant_color = color_thief.get_color(quality=1)

    return dominant_color
