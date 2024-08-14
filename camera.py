'''Using webcam --> the video is flipped''' 

# import the opencv library 
import cv2 
import numpy as np

# define a video capture object 
cap = cv2.VideoCapture(0) 
print('To start webcam : 1 \nTo record: 2 \nTo play video:3 \nTo Select region of interest: 4\nTo split image into channels: 5\nTo merge channels: 6 ')
inp = input("what do you want to do: ")
img_for_all = cv2.imread('C.jpg')
img_for_all = cv2.resize(img_for_all , (500,500))


if inp == "1":
    print("press q to quit")
    while True: 
        
        # Capture the capeo frame 
        # by frame 
        ret, frame = cap.read() 
        frame = cv2.Canny(frame , 100,100)

        # Display the resulting frame 
        cv2.imshow('frame', frame) 
        
        # the 'q' button is set as the quitting button you may use any desired button of your choice 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

    # After the loop release the cap object 
    cap.release() 
    # Destroy all the windows 
    cv2.destroyAllWindows() 

else:
    pass

'''Capture video Using Webcam'''
if inp == "2":

    name = input('save as: ')
    filename = name + '.MP4'
    if cap.isOpened() == False:
        print('give permision first naaaa! , idiot')


    # setting the resolution
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    #video codec --> is a hardware or software algorithm that compresses and decompresses digital video. 
    video_codec = cv2.VideoWriter_fourcc(*'XVID')

    # the video writer that write binary for image on a continuous flow
    vid_output = cv2.VideoWriter(filename , video_codec , 30 ,(frame_width , frame_height)) # -->argument order:(Filename, Fourcc_code, FrameRate, FrameSize)


    # starting the loop 
    while True:
        ret , frame = cap.read()

        if ret == True:
            vid_output.write(frame) # adding the frames continuously
            cv2.imshow('hai kuch' , frame)
    
        # setting the q key as quit button
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    vid_output.release()
    cv2.destroyAllWindows()
    print(f'video saved succesfully as {filename}')

'''Playing a video from file'''
if inp == '3':

    file_to_play = input('filename to play with extension: ')
    play = cv2.VideoCapture(file_to_play)

    while True:
        ret , frame = play.read()
        cv2.imshow('kuch to hua hai' , frame)

        if cv2.waitKey(24) & 0xFF == ord('q'):
            break
            
    play.release()
    cv2.destroyAllWindows()

'''Basic operation on images'''
if inp == '4':

    # Setting Region of image
    img = cv2.imread("E://from phone//1.jpg")
    img = cv2.resize(img , (500,500))

    roi = cv2.selectROI(img) # ROI stands for Region Of Interest
    print(roi) # gives an array of []

    # Crop image--> image[ start_row : end_row, start_col : end_col] this what is going on below and printing above
    cropped_image = img[int(roi[1]):int(roi[1]+roi[3]),  
                        int(roi[0]):int(roi[0]+roi[2])] 


    cv2.imshow('h' , cropped_image)
    cv2.imwrite('cropped_image.jpg' , cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

'''Splitting image'''
if inp == '5':

    img = cv2.imread("E://from phone//5.jpg")
    # Using cv2.split() to split channels of coloured image  
    b,g,r = cv2.split(img)

    cv2.imshow('blue part of image',b)
    cv2.imshow('green part of image', g)
    cv2.imshow('red part of image' , r)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

'''Merging Image'''
if inp == '6':

    img = cv2.imread("E://from phone//5.jpg")
    # Using cv2.split() to split channels of coloured image  
    b,g,r = cv2.split(img)


    # Using cv2.merge() to merge channnels
    merged_img = cv2.merge((g , b,r))

    merged_img = cv2.resize(merged_img , (500,500))
    cv2.imshow('merged image' ,merged_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

'''Blend two different images'''

if inp == '7':
    
    i1 = cv2.imread('cropped_image.jpg')
    i1 = cv2.resize(i1 , (500,500))
    i2 = cv2.imread('ocr image.jpg')
    i2 = cv2.resize(i2 , (500,500))


    # make sure that both images have same size (you can do that by resizing)
    blended_image = cv2.addWeighted(src1= i1 ,  #scr1 is the base image ,
                    alpha=1, # % percentage(value from 0 to 1) of base image to show
                    src2 = i2, # second image
                    beta=0.5, # % percentage (value from 0 to 1) of second image to show
                    gamma= 3)# darkness/sharpness of final image
    cv2.imshow('blended image' , blended_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


'''applying filter in on images'''

if inp == '8':
    img = cv2.imread('C.jpg')
    img = cv2.resize(img , (500,500))
    
    # see the image in this website --> https://www.geeksforgeeks.org/python-opencv-filter2d-function/
    # Creating the kernel(2d convolution matrix)
    k_shaped = np.array([[0,-1,0],
                         [-1 ,5, 1],
                         [0,-1,0]])
    
    contour = np.array([[-1,-1,-1],
                        [-1,8,-1],
                        [-1,-1,-1]])

    filtered_image = cv2.filter2D(img,-1 , contour)
    cv2.imshow('filltered' , filtered_image)
    cv2.imwrite('contoured image.jpg' , filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

'''Thresholding of image'''
if inp == '9':

    # for threshold -->  https://www.geeksforgeeks.org/python-thresholding-techniques-using-opencv-set-1-simple-thresholding/
    ret , THRESH_BINARY = cv2.threshold(img_for_all , 127 ,255 , cv2.THRESH_BINARY)
    ret , THRESH_BINARY_INV= cv2.threshold(img_for_all , 127 ,255 , cv2.THRESH_BINARY_INV)
    ret , THRESH_TOZERO= cv2.threshold(img_for_all , 127 ,255 , cv2.THRESH_TOZERO)
    ret , THRESH_TOZERO_INV= cv2.threshold(img_for_all , 127 ,255 , cv2.THRESH_TOZERO_INV)
    ret , THRESH_TRUNC= cv2.threshold(img_for_all , 127 ,255 , cv2.THRESH_TRUNC)

    # canny image 
    canny_image = cv2.Canny(img_for_all , 50,100)

    cv2.imshow('THRESH_BINARY' , THRESH_BINARY)
    cv2.imshow('THRESH_BINARY_INV' , THRESH_BINARY_INV)
    cv2.imshow('THRESH_TOZERO' , THRESH_TOZERO)
    cv2.imshow('THRESH_TOZERO_INV' , THRESH_TOZERO_INV)
    cv2.imshow('THRESH_TRUNC' , THRESH_TRUNC)
    cv2.imshow('CANNY IMAGE' , canny_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

