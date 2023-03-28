"""import cv2,os

cap=cv2.VideoCapture(0)
biscuit=cv2.CascadeClassifier("classifier\cascade.xml")
font1=cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret,Frame=cap.read()
    Frame=cv2.flip(Frame,1)
    gray=cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)
    biscuits=biscuit.detectMultiScale(gray,3,5)
    for (x,y,w,h) in biscuits:
        cv2.rectangle(Frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(Frame,"bebe bisküvisi",(x,y),font1,1,(255,0,0),cv2.LINE_4)
    cv2.imshow("bebe bisküvisi" , Frame)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
    cap.release()
    cv2.destroyAllWindows()"""


import cv2
face_cascade=cv2.CascadeClassifier(r'C:/Program Files/biscuit/classifier/cascade.xml')
img=cv2.imread("C:/Program Files/biscuit/classifier/p/1649458546321.jpg")
resized = cv2.resize(img,(400,200))
gray=cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,6.5,17)
for(x,y,w,h) in faces:
    resized=cv2.rectangle(resized,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('img',resized)
cv2.waitKey(0)
cv2.destroyAllWindows()