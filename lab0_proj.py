import numpy as np
import cv2


start='true'
cap = cv2.Videocapture(0)


while(true):
	ret,frame=cap.read()
	if ret==true:
		gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		if start=='true':
			start='false'
			current=gray

		a=current[:,0,0].size
		b=current[0,:,0].size

		x=np.arange(0,a,1)
		y=np.arange(0,b,1)

		delay=zeros[a,b]
		for i1 in x:
			for i1 in y:
				if current[i1,i2]<gray[i1,i2]:
					current[i1,i2]+=1;
				if frame[i1,i2,2]>180 and farme[i1,i2,1]<50 and frame[i1,i2,0]<50:
					current[i1,i2]=0;
		cv2.imshow('frame',current)
		if cv2.waitkey(1) & 0xFF ==ord('q'):
			break
	else: 
		break
cap.release()
cv2.destroyAllWindows