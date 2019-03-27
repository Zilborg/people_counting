"""Access IP Camera in Python OpenCV"""

# nc -vvn 192.168.142.1 7878
# {"msg_id":257,"token":?,"param":0}
# {"msg_id":259,"token":?,"param":"none_force"}
# rtsp://192.168.42.1/live

import cv2

stream = cv2.VideoCapture('rtsp://192.168.42.1:554/live')

# Use the next line if your camera has a username and password
# stream = cv2.VideoCapture('protocol://username:password@IP:port/1')  

while True:

    r, f = stream.read()
    cv2.imshow('IP Camera stream',f)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()