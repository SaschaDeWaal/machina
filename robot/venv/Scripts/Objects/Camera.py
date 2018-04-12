import picamera

class Camera:

    def __init__(self):
        camera = picamera.PiCamera()
        camera.capture('/home/pi/image.jpg')
        print "camera test"