import numpy as np
import cv2
import matplotlib.pyplot as plt


def show_pic(name, img):
    cv2.imshow(name, img)
    # fig = plt.figure(figsize=(15, 15))
    # ax = fig.add_subplot(111)
    # ax.imshow(img, cmap='gray')
    # cv2.waitKey(10000)


img = cv2.imread('DATA/crossword.jpg', 0)