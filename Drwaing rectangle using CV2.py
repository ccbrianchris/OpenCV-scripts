#DRAWING RECTANGE USING CV2

import cv2
import numpy as np


# Variables for Drwaing Rectangle

drawing = False
ix,iy = -1,-1

#creating function to record mouse action
def rectangle(events,x,y,flag,params):
    
    global drawing,ix,iy
    
    if events == cv2.EVENT_LBUTTONDOWN:
        
        drawing = True
        ix,iy = x,y
        cv2.rectangle(rectangleImage,(ix,iy),(x,y),(0,0,255),-1)
        
    elif events == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            
            cv2.rectangle(rectangleImage,(ix,iy),(x,y),(0,0,255),-1)
        
    elif events == cv2.EVENT_LBUTTONUP:
        drawing = False
        ix,iy = x,y
        cv2.rectangle(rectangleImage,(ix,iy),(x,y),(0,0,255),-1)





#Calling function

cv2.namedWindow(winname = "Rectangle_Draw")
cv2.setMouseCallback("Rectangle_Draw",rectangle)

# creating image

rectangleImage = np.zeros((512,512,3))
while True:
    
    cv2.imshow("Rectangle_Draw",rectangleImage)
    
    if cv2.waitKey(1) & 0xFF == 27:
        
        break
    
    
    
    
cv2.destroyAllWindows()




















#########################################################################################################
#############Drawing Rectngle without Filling ###########################################################
#########################################################################################################




import numpy as np
import cv2
import PIL
import matplotlib.pyplot as plt

%matplotlib inline


drawing = False
ix,iy = -1,-1

#creating function to record mouse action
def rectangle(events,x,y,flag,params):
    
    global drawing,ix,iy
    
    if events == cv2.EVENT_LBUTTONDOWN:
        
        drawing = True
        ix,iy = x,y
        cv2.rectangle(brian,(ix,iy),(x,y),(0,0,255),thickness=1)
        
    elif events == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            drawing = False
            
            cv2.rectangle(brian,(ix,iy),(x,y),(0,0,255),thickness=1)
        
    elif events == cv2.EVENT_LBUTTONUP:
        drawing = False
        #ix,iy = x,y
        cv2.rectangle(brian,(ix,iy),(x,y),(0,0,255),thickness=1)

cv2.namedWindow(winname = "brian")
cv2.setMouseCallback("brian",rectangle)
brian = PIL.Image.open("C:/Users/BRIAN CHRIS/Downloads/4.jpg")
brian = np.asarray(brian)


while True:
    cv2.imshow("brian",brian)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
