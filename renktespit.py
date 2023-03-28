import cv2 
import numpy as np
from collections import deque
    
buffer_size=16
pts=deque(maxlen=buffer_size)

blueLower=(100,110,0)
blueUpper=(200,255,255)

cap=cv2.VideoCapture(0)
cap.set(4,960)
cap.set(3,480)

while True:
    success, imgOriginal=cap.read()
    if success:
        blurred=cv2.GaussianBlur(imgOriginal, (11,11),  0)
        hsv=cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)
        cv2.imshow("Merhaba",hsv)
        mask=cv2.inRange(hsv,blueLower,blueUpper)
        cv2.imshow("Masked Image",mask)
        mask=cv2.erode(mask,None,iterations=2)
        mask=cv2.dilate(mask,None,iterations=2)
        cv2.imshow("Mask+erozyon+genisleme",mask)
        (_,contours,_)=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        center=None 
        if len(contours)>0:
            c=max(contours,key=cv2.contourArea)
            rect=cv2.minAreaRect(c)
            ((x,y),(width,height),rotation)=rect
            s="x:{},y:{},width{},height{},rotation{}".format(np.round(x),np.round(y),np.round(width),np.round(height),np.round(rotation))    
            print(s)
            box=cv2.boxPoints(rect)
            box=np.int64(box)
            M=cv2.moments(c)    
            center=(int(M["n10"]/M["n00"]),int(M["n01"]/M["n00"]))
            cv2.drawContours(imgOriginal,[box],0, (0,255,255),2)
            cv2.circle(imgOriginal,center,5,(255,0,255),-1)
            cv2.putText(imgOriginal,s,(25,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,0),2)
            
            
        cv2.imshow("Son Hali",imgOriginal)    
        pts.appendleft(center)
        for i in range(1,len(pts)):
            if pts[i -1] is None or pts[i] is None: continue
            cv2.line(imgOriginal,pts[i -1], pts[i], (0,255,0),3)
            
            
    if cv2.waitKey(1) & 0xFF == ord("q"): break