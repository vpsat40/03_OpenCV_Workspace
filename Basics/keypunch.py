#!/usr/bin/python3
import cv2

img = cv2.imread('DATA/rainbow.jpg')

while True:
    cv2.imshow('r', img)
    k = cv2.waitKey(1) & 0xFF

    if k == 27:
        break
    elif k != 255:
        print(k)
cv2.destroyAllWindows()
