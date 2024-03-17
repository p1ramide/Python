import cv2 
from datetime import datetime 
import numpy as np

def orario(frame):
    font = cv2.FONT_HERSHEY_SIMPLEX
    data = datetime.now()
    tempo = data.strftime('%H:%M:%S')       
    cv2.putText(frame,  
                f'{tempo}',  
                (450, 50),  
                font, 1,  
                (0, -255, 255),  
                2,  
                cv2.LINE_4)     

def registra():
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    return out

def rileva(frame1, frame2, excluded_region):
    diff = cv2.absdiff(frame1, frame2)
    diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(diff_gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(
        dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        
        if (excluded_region[0] < x < excluded_region[0] + excluded_region[2] and
            excluded_region[1] < y < excluded_region[1] + excluded_region[3]):
            continue  
            
        if cv2.contourArea(contour) < 900:
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (255, 0, 0), 2)

def main():
    vid = cv2.VideoCapture(0)
    ret, frame1 = vid.read()
    ret, frame2 = vid.read()

    excluded_region = (450, 10, 640, 60)
    #out = registra()

    while True: 
        ret, frame = vid.read() 
        rileva(frame1, frame2, excluded_region)

        cv2.imshow('Telecamera', frame1)  
        frame1 = frame2
        ret, frame2 = vid.read()

        #out.write(frame1) 
        orario(frame1)

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
        
    vid.release() 
    cv2.destroyAllWindows()

    return frame, frame1, frame2


if __name__ == "__main__":
    main()

