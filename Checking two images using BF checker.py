## Checking 2 image using ORB and BF_Checker
                                  ##############################################
                                  ##############Step -1#####################
                                  ###########################################

import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

def dis(img):
    fig = plt.figure(figsize = (12,12))
    ax = fig.add_subplot(111)
    ax.imshow(img)




namik = cv2.imread("C:/Users/BRIAN CHRIS/Downloads/namik.jpg")
namik = cv2.cvtColor(namik,cv2.COLOR_BGR2GRAY)
group = cv2.imread("C:/Users/BRIAN CHRIS/Downloads/namik2.jpg")
group = cv2.cvtColor(group,cv2.COLOR_BGR2GRAY)



# Finding the match of 2 images using ORB Match checker

orb_match = cv2.ORB_create()
kf1,desc1 = orb_match.detectAndCompute(namik,None)
kf2,desc2 = orb_match.detectAndCompute(group,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING,None)
match = bf.match(desc1,desc2)

#To call all short length matches

match = sorted(match,key = lambda x:x.distance)

namik_match = cv2.drawMatches(namik,kf1,group,kf2,match[0:20],None,flags = 2)
dis(namik_match)







                                 ##############################################
                                  ##############Step -2#####################
                                ################# Using SIFT ##############
                                  ###########################################














import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

def dis(img):
    fig = plt.figure(figsize = (12,12))
    ax = fig.add_subplot(111)
    ax.imshow(img)

    
dhoni = cv2.imread("C:/Users/BRIAN CHRIS/Downloads/dhoni1.jpg")
team = cv2.cvtColor(namik,cv2.COLOR_BGR2RGB)
group = cv2.imread("C:/Users/BRIAN CHRIS/Downloads/team.jpg")
group = cv2.cvtColor(group,cv2.COLOR_BGR2RGB)


# Shift create for more acurate reault

sift_create = cv2.SIFT_create()
kp01,description01 = sift_create.detectAndCompute(namik,None)
kp02,description02 = sift_create.detectAndCompute(group,None)



bf = cv2.BFMatcher()
matches = bf.knnMatch(description01,description02, k=2)

# To get shorter distances
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

# TO draw the match
namik_match01 = cv2.drawMatchesKnn(namik,kp01,group,kp02,good,None,flags=2)
dis(namik_match01)
