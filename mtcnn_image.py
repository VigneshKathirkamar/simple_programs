# This program shows a quick inference using MTCCN architecture

import cv2
from mtcnn.mtcnn import MTCNN

detector = MTCNN()

confidence = 0.7

image = cv2.imread('/home/space_monkey/virtual_environments/tf_expts/ext_data/download.jpeg')
rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
faces = detector.detect_faces(rgb_image)

for face in faces:
    if face['confidence']>=confidence:
        x,y,w,h = face['box']
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.circle(image,(face['keypoints']['nose']),4,(0,0,255),-1)
        

cv2.imshow('detection',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
