import numpy as np
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(2)

while(True):
    
   

    red = (0, 0, 255) #8
    cv2.line(frame, (300, 0), (0, 300), red, 3)
    line=cv2.line(frame,(0,0),(511,511),(0,255,0),50) 
    ret, frame = cap.read()
    gray = cv2.cvtColor(Vshow,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",gray)
    cv2.imshow('2frame',frame)
   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

