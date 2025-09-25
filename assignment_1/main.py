import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lena-1.png',0)


def print_image_information(img):

    height, width = img.shape[:2]
    print("Height: ",height)
    print("Width: ",width)
    channels = len(img.shape)

    if channels == 2:
        print("Channels: 1, grayscale image",)

    size=img.shape
    print("size: ",size)
    print("datatype: ",img.dtype)


    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    print_image_information(img)
