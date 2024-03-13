import cv2

outputdir='output/'
cap = cv2.VideoCapture('http://192.168.56.1:56000/mjpeg')
# http://192.168.1.131:56000/

id=0

while True:
    status, photo = cap.read()
    
    if(id % 40 == 0):
        cv2.imwrite(outputdir+'camera'+str(id)+'.jpg', photo)
    id+=1

    # Press Enter to exit
    if cv2.waitKey(10) == 13:
        break

cv2.destroyAllWindows()