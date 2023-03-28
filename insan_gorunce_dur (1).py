#IMPORTS
import cv2
import matplotlib.pyplot as plt
import time
from dronekit import Command, connect, VehicleMode, LocationGlobalRelative
import time
from pymavlink import mavutil
import math
import keyboard 



#ÖN TANIMLAMALAR
ortalamapayi = 40
global centerX
#SINIFLANDIRMA
face_cascade = cv2.CascadeClassifier("/home/pi/Desktop/KODLAR/faceDetection/FaceDetection/faceCascade.xml")


# DRONE BAĞLANTISI
connection_string="127.0.0.1:14550"
#connection_string="192.168.137.1:14550" 
global iha
#iha=connect(connection_string,wait_ready=True,timeout=100)
#iha=connect(connection_string,wait_ready=True,timeout=100,baud=115200)
iha=connect('/dev/ttyS0', wait_ready=True, baud=57600)




#FONKSİYONLAR------------------------------------------------------------------




def mode(mode):
    iha.mode = iha.VehicleMode(mode)
    while mode != iha.mode:
        print(f"Mod değiştiriliyor. {mode} ")
        time.sleep(1)



#------------------------------------------------------------------------------
        
        

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


def ortala_iha(centerX,width):
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
    
    if centerX > (width/2)-ortalamapayi and centerX < (width/2)+ortalamapayi:
        print("ortalandı")
        is_ortalandi = True
        return is_ortalandi


#------------------------------------------------------------------------------


def face_detect():
    
    
    cap = cv2.VideoCapture(0)
    global centerX, width
    
    while True:
        
        ret, frame = cap.read()
        height,width,d = frame.shape
        face_rect = face_cascade.detectMultiScale(frame, minNeighbors = 7)
        
                
        if  len(face_rect) == 1:
            
            for (x,y,w,h) in face_rect:
                centerX = x+(w//2)
                return centerX, width, len(face_rect)
            
        elif len(face_rect) > 1:
             return centerX, width, len(face_rect)
        else:
             return centerX, width, len(face_rect)
        
            
        
            
        
        
    
                
#------------------------------------------------------------------------------    

        


#GÖREV    



try:
    
    i = 0
    while True:
    
        centerX, width, algilama = face_detect()
        
        
        if algilama == 1 :
            
            i = i+1
            
            if (centerX > (width/2)-ortalamapayi and centerX < (width/2)+ortalamapayi):
               print("ortalandı")
            if (centerX > (width/2)-ortalamapayi and centerX < (width/2)+ortalamapayi) == 0:
               
               centerX, width, algilama = face_detect()
               iha.mode = VehicleMode("BRAKE")
               is_ortalandi=ortala_iha(centerX,width)

                
        elif algilama > 1:
            i = i+1
            print("birden fazla nesne algılanıyor")
        else:
            i = i+1
            print("algılanamıyor")  
            
        if i==10:
            break
        
except KeyboardInterrupt:
    pass









#try:
#    
#    
#    while True:
#    
#        centerX, width, algilama = face_detect()
#        
#        
#        if algilama == 1 :
#            
#            if (centerX > (width/2)-ortalamapayi and centerX < (width/2)+ortalamapayi):
#               print("ortalandı")
#            if (centerX > (width/2)-ortalamapayi and centerX < (width/2)+ortalamapayi) == 0:
#               
#               centerX, width, algilama = face_detect()
#               
#               if algilama == 1:
#                   iha.mode = VehicleMode("BRAKE")
#                   is_ortalandi=ortala_iha(centerX,width)
#               elif algilama > 1:
#                  print("birden fazla nesne algılanıyor")
#               else:
#                  print("algılanamıyor")       
#    
#                
#        elif algilama > 1:
#            print("birden fazla nesne algılanıyor")
#        else:
#            print("algılanamıyor")       
#        
#except KeyboardInterrupt:
#    pass
#





    
    

        







        














#while True:
#    
#    centerX, width, algilama = face_detect()
#    
#    
#    if algilama == 1 :
#        
#        while (centerX > (width/2)-ortalamapayi and centerX < (width/2)+ortalamapayi and algilama)==0:
#           
#           centerX, width, algilama = face_detect()
#           iha.mode = VehicleMode("BRAKE")
#           is_ortalandi=ortala_iha(centerX,width)
#            
#        
#    else:
#        print("algılanamıyor")





















## video
#cap = cv2.VideoCapture(0)
#
#while True:
#    
#    ret, frame = cap.read()
#    face_rect = face_cascade.detectMultiScale(frame, minNeighbors = 7)
#    height,width,d = frame.shape
#    cv2.circle(frame,(int(width/2),int(height/2)),5,(0,0,255),-1)
#    
#    if len(face_rect) >= 1:
#       print("algılandı")
#    
#            
#    for (x,y,w,h) in face_rect:
#        cv2.rectangle(frame, (x,y),(x+w, y+h),(255,255,255),6)
#        cv2.circle(frame,(int(x+w/2),int(y+h/2)),5,(0,255,255),-2)
#        
#        
#        
#        
#
#    cv2.imshow("face detect", frame)
#    
#    if cv2.waitKey(1) & 0xFF == ord("q"): 
#        break
#    else:
#        print("durdurulmadı")
#        
#
#
#cap.release()
#cv2.destroyAllWindows()





























