import cv2
import numpy as np
from caliberation import Caliberation,Transform
vc = cv2.VideoCapture(0)
print('Step 1: Press any key on screen once you have a suitable background')
while cv2.waitKey(1)==-1:
		return_value,frame = vc.read()
		frame=cv2.flip(frame,1)
		frame=cv2.resize(frame,(1280,720))
		cv2.imshow('Frame',frame)
cv2.imwrite('background.png',frame)
print('\n\n\t\tBackground image set successfully')
cv2.destroyAllWindows()#To prevent hanging of screen
c=input('\n\n[Press enter to continue]')
print('\n\nStep 2: Caliberating cloak\n')	
Lower,Upper=Caliberation()
print('\n\n\t\tCaliberation successfull')
c=input("\n\n\n\nStep 3: Press Enter to start")
background=cv2.imread('background.png')
vc.release()
cv2.destroyAllWindows()	

vc = cv2.VideoCapture(0)
while cv2.waitKey(1)==-1:
	return_value,frame = vc.read()
	frame=cv2.flip(frame,1)
	frame=cv2.resize(frame,(1280,720))
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	mask=cv2.inRange(hsv,np.array(Lower),np.array(Upper))
	
	mask=Transform(mask)
	
	frame=np.array(frame)
	temp=cv2.bitwise_and(background,background,mask=mask)
	mask=cv2.bitwise_not(mask)
	frame=cv2.bitwise_and(frame,frame,mask=mask)
	frame=cv2.add(frame,temp)
	cv2.imshow('Frame',frame)
vc.release()
cv2.destroyAllWindows()	
