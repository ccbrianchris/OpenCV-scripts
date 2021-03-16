#### RECORDING IMAGE WITH ORB FEATURE DETECTION


import cv2
video = cv2.VideoCapture("C:/Users/BRIAN CHRIS/Downloads/videoplayback.mp4")
webcam = cv2.VideoCapture(0)

imag = cv2.imread("C:/Users/BRIAN CHRIS/Downloads/4.jpg")
sucess,image = video.read()

WT,HT,CT = image.shape

imag = cv2.resize(imag,(HT,WT))
cv2.imshow("video",image)
cv2.imshow("image",imag)

while True:
    
    websucess,webc = webcam.read()
    obs = cv2.ORB_create(nfeatures = 2000)
    kp2,desti2 = obs.detectAndCompute(webc,None)
    webc = cv2.drawKeypoints(webc,kp2,None)
    
    cv2.imshow("WEBCAM",webc)
    if cv2.waitKey(1) & 0XFF == 27:
        break


cv2.waitKey(0)
webcam.release()
video.release()        
cv2.destroyAllWindows()