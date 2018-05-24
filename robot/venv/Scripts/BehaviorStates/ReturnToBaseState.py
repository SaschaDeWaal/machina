
import BaseState
import DriveState
import time
import random

class ReturnToBaseState(BaseState):

    def __init__(self):
        super(ReturnToBaseState, self).__init__()
        self.timer = 2
        self.leftRight = 2

    def onEnter(self):
        super(ReturnToBaseState, self).onEnter()
        self.timer = 2
        self.lookAround()

    def onLeave(self):
        super(ReturnToBaseState, self).onLeave()

    def onUpdate(self, delta):
        super(ReturnToBaseState, self).onUpdate(delta)
        self.timer -= delta
        if self.leftRight != 2:
            self.lookAround()


    """
    Makes the robot turn on the spot to look around its environment to see whether it can see its own base.
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
        else:
            # Drive towards base
            self.leftRight = 2
            return
