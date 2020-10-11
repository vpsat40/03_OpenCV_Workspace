import numpy as np
import cv2

def clk_evt(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ', ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        cv2.putText(img, strXY, (x,y), font, 1, (0,0,255), 2)
        #cv2.imshow('pups', img)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 20, (0, 0, 255), 3)
        #blue = img[y, x, 0]
        #green = img[y, x, 1]
        #red = img[y, x, 2]
        #font = cv2.FONT_HERSHEY_SIMPLEX
        #strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        #cv2.putText(img, strBGR, (x,y), font, 1, (0,255,255), 1)
        #cv2.imshow('pups', img)
        
#img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('DATA/00-puppy.jpg')

while True:    
    cv2.setMouseCallback('pups', clk_evt)
    cv2.imshow('pups', img)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()