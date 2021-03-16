### Drawing lines on a live image


import cv2

# defining function for event tracking

def rectangle_call(events,x,y,flags,param):
    
    global pt1,pt2,left_click,right_click
    
    if events == cv2.EVENT_LBUTTONDOWN:
        
        
         #Need to reset all co-ordinates since rectangle is drawn(meaning both mouse buttons are clicked)
        if left_click == True and right_click == True:
            pt1 = 0
            pt2 = 0
            left_click = 0
            right_click = 0
        
        if left_click == False:
            pt1 = (x,y)
            left_click = True                       #elif is compulsary to get two cordinates
        
        elif right_click == False:
            pt2 = (x,y)
            right_click = True
            
            



#Defining initial variables
pt1 = 0
pt2 = 0
left_click = 0
right_click = 0

#calling function
vcap = cv2.VideoCapture(0)
cv2.namedWindow(winname = "testingvideo")
cv2.setMouseCallback("testingvideo",rectangle_call)

# displaying of images




while True:
    val,frames = vcap.read()
    
    if left_click == True:
        cv2.circle(frames,(pt1),5,(0,0,255),-1)
    
    if left_click == True and right_click == True:        
        cv2.rectangle(frames, pt1, pt2, (0, 0, 255), 2)
    
    cv2.imshow("testingvideo",frames)
    
    if cv2.waitKey(1) & 0XFF == ord("q"):
        break

vcap.release()
cv2.destroyAllWindows()
    