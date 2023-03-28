#IMPORTS
import cv2
import time
from dronekit import connect, VehicleMode
from pymavlink import mavutil
import math

#ÖN TANIMLAMALAR
ortalamapayi = 40
global centerX
#SINIFLANDIRMA
face_cascade = cv2.CascadeClassifier(r"C:\Users\ alper\OneDrive\Masaüstü\CODING\ faceDetection\FaceDetection\ faceCascade.xml")


# DRONE BAĞLANTISI
connection_string="127.0.0.1:14550"
#connection_string="192.168.137.1:14550" 
global iha
#iha=connect(connection_string,wait_ready=True,timeout=100)
#iha=connect(connection_string,wait_ready=True,timeout=100,baud=115200)
iha=connect('/dev/ttyCOM6', wait_ready=True, baud=57600)

#FONKSİYONLAR------------------------------------------------------------------
        
        
#mavutil.mavlink.MAV_FRAME_LOCAL_NED,
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
                
        
    for x in range(0,duration):
        iha.send_mavlink(msg)
        time.sleep(1)
    
    
    

#------------------------------------------------------------------------------



def goright(süre):
    send_velocity(0,0.1,0,1)                             
                                                          
def goleft(süre):
    send_velocity(0,-0.1,0,1)


#------------------------------------------------------------------------------


def ortala_iha(centerX):
        
    iha.mode = VehicleMode("GUIDED")
    
    if centerX < 320 - ortalamapayi:
        print("Solda")
        goleft(1)
        return 
    
    if centerX > 320 + ortalamapayi:
        print("Sagda")
        goright(1)
        return
    
    if centerX > 320 - ortalamapayi and centerX < 320 + ortalamapayi:
        print("ortalandı")
        return


#------------------------------------------------------------------------------


def face_detect():
    
    global centerX
    
    cap1 = cv2.VideoCapture(0)
    cap=cv2.rotate(cap1, cv2.ROTATE_180)
    cap.set(3,640)
    ret, frame = cap.read()
    face_rect = face_cascade.detectMultiScale(frame, minNeighbors = 7)
    
            
    if  len(face_rect) == 1:
        
        for (x,y,w,h) in face_rect:
            centerX = x+(w//2)
            return centerX, len(face_rect)
        
    elif len(face_rect) > 1:
         return 0, len(face_rect)
    else:
         return 0, len(face_rect)
               
#------------------------------------------------------------------------------    
        
#GÖREV    
try:
    
    
    while True:
    
        centerX, algilama = face_detect()
        
        
        if algilama == 1 :
            
            if (centerX > 320 - ortalamapayi and centerX < 320 + ortalamapayi):
               print("ortalandı")
            if (centerX > 320-ortalamapayi and centerX < 320 +ortalamapayi) == 0:
               
               iha.mode = VehicleMode("BRAKE")
               ortala_iha(centerX)

                
        elif algilama > 1:
            print("birden fazla nesne algılanıyor")
        else:
            print("algılanamıyor")  


except KeyboardInterrupt:
    pass