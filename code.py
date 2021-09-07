import cv2

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)
#instead of 0 we can also pass 1 for secondary cam if available,0 is for primary cam.

while True:
    ret,frame = cam.read()
    
    if ret == False:
        continue
        
    all_faces = detector.detectMultiScale(frame,1.5,5)
    
    for face in all_faces:
        x,y,w,h = face
        #to put a rectangle frame on the face:-
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    
    cv2.imshow("Face Detection",frame)
    
    #finding which key you have pressed:-
    key_pressed=cv2.waitKey(1) & 0xFF
    #if user has pressed 'q',it will exit:-
    if key_pressed==ord('q'):
        break
        
cam.release()
cv2.destroyAllWindows()
