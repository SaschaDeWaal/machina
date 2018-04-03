from DriveMotor import DriveMotor
import InternalBehaviour
import time
import Sensor

"""

File/class that's supposed to be used to the apparent behaviour of the robot.
This includes things such as doing a victory dance, the specifics of which are dependant on the parameters
found in InternalBehaviour.

"""

class ExternalBehaviour:


    def __init__(self, motorLeft, motorRight):
        self._motorLeft = motorLeft
        self._motorRight = motorRight
        #_motorA.setDirection(1)
        InternalBehaviour._funFrust = 5 #test

    """
    Function that takes the supposed directions and speeds for both motors to change.
    -1: backward motion, 0 no motion, 1 forward motion
    """
    def MotorBehaviour(self, directionLeft, directionRight, speedLeft, speedRight):
        DriveMotor.setDirection(self._motorLeft, directionLeft)
        DriveMotor.setDirection(self._motorRight, directionRight)
        DriveMotor.setSpeed(self._motorLeft, speedLeft)
        DriveMotor.setSpeed(self._motorRight, speedRight)
