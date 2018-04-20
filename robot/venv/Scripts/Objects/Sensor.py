#import picam
import cv2
import os
import time
import numpy as np
import time
import msvcrt

"""

This file is meant to take care of, and store, the output given by the sensors of the robot.
This is for easier storage and usage by other files.

"""

class Sensor:
    def __init__(self):
        print"hi"
        self.extractCameraFrames()
        # self.func1()
        #self.func2()
        #self.func3()


    def func1(self):
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("test")

        img_counter = 0

        while True:
            ret, frame = cam.read()
            if frame != None:
                cv2.imshow("test", frame)

                if not ret:
                    break
            k = cv2.waitKey(1)

            if k % 256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k % 256 == 32:
                # SPACE pressed
                img_name = "opencv_frame_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1

        cam.release()

        cv2.destroyAllWindows()


    def func2(self):
        cap = cv2.VideoCapture(0)
        while (cap.isOpened()):
            ret, frame = cap.read
            cv2.imshow('WindowName', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                break

    """
    def func3(self):
        while (True):
            printscreen_pil = ImageGrab.grab()
            printscreen_numpy = np.array(printscreen_pil.getdata(), dtype='uint8') \
                .reshape((printscreen_pil.size[1], printscreen_pil.size[0], 3))
            cv2.imshow('window', printscreen_numpy)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
    """

    """" Function to extract frames from the camera"""
    def extractCameraFrames(self):
        cap = cv2.VideoCapture(0)
        count = 0
        while True:
            ret, img = cap.read()
            if ret == True:
                count += 1
                # Used to set fps, Set 50 for 20, 100 for 10, 33 for 30
                cv2.waitKey(100)
                cv2.imshow('Webcam', img)
                # File path to save the frames
                img_path = "C:\\Users\\Ishdeep Bhandari\\Desktop\\Frames_Cam"
                # Resizing to desired size for the frame
                resized_img = cv2.resize(img,(128,128))
                cv2.imwrite(os.path.join(img_path,'Frame %d.jpg' % count), resized_img)
                # To exit just stop the code
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    derp = Sensor()