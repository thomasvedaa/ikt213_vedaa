import cv2
import numpy as np
from matplotlib import pyplot as plt

image=cv2.imread("lambo.png")


def sobel_edge_detection(image):
    cv2.imshow('Original', image)
    cv2.waitKey(0)

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_blur = cv2.GaussianBlur(image_gray, (3, 3), 0)

    sobel = cv2.Sobel(src=image_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=1)
    cv2.imshow('Sobel X', sobel)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("sobel_edged.png", sobel)
    print("Sobel edge image saved as sobel_edged.png")



def canny_edge_detection(image, threshold1, threshold2):
    cv2.imshow('Original', image)
    cv2.waitKey(0)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_blur = cv2.GaussianBlur(image_gray, (3, 3), 0)
    edges = cv2.Canny(image=image_gray, threshold1=threshold1, threshold2=threshold2)

    cv2.imshow('Canny Edge Detection', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("canny_edged.png", edges)
    print("Canny edge image saved as canny_edged.png")


def template_matching(image,template):

    image_gray = image
    template= template
    width, height = template.shape[::-1]

    res = cv2.matchTemplate(image_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(image, pt, (pt[0] + width, pt[1] + height), (0, 255, 0), 2)

    cv2.imshow('Template', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("template_matching.png", image)
    print("Template image saved as template_matching.png")



def resize(image,scale_factor:int, up_or_down: str):
    cv2.imshow('Original', image)
    cv2.waitKey(0)

    if up_or_down == 'up':
        for _ in range(scale_factor-1):
            image = cv2.pyrUp(image)
    elif up_or_down == 'down':
        for _ in range(scale_factor-1):
            image = cv2.pyrDown(image)

    cv2.imshow('Resize', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("resize.png", image)
    print("Resize image saved as resize.png")


    
if __name__ == '__main__':
    while True:
        print("1.Sobel Edge Detection"
              "\n2. Canny Edge Detection"
              "\n3. Template Matching"
              "\n4. Resize")
        choice = input("Enter your choice: \n")

        if choice == '1':
            sobel_edge_detection(image)
        elif choice == '2':
            canny_edge_detection(image,50,50)
        elif choice == '3':
            template = cv2.imread("shapes_template.jpg",0)
            image = cv2.imread("shapes-1.png",0)
            template_matching(image,template)
        elif choice == '4':
            resize_choice = input("Up or down:")
            scale_factor = int(input("Scale factor:"))
            resize(image,scale_factor,up_or_down=resize_choice)