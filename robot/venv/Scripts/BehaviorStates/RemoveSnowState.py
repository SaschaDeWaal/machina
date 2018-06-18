
import BaseState
import time
import DriveState
import random

class RemoveSnowState(DriveState):

    def __init__(self):
        super(RemoveSnowState, self).__init__()
        self.timer = 2

    def onEnter(self):
        super(RemoveSnowState, self).onEnter()
        self.timer = 2
        super(RemoveSnowState, self).TimeDriveForward()

    def onLeave(self):
        super(RemoveSnowState, self).onLeave()

    def onUpdate(self, delta):
        super(RemoveSnowState, self).onUpdate(delta)
        self.timer -= delta


    """
    Makes the robot turn on the spot to look around its environment to see whether it can find snow to push
    """
    def lookAround(self):
        gyro = self.robotData.gyroscope
        curOrientation = gyro[5]        # Current orientation expressed in amount of degrees turned from initial orientation
        if self.leftRight == 2:
            self.leftRight = random.randint(0, 1)  # 0 if left, 1 if right
            if self.leftRight == 0:
                self.leftRight = -1
        # Do pole and colour detection here
        baseFound = False
        if not baseFound:
            self.DriveState.DriveState.TurnDegrees(5 * self.leftRight)
        elif baseFound: # this should include an 'and' where it states there is white (snow) in sight
            self.DriveState.DriveState.TurnDegrees(90 * self.leftRight)
            self.DriveState.DriveState.timer = 1
            self.DriveState.DriveState.TimeDriveForward()
            self.DriveState.DriveState.TurnDegrees(135 * (-1*self.leftRight))
        elif baseFound: # this should include an 'and' where it states there is no white (snow) in sight
            # Drive towards base
            self.DriveState.DriveState.TimeDriveForward(2)
            self.leftRight = 2
            self.onLeave()