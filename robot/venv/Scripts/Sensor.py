#import picam
import cv2
import time

"""

This file is meant to take care of, and store, the output given by the sensors of the robot.
This is for easier storage and usage by other files.

"""


def main():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if frame != None:
            cv2.imshow("test", frame)

        #if not ret:
            #break
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


if __name__ == '__main__':
    main()