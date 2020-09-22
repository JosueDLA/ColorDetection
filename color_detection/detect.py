import numpy as np
import colorsys
import cv2


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


def detect(frame, masks, color_threshold=0.10):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for mask in masks:
        temporal_mask = cv2.inRange(hsv, np.array(mask.color_lower),
                                    np.array(mask.color_upper))

        if(np.count_nonzero(temporal_mask) != 0):
            color = mask
            break
    return color


def detect_dominant(frame):
    pass
