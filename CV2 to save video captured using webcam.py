#### CV2 to record and store video in gray format


import cv2

sets = cv2.VideoCapture(0)

width = int(sets.get(cv2.CAP_PROP_FRAME_WIDTH))
height =int(sets.get(cv2.CAP_PROP_FRAME_HEIGHT))
count_of_frame = int(sets.get(cv2.CAP_PROP_FRAME_COUNT))

# To write or download a video in locally we will create a variable with parameters to store


writer = cv2.VideoWriter("Videotest0200.mp4",cv2.VideoWriter_fourcc(*"DIVX"),20,(width,height))
while True:
    capt,catv = sets.read()
   
    gray = cv2.cvtColor(catv,cv2.COLOR_BGR2GRAY)
    cv2.imshow("name",gray)
    writer.write(gray)
    if cv2.waitKey(9) & 0XFF == ord("q"):
        break
        
print("saved")

sets.release()

writer.release()
cv2.destroyAllWindows()
