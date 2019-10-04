import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    
    
    # Display the resulting frame
    #x=np.size(gray[:,0])
    #y=np.size(gray[0,:])
    #flip=255*np.ones(x,y)-gray
    x,y,z=frame.shape
    full=np.ones((x,y),dtype=np.uint8)*255
    inv=np.zeros((x,y,3),dtype=np.uint8)
    #inv=np.ones((x,y),dtype=np.uint8)*255-gray
    inv[:,:,0]=full-frame[:,:,0]
    inv[:,:,1]=full-frame[:,:,1]
    inv[:,:,2]=full-frame[:,:,2]
    cv2.imshow('frame',inv)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
