import cv2
import numpy as np
from caliberation import Caliberation,Transform

vc=cv2.VideoCapture(0)

#step 1: Capture background image
print('Press any key once suitable background has been obtained: ')
while cv2.waitKey(1)==-1:
	return_value,frame=vc.read()
	frame=cv2.flip(frame,1)
	frame=cv2.resize(frame,(1280,720))
	cv2.imshow('frame',frame)
cv2.imwrite('background.png',frame)
cv2.destroyAllWindows()
print('\n\n\t\tBackground Image has been saved successfully !!!')
#step 2: HSV Color Range for Cloak
c=input("Press Enter to start Caliberation: ")
Lower,Upper=Caliberation()
print(Lower,Upper)

#step 3: Real time application
c=input('Press enter to start Magic :) ')
vc.release()
background=cv2.imread('background.png')
vc=cv2.VideoCapture(0)
while cv2.waitKey(1)==-1:
	return_value,frame=vc.read()
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
