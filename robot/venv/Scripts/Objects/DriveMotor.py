import RPi.GPIO as GPIO
import time

class DriveMotor:

    def __init__(self, pinA, pinB):
        self.pinA = pinA
        self.pinB = pinB

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pinA, GPIO.OUT)
        GPIO.setup(pinB, GPIO.OUT)

        self.pwmA = GPIO.PWM(pinA, 10000)
        self.pwmB = GPIO.PWM(pinB, 10000)

    def setDirection(self, direction):
        if direction == 1:
            self.pwmA.start(1)
            self.pwmB.start(0)
        elif direction == -1:
            self.pwmA.start(0)
            self.pwmB.start(1)
        else:
            self.pwmA.start(0)
            self.pwmB.start(0)

    def setSpeed(self, speed):
        self.pwmA.ChangeFrequency(speed)
        self.pwmB.ChangeFrequency(speed)
