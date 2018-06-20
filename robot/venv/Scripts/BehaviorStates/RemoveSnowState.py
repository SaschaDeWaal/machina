
import BaseState
import time
from DriveState import DriveState
import random

class RemoveSnowState(DriveState):

    def __init__(self):
        super(RemoveSnowState, self).__init__()
        self.timer = random.randrange(15, 60, 1)
        self.leftRight = 2
        self.stateName = "RemoveSnowState"

    def onEnter(self):
        super(RemoveSnowState, self).onEnter()
        self.timer = random.randrange(15, 60, 1)
        super(RemoveSnowState, self).SetCurFunction(2, "TimeDriveForward", 0)
        super(RemoveSnowState, self).SetCurFunction(1.5, "TimeDriveBackward", 0)
        #super(RemoveSnowState, self).TimeDriveForward()

    def onLeave(self):
        super(RemoveSnowState, self).onLeave()
        BaseState.BaseState.goToState(self, "AttackBaseState")

    def onUpdate(self, delta):
        super(RemoveSnowState, self).onUpdate(delta)
        self.timer -= delta
        if self.timer <= 0:
            self.onLeave()
        else:
            self.lookAround()


    """
    Makes the robot turn on the spot to look around its environment to see whether it can find snow to push
    Robot randomly picks left or right to search for snow in that direction.
    Once snow is found, the robot drives forward for 2 seconds, followed by 2 back, and restarts the process again.
    """
    def lookAround(self):
        gyro = self.robotData.getGyro()
        curOrientation = gyro[2]        # Current orientation expressed in amount of degrees turned from initial orientation
        if self.leftRight == 2:
            self.leftRight = random.randint(0, 1)  # 0 if left, 1 if right
            if self.leftRight == 0:
                self.leftRight = -1
        # Do pole and colour detection here
        baseFound = False
        snowFound = False
        if baseFound:
            super(RemoveSnowState, self).SetCurFunction(10000, "TurnDegrees", 180)
            super(RemoveSnowState, self).SetCurFunction(1, "TimeDriveBackward", 0)
            if self.leftRight == -1:
                self.leftRight = 1
            elif self.leftRight == 1:
                self.leftRight = -1
        if not baseFound:
            if snowFound:
                super(RemoveSnowState, self).SetCurFunction(2, "TimeDriveForward", 0)
                super(RemoveSnowState, self).SetCurFunction(2, "TimeDriveBackward", 0)
                self.leftRight = 2
                #self.DriveState.DriveState.TurnDegrees(5 * self.leftRight)
        if not baseFound and not snowFound:
            super(RemoveSnowState, self).SetCurFunction(10000, "TurnDegrees", 5 * self.leftRight)
