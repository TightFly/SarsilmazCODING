import cv2
import mediapipe as mp
import time, os, sys, math
import serial
#from STorM32_lib import *
#myrtmp_addr = "rtmp://192.168.137.1:1935/"
uart = "COM37"
baud = 115200
display = True


t1Hz_last = time.perf_counter()

pitch = 0.0
pitch_dir = 1.0
yaw = 0.0
yaw_dir = 1.0
roll = 0.0
roll_dir = 1.0
basla = 0

if len(sys.argv) > 1:
    print(sys.argv[1])
    if sys.argv[1] == '57' or sys.argv[1] == '57600':
        baud = 57600
    if sys.argv[1] == '115' or sys.argv[1] == '115200':
        baud = 115200
    if sys.argv[1] == '921' or sys.argv[1] == '921600':
        baud = 921600

#cmd = cCMD_SETANGLES(ser, pitch, roll, yaw)
#cmd.send()
#print(">- ", cmd.getCmd())

cap = cv2.VideoCapture(0)
pTime = 0

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection(0.70)
_, frame = cap.read()
rows, cols, _ = frame.shape
x_medium = int(cols / 2)
y_medium = int(rows / 2)
#print(x_medium)
#print(y_medium)
position = 0  # degrees
position2 = 0

while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    #print(results)


    if results.detections:
        for id, detection in enumerate(results.detections):


            bboxC = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                   int(bboxC.width * iw), int(bboxC.height * ih)

            cv2.rectangle(img, bbox, (255, 0, 255), 2)
            #cv2.line(img,bbox,(0,255,255),2)
            #print(detection)
            cv2.putText(img, f'{int(detection.score[0] * 100)}%',
                        (bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_PLAIN,
                        2, (0, 255, 0), 2)
            #cv2.line(img, (int((bbox[0]+(bbox[0]+bbox[2]))/2), int((bbox[1]+(bbox[1]+bbox[3]))/2)), (bbox[0]+bbox[2], bbox[1]+bbox[3]), (0, 255, 0), 2)
            #print(int((bbox[0]+(bbox[0]+bbox[2]))/2))
            basla=1






    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (0, 255, 0), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)

    if basla > 0:
        if x_medium < int((bbox[0]+(bbox[0]+bbox[2]))/2) - 50:
            if position >= 100:
                position = 100
            else:
                position += 0.5
        elif x_medium > int((bbox[0]+(bbox[0]+bbox[2]))/2) + 50:
            if position <= -100:
                position = -100
            else:
                position -= 0.5

        if y_medium < int((bbox[1]+(bbox[1]+bbox[3]))/2) - 30:
            if position2 >= 20:
                position2 = 20
            else:
                position2 += 0.2
        elif y_medium > int((bbox[1]+(bbox[1]+bbox[3]))/2) + 30:
            if position2 <= -40:
                position2 = -40
            else:
                position2 -= 0.2


    print(position2)
    pitch=position2
    yaw=-position

