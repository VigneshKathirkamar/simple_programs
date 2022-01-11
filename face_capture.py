import cv2
import os
from mtcnn.mtcnn import MTCNN

detector=MTCNN()

video = cv2.VideoCapture(0)

height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
confidence = 0.7
test = cv2.VideoWriter('/home/vignesh/test.avi',cv2.VideoWriter_fourcc(*'MJPG'),30,(width,height))
while video.isOpened():
    ret,frame = video.read()
    if ret == True:
        rgb_image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        faces = detector.detect_faces(rgb_image)
        
        for face in faces:
            
            if face['confidence'] >= confidence:
                #x,y,w,h = face['box']
                #test = cv2.VideoWriter('/home/vignesh/test.avi',cv2.VideoWriter_fourcc(*'MJPG'),30,(width,height))
                cv2.putText(frame,"Face \n detected",(x,y),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,255),5)
                test.write(frame)
                print('writing frame..')
                
        cv2.imshow('frame',frame)
    
                
                
    if cv2.waitKey(10)==ord('q'):
        cv2.destroyAllWindows()
        video.release()
        test.release()
        break
