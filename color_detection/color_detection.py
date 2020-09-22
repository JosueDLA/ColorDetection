import cv2
import numpy as np
import colors


class Mask:
    def __init__(self, color_lower, color_upper):
        self.color_lower = color_lower
        self.color_upper = color_upper
