#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""



"""

import cv2
from dronekit import Command, connect, VehicleMode, LocationGlobalRelative
import time
from pymavlink import mavutil
import math


ortalamapayi = 40


#DRONE BAĞLANTISI
connection_string="127.0.0.1:14551"
#connection_string="192.168.137.1:14550" 
global iha
iha=connect(connection_string,wait_ready=True,timeout=100)
#iha=connect(connection_string,wait_ready=True,timeout=100,baud=115200)










#mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED

def send_velocity(velocity_x, velocity_y, velocity_z, duration):
    msg = iha.message_factory.set_position_target_local_ned_encode(
     0,
     0, 0,
     mavutil.mavlink.MAV_FRAME_LOCAL_NED, 
     0b0000011111000111,
     0, 0, 0, 
     velocity_x, velocity_y, velocity_z,
     0, 0, 0,
     0, math.radians(0))
                
        
    for x in range(0,duration):
        iha.send_mavlink(msg)
        time.sleep(1)
    
    
    





def goright(süre):
    send_velocity(0,0.30,0,1)                             
                                                          
def goleft(süre):
    send_velocity(0,-0.30,0,1)

def goup(süre):
    send_velocity(0,0,0.30,1)

def godown(süre):
    send_velocity(0,0,-0.30,1)







def ortala(centerX,centerY,width,height):
    iha.mode = VehicleMode("GUIDED")
    
    is_ortalandi = False
    
    if centerX < width/2-ortalamapayi:        
        print("Solda")
        goleft(1)
        return is_ortalandi
    
    if centerX > width/2+ortalamapayi:
        print("Sagda")
        goright(1)
        return is_ortalandi
    
    if centerY > height/2+ortalamapayi:
        print("Aşağıda")
        godown(1)
        return is_ortalandi
    
    if centerY < height/2-ortalamapayi:
        print("Yukarda")
        goup(1)
        return is_ortalandi
    
    if centerX > width/2-ortalamapayi and centerX < width/2+ortalamapayi and centerY < height/2+ortalamapayi and centerY > height/2-ortalamapayi:
        print("ortalandı")
        is_ortalandi = True
        return is_ortalandi











## sınıflandırıcı
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


# video
cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    
    
    
    if ret:
        
        height,width,d = frame.shape
        cv2.circle(frame,(int(width/2),int(height/2)),5,(0,0,255),-1)
        face_rect = face_cascade.detectMultiScale(frame, minNeighbors = 7)
        
        
        for (x,y,w,h) in face_rect:
            cv2.rectangle(frame, (x,y),(x+w, y+h),(0,255,0),5)
            cv2.circle(frame,(int(x+w/2),int(y+h/2)),5,(255,0,0),-1)
            centerX = x+(w//2)
            centerY = y+(h//2)
            ortala(centerX,centerY,width,height)
            
            
            
        cv2.imshow("face detect", frame)

        
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
           break





cap.release()
cv2.destroyAllWindows()