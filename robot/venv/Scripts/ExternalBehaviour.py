from DriveMotor import DriveMotor
import InternalBehaviour
import time
import Sensor
import random
import datetime
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

    """
    Drives both motors forward for a given time
    This is done by checking the time at which this function is supposed to stop
    (given by stoptime, which is supposed to be the time at which the function was initiated, to which the amount of
    seconds is added for how long the robot should drive forward) against the current time.

    Returns false if this time has not yet passed, and true otherwise.
    """
    def TimeDriveForward(self, stoptime):
        #stoptime = timeStarted + datetime.timedelta(seconds=duration)
        if stoptime < datetime.datetime.now():
            self.MotorBehaviour(0, 0, 0, 0)
            return True
        elif stoptime > datetime.datetime.now():
            self.MotorBehaviour(1, 1, 1000, 1000)
            return False

    """
    Drives both motors backward for a given time
    Same as above, but in opposite direction
    """
    def TimeDriveBackward(self, stoptime):
        # stoptime = timeStarted + datetime.timedelta(seconds=duration)
        if stoptime < datetime.datetime.now():
            self.MotorBehaviour(0, 0, 0, 0)
            return True
        elif stoptime > datetime.datetime.now():
            self.MotorBehaviour(-1, -1, 750, 750)
            return False


