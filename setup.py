from color_detection.detect import Mask, detect
import numpy as np
import colorsys
import colors
import cv2


def selectImage(source, height, width):
    # Using image
    image = cv2.imread(source)
    image = cv2.resize(image, (width, height))


blue = Mask("Azul", colors.BLUE["lower"], colors.BLUE["upper"])
green = Mask("Verde", colors.GREEN["lower"], colors.GREEN["upper"])
orange = Mask("Naranja", colors.ORANGE["lower"], colors.ORANGE["upper"])
red = Mask("Rojo", colors.RED["lower"], colors.RED["upper"])
yellow = Mask("Amarillo", colors.YELLOW["lower"], colors.YELLOW["upper"])
white = Mask("Blanco", colors.WHITE["lower"], colors.WHITE["upper"])
colors = [blue, green, orange, red, yellow, white]

image = cv2.imread("img/blue.jpg")

detected_color = detect(image, colors)
print(detected_color.name)

cv2.imshow("contour", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
