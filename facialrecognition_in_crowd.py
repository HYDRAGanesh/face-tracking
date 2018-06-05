#
#https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/
#http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html
#
# Includes both the eye and face classifiers.
#
# Only finds out if the face and eyes are present in the page.
# Does not detect the faces yet !
#

import cv2
cam = cv2.VideoCapture('TimesSquare.mp4')
face_detector=cv2.CascadeClassifier('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml')
if (face_detector.empty() ) :
	print ("The face classifier is empty, Breaking out ")
	quit()

eye_detector=cv2.CascadeClassifier('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cv2/data/haarcascade_eye.xml')

if (eye_detector.empty() ) :
	print ("The eye classifier is empty ")
	quit()
#else :
#	print ("the eye classifier is good")

print ("After the facial recognition");

while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        roi_gray  = gray[y:y+h, x:x+w]
        roi_color = img [y:y+h, x:x+w]

        eyes = eye_detector.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        cv2.imshow('frame',img)

	#Press Q on keyboard to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
           break

cam.release()
cv2.destroyAllWindows()
