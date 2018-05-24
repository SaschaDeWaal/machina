import BaseState
import time
import random

class DriveState(BaseState):

    def __init__(self):
        super(DriveState, self).__init__()
        self.timer = 2
        self._degreesTurned = 0         # The amount of degrees the robot is turned, from 0 to 360.
                                        # It should be ensured this is relative to the gyroscope input
                                        # e.g. the initial orientation should be equal to 0 degrees.

    def onEnter(self):
        super(DriveState, self).onEnter()
        self.timer = 2

    def onLeave(self):
        super(DriveState, self).onLeave()

    def onUpdate(self, delta):
        super(DriveState, self).onUpdate(delta)
        self.timer -= delta

    """
    Function that takes the supposed directions and speeds for both motors to change.
    A negative number indicates the motor should drive backward
    """
    def MotorBehaviour(self, speedLeft, speedRight):
        self.robotData.motorLeft.setSpeed(speedLeft)
        self.robotData.motorRight.setSpeed(speedRight)


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
    Function that aligns the robot to a given amount of angles.
    This is accomplished by rotating it in the corresponding direction until the robot's alignment is within
    a margin of 6 degrees: 3 below and 3 above the supposed alignment.
    The turning speed is modified by the arousal level.
    """
    def TurnDegrees(self, futureDegreesTurned):
        if futureDegreesTurned-3 <= self._degreesTurned <= futureDegreesTurned+3:
            self.MotorBehaviour(0, 0)
        elif futureDegreesTurned < self._degreesTurned:
            self.MotorBehaviour(-1000 - 1800 * self.robotData.arousal , 1000 + 1800 * self.robotData.arousal)
            while futureDegreesTurned < self._degreesTurned:
                if futureDegreesTurned-3 <= self._degreesTurned <= futureDegreesTurned+3:
                    self.MotorBehaviour(0, 0)
        elif futureDegreesTurned > self._degreesTurned:
            self.MotorBehaviour(1000 + 1800 * self.robotData.arousal, -1000 - 1800 * self.robotData.arousal)
            while futureDegreesTurned > self._degreesTurned:
                if futureDegreesTurned-3 <= self._degreesTurned <= futureDegreesTurned+3:
                    self.MotorBehaviour(0, 0)


    """
    Drives both motors forward for a given time
    This is done by checking the time at which this function is supposed to stop
    (given by stoptime, which is supposed to be the time at which the function was initiated, to which the amount of
    seconds is added for how long the robot should drive forward) against the current time.

    Returns false if this time has not yet passed, and true otherwise.
    """
    def TimeDriveForward(self, stoptime):
        if stoptime < time.time():
            self.MotorBehaviour(0, 0)
        elif stoptime > time.time():
            self.MotorBehaviour(1000 + 1800 * self.robotData.arousal, 1000 + 1800 * self.robotData.arousal)
            while stoptime > time.time():
                if stoptime < time.time():
                    self.MotorBehaviour(0, 0)

    """
    Drives both motors backward for a given time
    Same as above, but in opposite direction
    """
    def TimeDriveBackward(self, stoptime):
        if stoptime < time.time():
            self.MotorBehaviour(0, 0)
        elif stoptime > time.time():
            self.MotorBehaviour(-1000 - 1800 * self.robotData.arousal, -1000 - 1800 * self.robotData.arousal)
            while stoptime > time.time():
                if stoptime < time.time():
                    self.MotorBehaviour(0, 0)