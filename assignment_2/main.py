import cv2
import numpy as np
from matplotlib import pyplot as plt

border_width = 100
x_0=80
y_0=80
x_1 = 130
y_1= 130




image = cv2.imread('lena-2.png')
def padding(image, border_width):
    border_width = border_width
    padded_image=cv2.copyMakeBorder(image, border_width,border_width,border_width,border_width,cv2.BORDER_REFLECT)
    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite("padded_lena_reflected.png", padded_image)
    print("Padded image saved as padded_lena_reflected.png")

def crop(image, x_0,x_1,y_0,y_1):
    h, w = image.shape[:2]
    cropped_image = image[y_0:h - y_1, x_0:w - x_1]
    cv2.imshow('cropped_image',cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("cropped_lena.png", cropped_image)
    print("Cropped image saved as cropped_lena.png")


def resize(image, width,height):
    width = width
    height = height
    image = image
    resized_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_LINEAR)
    cv2.imshow('resized_image', resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_lena.png", resized_image)
    print("Resized image saved as resized_lena.png")

def copy(image, emptyPictureArray):
    emptyPictureArray = emptyPictureArray
    image = image
    height, width = image.shape[:2]
    channels = len(image.shape)
    np.copyto(emptyPictureArray, image)
    cv2.imshow("array", emptyPictureArray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("copy.png", image)
    print("Copy image saved as copy.png")

def grayscale(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('grayscale', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("grayscale.png", image)
    print("Grayscale image saved as grayscale.png")

def hsv(image):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    cv2.imshow('hsv', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("hsv.png", image)
    print("HSV image saved as hsv.png")

def hue_shifted(image, emptyPictureArray, hue):
    np.copyto(emptyPictureArray, image)
    shifted = emptyPictureArray.astype(np.uint8)
    shifted = shifted + hue


    cv2.imshow("Hue Shifted", shifted)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("hue_shifted.png", shifted)
    print("Hue-shifted image saved as hue_shifted.png")


def smoothing(image):
    smoothed_image = cv2.GaussianBlur(image, (15, 15), 0)
    cv2.imshow('smoothing', smoothed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("smoothing.png", smoothed_image)
    print("Smoothing image saved as smoothing.png")


def rotation(image, rotation_angle):
    rotation_angle = rotation_angle
    if rotation_angle == 90:
        image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    elif rotation_angle == 180:
        image = cv2.rotate(image, cv2.ROTATE_180)
    cv2.imshow('rotation', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("rotation.png", image)
    print("Rotation image saved as rotation.png")

if __name__ == "__main__":
    while(True):

        choice=input("Choose image operation"
                     "\n1. Padding-reflection"
                     "\n2. Cropped"
                     "\n3. Resize"
                     "\n4. Copy"
                     "\n5. Grayscale"
                     "\n6. HSV"
                     "\n7. Hue shifted"
                     "\n8. Smoothing"
                     "\n9. Rotation"
                     "\n10. Stop\n")

        if choice=="1":
            padding(image,border_width)

        elif choice=="2":
            crop(image,x_0,x_1,y_0,y_1)

        elif choice=="3":
            width = 200
            height = 200
            resize(image,width,height)

        elif choice=="4":
            width = 512
            height = 512
            emptyPictureArray = np.zeros((height, width, 3), np.uint8)
            copy(image,emptyPictureArray)

        elif choice=="5":
            grayscale(image)

        elif choice=="6":
            hsv(image)

        elif choice=="7":
            width = 512
            height = 512
            emptyPictureArray = np.zeros((height, width, 3), np.uint8)
            hue_shifted(image,emptyPictureArray,50)
        elif choice=="8":
            smoothing(image)

        elif choice=="9":
            rotation_angle = int(input("Enter rotation angle: "))
            rotation(image,rotation_angle)
        elif choice=="10":
            break