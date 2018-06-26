import RPi.GPIO as GPIO
import time
import math


class DriveMotor:
    """ This class can control one motor """

    def __init__(self, pinA, pinB):
        print "Init motor connected to pin " + str(pinA) + " and " + str(pinB)

        self.pinA = pinA
        self.pinB = pinB
        self.currentSpeed = 0

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pinA, GPIO.OUT)
        GPIO.setup(pinB, GPIO.OUT)

        self.pwmA = GPIO.PWM(pinA, 100)
        self.pwmB = GPIO.PWM(pinB, 100)

        self.stopMoving()

    #self.stopMoving()


    def stopMoving(self):
        """ Stop moving this motor. This will set the speed of the motor to 0 """

        self.setSpeed(0)


    def setSpeed(self, speed):
        """ Set the motor speed. A negative speed means it will drive backwards,
        a speed of 0 means that it will stop driving """
        print "Set speed to: " + str(speed)
        if speed == 0:
            self.pwmA.start(0)
            self.pwmB.start(0)
        else:
            if speed > 0:
                self.pwmA.start(1)
                self.pwmB.start(0)
            if speed < 0:
                self.pwmA.start(0)
                self.pwmB.start(1)

            self.pwmA.ChangeFrequency(math.fabs(speed * 1000000))
            self.pwmB.ChangeFrequency(math.fabs(speed * 1000000))
            self.currentSpeed = speed
            time.sleep(0.5)
