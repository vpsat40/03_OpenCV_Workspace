import numpy as np
import cv2

def clk_evt(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        points.append((x, y))
        
        if len(points) >=2:
            cv2.line(img, points[-1], points[-2], (255, 125, 0), 3)        
        cv2.imshow('pups', img)
    elif event == cv2.EVENT_RBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        print(blue, ',', green, ',', red)
        
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)        
        mycolimg = np.zeros((50, 50, 3), np.uint8)
        
        #mycolimg[:] = [blue, green, red]
        mycolimg[:, :, 0] = blue
        mycolimg[:, :, 1] = green
        mycolimg[:, :, 2] = red
        
        cv2.imshow('col', mycolimg)
        
#img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('DATA/00-puppy.jpg')
points = []
cv2.imshow('pups', img)

while True:    
    cv2.setMouseCallback('pups', clk_evt)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()