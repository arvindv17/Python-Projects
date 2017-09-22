"""
This project is aimed to perform motion detection using the computer webcam.

__author__=Arvind
__Date__=09/21/2017
__PythonVersion__=2.7
"""


import cv2,time
from datetime import datetime
import pandas

first_frame=None
#Creating a video capture object
video=cv2.VideoCapture(0)
status_list=[None,None]
times=[]
df=pandas.DataFrame(columns=["Start","End"])
"""
check is a boolean datatype, frame is a numpy array
check - True ( to check if the webcam is on or not)
frame is the numpy array captured by the camera
"""
while True:
    check,frame=video.read()
    status=0
    #Converting it to grayscale
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame=gray
        continue

    delta_frame=cv2.absdiff(first_frame,gray)
    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame,None,iterations=2)

    (_,cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status=1
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
        status_list.append(status)
        if status_list[-1]==1 and status_list[-2]==0:
            times.append(datetime.now())
        elif status_list[-1] == 0 and status_list[-2] == 1:
            times.append(datetime.now())




    #Setting a timer to see that the webcam be on for that duration
    #time.sleep(3)
    cv2.imshow("Gray Frame",gray)
    cv2.imshow("Delta",delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame",frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        if status==1:
            times.append(datetime.now())
        break
    #print(status)

#Release the webcam after the process has been completed
for i in range(0,len(times),2):
    df=df.append({"Start":times[i],"End":[i+1]},ignore_index=True)

df.to_csv("Time.csv")
video.release()
cv2.destroyAllWindows()