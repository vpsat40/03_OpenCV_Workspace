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
    corHar_img=cv2.dilate(corHar_img,None)

    return corHar_img
    
def shiTomasiDetect(src_img, gray_img, numCorners):

    corners = cv2.goodFeaturesToTrack(gray_img, numCorners, 0.01, 10)
    corners = np.int0(corners)

    for i in corners:
        x,y = i.ravel()
        cv2.circle(src_img, (x,y), 3, 255, -1)

    return src_img


flat_chess = cv2.imread('../DATA/flat_chessboard.png')
flat_chess = cv2.cvtColor(flat_chess,cv2.COLOR_BGR2RGB)
gray_flat_chess = cv2.cvtColor(flat_chess,cv2.COLOR_BGR2GRAY)
fin_flatChess = flat_chess.copy()
harris_img = harrisCornerDetect(gray_flat_chess)
fin_flatChess[harris_img>0.01*harris_img.max()] = [255,0,0]

real_chess = cv2.imread('../DATA/real_chessboard.jpg')
real_chess = cv2.cvtColor(real_chess,cv2.COLOR_BGR2RGB)
gray_real_chess = cv2.cvtColor(real_chess,cv2.COLOR_BGR2GRAY)
fin_grayChess = real_chess.copy()
harris_img = harrisCornerDetect(gray_real_chess)
fin_grayChess[harris_img > 0.01*harris_img.max()] = [255,0,0]

shiTom_flatChess = shiTomasiDetect(flat_chess, gray_flat_chess, 70)

shiTom_grayChess = shiTomasiDetect(real_chess, gray_real_chess, 150)


plt.subplot(331)
plt.imshow(flat_chess)
plt.subplot(332)
plt.imshow(gray_flat_chess,cmap='gray')
plt.subplot(333)
plt.imshow(real_chess)
plt.subplot(335)
plt.imshow(gray_real_chess,cmap='gray')
plt.subplot(334)
plt.imshow(fin_flatChess)
plt.subplot(336)
plt.imshow(fin_grayChess)
plt.subplot(337)
plt.imshow(shiTom_flatChess)
plt.subplot(339)
plt.imshow(shiTom_grayChess)



plt.show()

