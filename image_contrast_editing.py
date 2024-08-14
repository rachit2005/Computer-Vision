import cv2
import numpy as np

def empty(hue):
    pass


'''Creating a TrackBar'''

cv2.namedWindow('TrackBar')
cv2.resizeWindow("TrackBar" , 640 , 240)
cv2.createTrackbar("Hue Min","TrackBar" , 0 , 179 , empty )
cv2.createTrackbar("Hue Max","TrackBar" , 179 , 179 , empty )
cv2.createTrackbar("Sat Min","TrackBar" , 0 , 255 , empty )
cv2.createTrackbar("Sat Max","TrackBar" , 255 , 255 , empty )
cv2.createTrackbar("Val Min","TrackBar" , 0 , 255 , empty )
cv2.createTrackbar("Val Max","TrackBar" , 255 , 255 , empty )


while True:

    img = cv2.imread('CC.jpg')
    img = cv2.resize(img , (700,700))
    imgHSV = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)

    hue_min = cv2.getTrackbarPos("Hue Min" , "TrackBar")
    hue_max = cv2.getTrackbarPos("Hue Max" , "TrackBar")
    Sat_min = cv2.getTrackbarPos("Sat Min" , "TrackBar")
    Sat_max = cv2.getTrackbarPos("Sat Max" , "TrackBar")
    Val_min = cv2.getTrackbarPos("Val Min" , "TrackBar")
    Val_max = cv2.getTrackbarPos("Val Max" , "TrackBar")

    lower = np.array([hue_min , Sat_min , Val_min])
    upper = np.array([hue_max , Sat_max , Val_max])

    mask = cv2.inRange(imgHSV , lower , upper)
    '''
    cv2. inRange() function sets all the values that lie within the range to 255 and the rest to 0. The output of this function will be our mask.
    Finally passing this mask in the bitwise_and function mentioned earlier will produce the desired result.
    '''

    og_Img = cv2.bitwise_and(img , img , mask=mask)


    print(f"Hue min {hue_min}| Hue Max {hue_max}| Sat Min {Sat_min} | Sat Max {Sat_max} | val min {Val_min} | val max {Val_max}")

    # cv2.imshow('image' , imgHSV)
    cv2.imshow('og' , og_Img)
    cv2.waitKey(1)

