# importing the library 

import cv2

# `haarcascade_russian_plate_number` is a file that contains the cascade classifier data for detecting Russian license plate
# numbers using the Haar feature-based cascade classifiers. Haar cascades are a popular method for object detection in computer vision.
# They work by analyzing regions of an image for certain features that match a predefined pattern. 

# In this case, the `haarcascade_russian_plate_number` file would contain data trained specifically to recognize 
# the patterns typically found in Russian license plates. This classifier could be used in various applications such as automatic
# license plate recognition systems, vehicle tracking, or security systems.

harcascade = "model/haarcascade_russian_plate_number.xml"

# cv2 is the OpenCV library.
# VideoCapture(0) creates a video capture object that captures video from the first camera device found on your system.
# If you have multiple cameras, you can specify a different index to select a different camera.
# cap is a variable that now holds this video capture object, allowing you to access frames from the video stream.

cap = cv2.VideoCapture(0)

# cap.set(2, 640) sets the width of the captured video stream to 640 pixels. The argument 2 corresponds to the property identifier for width.

cap.set( 2, 640)  # Width

# cap.set(4, 480) sets the height of the captured video stream to 480 pixels. The argument 4 corresponds to the property identifier for height.
cap.set( 4, 480)  # Height

# min_area = 500: This variable min_area is assigned the value 500, which likely represents the minimum area threshold for some object detection or tracking algorithm. 
# This threshold could be used, for example, to filter out small contours or regions of interest detected in an image or video frame.

# count = 0: This variable count is initialized to 0. It might be intended to keep track of some kind of count,
# such as the number of objects detected or some other relevant metric in the application. Depending on the context, 
# it could be updated later in the code as the application runs.

min_area = 500
count = 0

# initializing the while loop is equal to 'true'
while True:

    # success: This variable typically holds a boolean value (True or False) indicating whether the frame was successfully read from the video stream. 
    # If True, it means that a frame was read successfully; otherwise, it means that there might have been an issue in reading the frame.
    # img: This variable holds the actual image data of the frame that was read. It's usually represented as a NumPy array (assuming OpenCV is being used), 
    # allowing you to perform various image processing operations on it.

    success, img = cap.read()


    # The line plate_cascade = cv2.CascadeClassifier(harcascade) is attempting to create a cascade classifier object named plate_cascade using the file
    #  specified by the variable harcascade. Typically, harcascade would contain the file path to the cascade classifier XML file that defines the features used to detect license
    # plates.
    # However, in your previous message, you mentioned haarcascade_russian_plate_number. So, if harcascade is indeed holding the path to this XML file, 
    # then plate_cascade will be a cascade classifier object specifically trained for detecting Russian license plates.
    # After initializing the cascade classifier, you can use it to detect license plates in images or video frames by applying the detectMultiScale method to the image data.
    
    plate_cascade = cv2.CascadeClassifier(harcascade)

    # cv2.cvtColor: This function is used to convert the color space of an image.
    # img: This is the input image, typically in BGR (blue-green-red) color format.
    # cv2.COLOR_BGR2GRAY: This parameter specifies the conversion from BGR color space to grayscale. It's one of the color conversion codes provided by OpenCV.

    img_gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY)

    # img_gray: This is the grayscale image in which you want to detect license plates.
    # 1.1: This parameter represents the scale factor. It specifies how much the image size is reduced at each image scale.
    # In this case, it's set to 1.1, meaning the image is resized by reducing its size by 10% each time to detect objects of different sizes in the image.
    # 4: This parameter represents the minimum number of neighbor rectangles that need to be detected for an object to be considered valid. In this case,
    # it's set to 4, meaning an object needs to be detected at least four times to be considered a valid detection.

    plates = plate_cascade.detectMultiScale( img_gray, 1.1, 4)

    # initializing the for loop with variables x,y,w,h
    # w = width
    # h = height

    for (x,y,w,h) in plates:

        # calculating the area of screen we want to display
        area = w * h

        # this is to check that the showing image or video has the number plate or not if it has then the camera capture the
        # number plate.
        if area > min_area:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText( img, "Number Plate", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, ( 255, 0, 255), 2)
            img_reason_of_intrest = img[y: y+h, x: x+w]
            cv2.imshow("Reason of Intrest", img_reason_of_intrest)


    # show the image captured by the camera
    cv2.imshow("Result", img) 

    # here we are assigning the s for saving the image of number plate
    # and e for exiting the if statement and closing the camera.
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("Number_plates/scanned_img_" + str(count) + ".jpg", img_reason_of_intrest)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
        cv2.imshow("Results", img)
        cv2.waitKey(500)
        count += 1
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break
