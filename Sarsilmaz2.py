import cv2
import mediapipe as mp
import time
#from dronekit import connect, VehicleMode
#from pymavlink import mavutil
import math

#connection_string="127.0.0.1:14551"
#iha=connect(connection_string,wait_ready=True,timeout=100)










mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()
#myrtmp_addr = "rtmp://192.168.137.1:1935/"
cap = cv2.VideoCapture(2)
pTime = 0
i=0

width  =  cap.get(3)
height =  cap.get(4)
width  =  cap.get(3)
ortalamapayi=40
centerX=320

# mavutil.mavlink.MAV_FRAME_LOCAL_NED,
def send_velocity(velocity_x, velocity_y, velocity_z, duration):
    msg = iha.message_factory.set_position_target_local_ned_encode(
        0,
        0, 0,
        mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED,
        0b0000011111000111,
        0, 0, 0,
        velocity_x, velocity_y, velocity_z,
        0, 0, 0,
        0, math.radians(0))

    for x in range(0, duration):
        iha.send_mavlink(msg)
        time.sleep(1)


# ------------------------------------------------------------------------------


def goright(süre):
    send_velocity(0, 0.1, 0, 1)


def goleft(süre):
    send_velocity(0, -0.1, 0, 1)


# ------------------------------------------------------------------------------


def ortala_iha(centerX):
    # iha.mode = VehicleMode("GUIDED")

    if centerX < 320 - ortalamapayi:
        print("Solda" , centerX)
        # goleft(1)
        return

    if centerX > 320 + ortalamapayi:
        print("Sagda",centerX)
        # goright(1)
        return

    if centerX > 320 - ortalamapayi and centerX < 320 + ortalamapayi:
        print("ortalandıgibi")
        return


# ------------------------------------------------------------------------------


def face_detect(frame):
    global centerX

    # cap= cv2.VideoCapture(2)

    #    cap.set(3,640)
    #    ret, frame = cap.read()
    #    new_frame = cv2.rotate(frame,cv2.ROTATE_180)
    face_rect = face_cascade.detectMultiScale(frame, minNeighbors=7)
    cv2.circle(frame, (int(320), int(240)), 5, (0, 0, 255), -1)

    if len(face_rect) == 1:

        for (x, y, w, h) in face_rect:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(frame, (int(x + w / 2), int(y + h / 2)), 5, (255, 0, 0), -1)
            centerX = x + (w // 2)
            return centerX, len(face_rect)

    elif len(face_rect) > 1:
        return 0, len(face_rect)
    else:
        return 0, len(face_rect)


# ------------------------------------------------------------------------------






while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    #print(results.pose_landmarks)
    if results.pose_landmarks:
        #mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            #print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            color = 255



            cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
            centerX=cx

            if (centerX > 320 - ortalamapayi and centerX < 320 + ortalamapayi):
                print("ortalandı",centerX)

            if (centerX > 320 - ortalamapayi and centerX < 320 + ortalamapayi) == 0:
                # iha.mode = VehicleMode("BRAKE")
                ortala_iha(centerX)

            break




            #cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)


# FONKSİYONLAR------------------------------------------------------------------


# GÖREV

try:

    cap = cv2.VideoCapture(2)

    while True:

        ret, frame = cap.read()
        # new_frame = cv2.rotate(frame,cv2.ROTATE_180)
        cv2.imshow("face detect", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        centerX, algilama = face_detect(frame)

        if algilama == 1:

            if (centerX > 320 - ortalamapayi and centerX < 320 + ortalamapayi):
                print("ortalandı")
            if (centerX > 320 - ortalamapayi and centerX < 320 + ortalamapayi) == 0:
                # iha.mode = VehicleMode("BRAKE")
                ortala_iha(centerX)


        elif algilama > 1:
            print("birden fazla nesne algılanıyor")
        else:
            print("algılanamıyor")



except KeyboardInterrupt:
    pass


