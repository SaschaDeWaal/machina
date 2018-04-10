#import picam
import cv2
import time
from PIL import ImageGrab
import numpy as np

"""

This file is meant to take care of, and store, the output given by the sensors of the robot.
This is for easier storage and usage by other files.

"""

class Sensor:

    def main(self):
        print("hi")
        self.func2()
        self.func3()


    def func1(self):
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("test")

        img_counter = 0

        while True:
            ret, frame = cam.read()
            if frame != None:
                cv2.imshow("test", frame)

                # if not ret:
                # break
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
            ret, frame = cap.read()
            cv2.imshow('WindowName', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                break

    def func3(self):
        while (True):
            printscreen_pil = ImageGrab.grab()
            printscreen_numpy = np.array(printscreen_pil.getdata(), dtype='uint8') \
                .reshape((printscreen_pil.size[1], printscreen_pil.size[0], 3))
            cv2.imshow('window', printscreen_numpy)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break