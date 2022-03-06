# IMPORTING THE OPENCV LIBRARY
import cv2 as cv

# IMAGES---------------------------------------------------------------

# READING AN IMAGE FROM SPECIFIED PATH
img = cv.imread('Resources/Photos/cat.jpg')

# DISPLAYING AN IMAGE AS A NEW WINDOW. INPUT NEEDED IS THE NAME AND MATRIX OF PIXELS
cv.imshow('Cat', img)

# THIS LINE WILL DISPLAY THE WINDOW INFINITELY UNTIL ANY KEYBOARD IS PRESSED
cv.waitKey(0)


# VIDEOS ---------------------------------------------------------------

# CREATING A VIDEOCAPTURE OBJECT TO READ A VIDEO FROM A SPECIFIED PATH (INPUT 0 WILL CAPTURE VIDEOS FROM WEBCAM)
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

# USING A WHILE LOOP TO READ THE VIDEO FRAME BY FRAME
while True:
    isTrue, frame = capture.read()
    # DISPLAYING THE VIDEO FRAME BY FRAME
    cv.imshow('Video', frame)
    # STOPPING THE VIDEO FROM PLAYING INDEFINITELY
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

# CLOSING THE VIDEO WINDOW
capture.release()
cv.destroyAllWindows()

