import numpy as np
import cv2
import matplotlib.pyplot as plt


def onTrackBarChange(num):
    print(num)
    return num


def show_pic(name, img):
    cv2.imshow(name, img)
    # fig = plt.figure(figsize=(15, 15))
    # ax = fig.add_subplot(111)
    # ax.imshow(img, cmap='gray')
    # cv2.waitKey(10000)


cv2.namedWindow('Thresh')
cv2.namedWindow('AdapThresh')

cv2.createTrackbar('Threshold', 'Thresh', 3, 254, onTrackBarChange)
cv2.createTrackbar('BlockSize', 'AdapThresh', 1, 49, onTrackBarChange)

img = cv2.imread('DATA/crossword.jpg', 0)

while True:

    th_level = cv2.getTrackbarPos('Threshold', 'Thresh')
    blk_size = cv2.getTrackbarPos('BlockSize', 'AdapThresh')
    blk_size = 2*blk_size +1
    if blk_size < 3:
        blk_size = 3

    ret, th1 = cv2.threshold(img, th_level, 255, cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blk_size, 8)

    assert isinstance(th1, object)
    assert isinstance(th2, object)

    blnd = cv2.addWeighted(src1=th1, alpha=0.6, src2=th2, beta=0.4, gamma=1)

    k = cv2.waitKey(1) & 0xFF
    show_pic('Orig', img)
    show_pic('Thresh', th1)
    show_pic('AdapThresh', th2)
    show_pic('Blend', blnd)

    if k == 27 or k == 32:
        break
cv2.destroyAllWindows()
