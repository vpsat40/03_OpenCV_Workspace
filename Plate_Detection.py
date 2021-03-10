import numpy as np
import cv2
import matplotlib.pyplot as plt

def disp_cvimage(img):
    cv2.imshow('RusPlate', img)

    while True:
        k = cv2.waitKey(1) & 0xFF

        if k == 27 or k == 32:
            break

        cv2.destroyAllWindows()


def disp_matimage(subpl, img, isGray):
    plt.subplot(subpl)
    if isGray:
        plt.imshow(img,cmap='grey')
    else:
        plt.imshow(img)


def detect_plate(img):
    plt_img = img.copy()

    plt_rects = plate_cascade.detectMultiScale(plt_img, scaleFactor=1.2)

    for (x,y,w,h) in plt_rects:
        cv2.rectangle(plt_img,(x,y),(x+w,y+h),(255,0,0),4)

    return plt_img,plt_rects


def detect_and_blur(img, verts):
    blurred_plt = img.copy()
    x,y,w,h = verts[0]
    blur_im = blurred_plt[y:y+h,x:x+w,:]

    blur_im = cv2.medianBlur(blur_im,5)

    blurred_plt[y:y+h, x:x+w, :] = blur_im

    return blurred_plt


plate = cv2.imread('../DATA/car_plate.jpg')
src_plate = cv2.cvtColor(plate, cv2.COLOR_BGR2RGB)
disp_matimage(131, src_plate, False)

plate_cascade = cv2.CascadeClassifier('../DATA/haarcascades/haarcascade_russian_plate_number.xml')
res_img, rects = detect_plate(src_plate)
disp_matimage(132, res_img, False)
print(rects)
blurred_im = detect_and_blur(src_plate,rects)
print(blurred_im.shape)
disp_matimage(133, blurred_im, False)

plt.show()