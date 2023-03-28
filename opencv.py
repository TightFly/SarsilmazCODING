import cv2, sys
#Haar cascade classifier yukle
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0) #dosyayi okumak icin

while True:
    ret,frame = video_capture.read() #video frameleri oku
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #frameleri siyah-beyaz yap
    faces = faceCascade.detectMultiScale(gray, 1.1, 5, minSize=(100,100)) #yuzleri bul
    for (x,y,w,h) in faces: #yuzleri isaretle
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0) ,2)

    #esc basinca cik
    cv2.imshow('Video', frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

video_capture.release()
cv2.destroyAllWindows()