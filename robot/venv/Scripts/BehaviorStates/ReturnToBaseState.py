
import BaseState
import DriveState
import time
import random
from thread import start_new_thread

class ReturnToBaseState(BaseState):

    def __init__(self):
        super(ReturnToBaseState, self).__init__()
        self.timer = 2
        self.leftRight = 2

    def onEnter(self):
        super(ReturnToBaseState, self).onEnter()
        self.timer = 2
        #self.lookAround()
        start_new_thread(self.lookAround, ())

    def onLeave(self):
        super(ReturnToBaseState, self).onLeave()
        super(ReturnToBaseState, self).TimeDriveForward(3)
        # Go to removeSnow

    def onUpdate(self, delta):
        super(ReturnToBaseState, self).onUpdate(delta)
        self.timer -= delta
        #if self.leftRight != 2:
        #    self.lookAround()
        #else:
        #    if self.robotData.motorLeft.speed == 0 and self.robotData.motorRight.speed == 0:
        #        self.DriveState.DriveState.TimeDriveForward(2)

    """
    Makes the robot turn on the spot to look around its environment to see whether it can see its own base
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
            self.DriveState.DriveState.TimeDriveForward(1)
            self.DriveState.DriveState.TurnDegrees(135 * (-1*self.leftRight))
        elif baseFound: # this should include an 'and' where it states there is no white (snow) in sight
            # Drive towards base
            self.DriveState.DriveState.TimeDriveForward(2)
            self.leftRight = 2
            return
