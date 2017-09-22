import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("photo.jpg")

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face=face_cascade.detectMultiScale(gray_img,
                                   scaleFactor=1.05,
                                   minNeighbors=5)

for x,y,w,h in face:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

print(type(face))
print(face)


cv2.imshow("Gray",img)
cv2.waitKey(0)
cv2.destroyAllWindows()