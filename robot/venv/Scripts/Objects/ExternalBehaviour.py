from DriveMotor import DriveMotor
import InternalBehaviour
import time
import random

"""

File/class that's supposed to be used to the apparent behaviour of the robot.
This includes things such as doing a victory dance, the specifics of which are dependant on the parameters
found in InternalBehaviour.

"""

class ExternalBehaviour:


    def __init__(self, motorLeft, motorRight):
        self._motorLeft = motorLeft
        self._motorRight = motorRight
        self._degreesTurned = 0         # The amount of degrees the robot is turned, from 0 to 360.
                                        # It should be ensured this is relative to the gyroscope input
                                        # e.g. 'north' should be equal to 0 degrees.
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
    Performs either move forward for a random amount of seconds between 1 and 3, backward, or turns to a
    random alignment, all with a chance of 1 in 3.
    """
    def RandomMove(self):
        randNum = random.randint(0, 2)
        curTime = time.time()
        duration = random.randrange(1, 3, 0.25)
        stopTime = curTime + duration
        if randNum == 0:
            self.TimeDriveForward(stopTime)
        elif randNum == 1:
            self.TimeDriveBackward(stopTime)
        elif randNum == 2:
            degreesToTurnTo = random.randrange(0, 359, 1)
            self.TurnDegrees(degreesToTurnTo)

    """
    Drives both motors forward for a given time
    This is done by checking the time at which this function is supposed to stop
    (given by stoptime, which is supposed to be the time at which the function was initiated, to which the amount of
    seconds is added for how long the robot should drive forward) against the current time.

    Returns false if this time has not yet passed, and true otherwise.
    """
    def TimeDriveForward(self, stoptime):
        #stoptime = timeStarted + datetime.timedelta(seconds=duration)
        #if stoptime < datetime.datetime.now():
        if stoptime < time.time():
            self.MotorBehaviour(0, 0, 0, 0)
        #elif stoptime > datetime.datetime.now():
        elif stoptime > time.time():
            self.MotorBehaviour(1, 1, 1000, 1000)
            #while stoptime > datetime.datetime.now():
            while stoptime > time.time():
                #if stoptime < datetime.datetime.now():
                if stoptime < time.time():
                    self.MotorBehaviour(0, 0, 0, 0)

    """
    Drives both motors backward for a given time
    Same as above, but in opposite direction
    """
    def TimeDriveBackward(self, stoptime):
        # stoptime = timeStarted + datetime.timedelta(seconds=duration)
        #if stoptime < datetime.datetime.now():
        if stoptime < time.time():
            self.MotorBehaviour(0, 0, 0, 0)
        #elif stoptime > datetime.datetime.now():
        elif stoptime > time.time():
            self.MotorBehaviour(-1, -1, 1000, 1000)
            # while stoptime > datetime.datetime.now():
            while stoptime > time.time():
                # if stoptime < datetime.datetime.now():
                if stoptime < time.time():
                    self.MotorBehaviour(0, 0, 0, 0)

    """
    Function that aligns the robot to a given amount of angles.
    This is accomplished by rotating it in the corresponding direction until the robot's alignment is within
    a margin of 6 degrees: 3 below and 3 above the supposed alignment.
    """
    def TurnDegrees(self, futureDegreesTurned):
        if futureDegreesTurned-3 <= self._degreesTurned <= futureDegreesTurned+3:
            self.MotorBehaviour(0, 0, 0, 0)
        elif futureDegreesTurned < self._degreesTurned:
            self.MotorBehaviour(-1, 1, 100, 100)
            while futureDegreesTurned < self._degreesTurned:
                if futureDegreesTurned-3 <= self._degreesTurned <= futureDegreesTurned+3:
                    self.MotorBehaviour(0, 0, 0, 0)
        elif futureDegreesTurned > self._degreesTurned:
            self.MotorBehaviour(1, -1, 100, 100)
            while futureDegreesTurned > self._degreesTurned:
                if futureDegreesTurned-3 <= self._degreesTurned <= futureDegreesTurned+3:
                    self.MotorBehaviour(0, 0, 0, 0)
