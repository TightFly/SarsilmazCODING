import cv2
import numpy as np


import time


cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 480)

_, frame = cap.read()
rows, cols, _ = frame.shape
kilit = 0

x_medium = int(rows / 2)
center = int(rows / 2)
y_medium = int(cols / 2)-40
ycenter = int(cols / 2)+20
position = 120 # degrees
positiony = 80 # degrees
hedefyok=0
cnt=[]
while True:
    _, frame = cap.read()
    frame =cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # red color
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    contours,hiec = cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #_, contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    if contours == []:
        hedefyok +=1
        kilit=0
        if hedefyok>120:
            position = 120 # degrees
            positiony = 100 # degrees
            x_medium = 240
            y_medium = 180
            hedefyok=0
            kilit=0
            
    print('hyok',hedefyok)
    for cnt in contours:
        #(x, y, w, h) = cv2.boundingRect(cnt)
        area = cv2.contourArea(cnt)
        if area > 200:
            
            (x, y, w, h) = cv2.boundingRect(cnt)
            x_medium = int((x + x + w) / 2)
            y_medium = int((y+y+h)/2)-40
            cv2.circle(frame, (x_medium, y_medium+40),30, (255, 0, 0), 2)

        break
    
    cv2.line(frame, (x_medium, 0), (x_medium, 320), (0, 255, 0), 2)
    cv2.line(frame, (0, y_medium), (480, y_medium), (0, 255, 0), 2)
    cv2.imshow("Frame", frame)
    
    
    key = cv2.waitKey(1)
    
    


    
    
    cap.release()
    cv2.destroyAllWindows()

