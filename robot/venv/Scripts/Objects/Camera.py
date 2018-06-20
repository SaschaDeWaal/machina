from picamera import PiCamera
from picamera.array import PiRGBArray
from threading import Thread

class Camera:

    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (320, 240)
        self.camera.framerate = 30
        self.rawCapture = PiRGBArray(self.camera, size=(320, 240))

        self.tracking = True

        self.thread = Thread(target=self.trackingLoop, args=())
        self.thread.start()
        #camera.capture('/home/pi/image.jpg')

    def trackingLoop(self):
        #while self.tracking:
        self.camera.capture('/home/pi/cameraObject.jpg')
        print "photo taken";


    def stop(self):
        self.tracking = False
