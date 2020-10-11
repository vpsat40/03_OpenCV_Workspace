import numpy as np
import cv2
import matplotlib.pyplot as plt
#%matplotlib inline

img = cv2.imread('DATA\dog_backpack.jpg')
#type(img_b)

#plt.imshow(img)
cv2.imshow('bkpk_dog', img)

while True:
    if cv2.waitKey(5000) & 0xFF == 27:
        break

cv2.destroyAllWindows()

