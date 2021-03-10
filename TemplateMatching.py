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

# All the 6 methods for comparison in a list
# Note how we are using strings, later on we'll use the eval() function to convert to function
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

full_s = cv2.imread('..\DATA\sammy.jpg')
face = cv2.imread('..\DATA\sammy_face.jpg')
count=0

for m in methods:

    # Create a copy
    full_copy=full_s.copy()
    curr_Method = eval(m)

    # Template matching
    res = cv2.matchTemplate(full_copy,face,curr_Method)

    # Grab min and max values and calculate the top_left and bottom right pts of rectangle
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if curr_Method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    height, width, chan = face.shape

    bottom_right = (top_left[0]+width, top_left[1]+height)

    # Place the red rectangle on identified ROI
    cv2.rectangle(full_copy, top_left, bottom_right, (0, 255, 0), 3)

    # Plot and show the images
    count += 1
    plt.subplot(2, 6, count)
    plt.imshow(res)
    plt.title('Heat '+m)

    count +=1
    plt.subplot(2, 6, count)
    plt.imshow(full_copy)
    plt.title('Detect '+m)

plt.show()
print('\n')





