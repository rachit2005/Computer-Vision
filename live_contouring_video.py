import cv2
import numpy as np

def getContours(img):
    # try different modes and methods 
    # what is contours --> the shape of the outer surface of something
    contours , hierarchy = cv2.findContours(img , cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE )
    for cnt in contours:
        area = cv2.contourArea(cnt) # finds area of the contour
        # print(f"area of curves {area}")
        cv2.drawContours(img_cont , cnt , -1 , [0,0,0] , 3 , cv2.LINE_AA)
        
        perimeter = cv2.arcLength(cnt , True)
        # print(f"perimeter of curves {perimeter}")

        '''Approx the contour shape'''
        
        # approximates a contour shape to another shape with less number of vertices. It accepts the following arguments 
        # cnt: The array of the contour points. epsilon: Maximum distance from contour to approximated contour.
        approx = cv2.approxPolyDP(cnt , 0.02*perimeter , True)
        obj_corner = len(approx)

        x,y,w,h = cv2.boundingRect(approx)

        if obj_corner == 3: ObjectType = "Triangle"
        elif obj_corner == 4: ObjectType = "quadrilateral"
        elif obj_corner == 2: ObjectType = "what !!"
        else: ObjectType = "None"

        cv2.rectangle(img_cont , (x,y) , (x+w,y+h) , (0,255,0) , 3 , 1)
        cv2.putText(img_cont , ObjectType , (x+(w//2)-100 , y+(h//2)-10) , cv2.FONT_HERSHEY_SIMPLEX , 1 , (0,0,0) , 2 , -1 )



img = cv2.imread('GG.jpg')
img_cont = img.copy()
gray_img = cv2.cvtColor(img , cv2.COLOR_BGRA2GRAY)
img_blur = cv2.GaussianBlur(gray_img , (7,7) , 1)

'''Finding Edges'''
img_canny = cv2.Canny(img_blur , 100 , 100)
getContours(img_canny)

# cv2.imshow('image' , img_cont)

print("Press 'q' to quit")

cap = cv2.VideoCapture(0)

while True:
    success , image = cap.read()
    image_gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
    img_canny2 = cv2.Canny(image_gray , 100,100)
    # getContours(img_canny2)

    cv2.imshow('live' , img_canny2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

# cv2.waitKey(0)
cv2.destroyAllWindows()