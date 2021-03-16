# Taking picture using CV2 python

import matplotlib.pyplot as plt
%matplotlib inline
import cv2
capture = cv2.VideoCapture(0)

while True:
    ret, image = capture.read()
    cv2.imshow('Camera stream', image)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()

image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image)