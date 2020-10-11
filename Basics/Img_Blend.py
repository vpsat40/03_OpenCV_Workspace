import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('DATA/dog_backpack.png')
img2 = cv2.imread('DATA/watermark_no_copy.png')
img1_p = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2_p = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# Resize the image 2
img2 = cv2.resize(img2, (600, 600))
img2_p = cv2.resize(img2_p, (600, 600))

# Calculate the place to put in the blended image and ROI
x_offset = 934 - 600
y_offset = 1401 - 600

roi = img1[y_offset:1401, x_offset:934]
roi_p = img1_p[y_offset:1401, x_offset:934]

# Get grayscale of image2 and inverse it
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# img2gray_p = cv2.cvtColor(img2_p, cv2.COLOR_RGB2GRAY)

mask_inv = cv2.bitwise_not(img2gray)
# mask_inv_p = cv2.bitwise_not(img2gray_p)

# reshape
white_bg = np.full(img2.shape, 255, dtype=np.uint8)
bk = cv2.bitwise_or(white_bg, white_bg, mask=mask_inv)


fg = cv2.bitwise_or(img2, img2, mask=mask_inv)
fg_p = cv2.bitwise_or(img2_p, img2_p, mask=mask_inv)

final_roi = cv2.bitwise_or(roi, fg)
final_roi_p = cv2.bitwise_or(roi_p, fg_p)

large_img = img1
small_img = final_roi
large_img[y_offset:y_offset+small_img.shape[0], x_offset:x_offset+small_img.shape[1]] = small_img

large_img_p = img1_p
small_img_p = final_roi_p
large_img_p[y_offset:y_offset+small_img_p.shape[0], x_offset:x_offset+small_img_p.shape[1]] = small_img_p

while True:

    # plt.imshow(large_img_p)
    # plt.show()
    cv2.imshow('blended_p', large_img_p)
    cv2.imshow('blended', large_img)
    cv2.imshow('final_roi_p', final_roi_p)
    cv2.imshow('final_roi', final_roi)

    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()




