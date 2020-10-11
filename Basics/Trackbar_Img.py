import numpy as np
import cv2


def trkBar_OnChange(num): print(num)


# Identify and name the window for future objects
cv2.namedWindow('image')

# Create trackbars in image window
cv2.createTrackbar('Blue', 'image', 0, 255, trkBar_OnChange)
cv2.createTrackbar('Green', 'image', 0, 255, trkBar_OnChange)
cv2.createTrackbar('Red', 'image', 0, 255, trkBar_OnChange)

# Create a variable switch
switch = 'ON/OFF'
cv2.createTrackbar(switch, 'image', 0, 1, trkBar_OnChange)

# Create a black image of size 512x512x3
img = np.zeros((512, 512, 3), np.uint8)

# Read a local image
# img = cv2.imread('DATA/00-puppy.jpg')

while True:
    b = cv2.getTrackbarPos('Blue', 'image')
    g = cv2.getTrackbarPos('Green', 'image')
    r = cv2.getTrackbarPos('Red', 'image')
    swt = cv2.getTrackbarPos(switch, 'image')

    assert isinstance(img, object)
    if swt == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
