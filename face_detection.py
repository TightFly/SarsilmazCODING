import cv2
import numpy as npimport, os
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
face_cascade = cv2.CascadeClassifier("faceCascade.xml")

cap = cv2.VideoCapture("ffplay -probesize 128 -sync video -an -sn -fast -infbuf -f mpegts -i udp://127.1.1.0:10000", cv2.CAP_FFMPEG)

while True:
    
    ret, frame = cap.read()
        
    if ret:
        
        height,width,d = frame.shape
        cv2.circle(frame,(int(width/2),int(height/2)),5,(0,0,255),-1)
        face_rect = face_cascade.detectMultiScale(frame, minNeighbors = 7)
        
        
        for (x,y,w,h) in face_rect:
            cv2.rectangle(frame, (x,y),(x+w, y+h),(0,255,0),5)
            cv2.circle(frame,(int(x+w/2),int(y+h/2)),5,(255,0,0),-1)
            MotorPixel = (x+w/2)- (width/2)
            #MotorMeter = MotorPixel*0.0264583333337192
            outfile = open('data.txt', 'w')
            #outfile.write = MotorMeter
            outfile.close()
            
        cv2.imshow("face detect", frame)
             
        #print(MotorMeter)
        
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()