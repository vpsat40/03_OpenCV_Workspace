import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import cv2

blank_img = np.zeros(shape=(512, 512, 3), dtype=np.int16)
cv2.rectangle(blank_img, pt1=(384, 10), pt2=(500, 150), color=(0, 0, 255), thickness=7, lineType=cv2.LINE_4)

# img = cv2.imread('DATA/00-puppy.jpg')
plt.imshow(blank_img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
