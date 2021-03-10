import numpy as np
import cv2
import matplotlib.pyplot as plt

def disp_img(img, cmap=None):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap)
    plt.show()

def show_pic(name, img):
    cv2.imshow(name, img)

def harrisCornerDetect(gray_img):

    # Convert input GrayScale Image to Float Values
    gray_float = np.float32(gray_img)

    # Apply corner harris detection
    corHar_img = cv2.cornerHarris(gray_float, blockSize=2, ksize=3, k=0.04)

    # Dialating the resultant image to mark the corners
    corHar_img=cv2.dilate(corHar_img, None)

    return corHar_img
    

flat_chess = cv2.imread('../DATA/flat_chessboard.png')
flat_chess = cv2.cvtColor(flat_chess,cv2.COLOR_BGR2RGB)
gray_flat_chess = cv2.cvtColor(flat_chess,cv2.COLOR_BGR2GRAY)
fin_flatChess = flat_chess.copy()
dst = harrisCornerDetect(gray_flat_chess)
fin_flatChess[dst>0.01*dst.max()] = [255,0,0]

real_chess = cv2.imread('../DATA/real_chessboard.jpg')
real_chess = cv2.cvtColor(real_chess,cv2.COLOR_BGR2RGB)

gray_real_chess = cv2.cvtColor(real_chess,cv2.COLOR_BGR2GRAY)


plt.subplot(231)
plt.imshow(flat_chess)
plt.subplot(232)
plt.imshow(gray_flat_chess,cmap='gray')
plt.subplot(233)
plt.imshow(real_chess)
plt.subplot(234)
plt.imshow(gray_real_chess,cmap='gray')
plt.subplot(235)
plt.imshow(fin_flatChess)

plt.show()
