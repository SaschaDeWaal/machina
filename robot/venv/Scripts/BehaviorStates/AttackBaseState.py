
import BaseState
import random
import time

class AttackBaseState(BaseState):

    def __init__(self):
        super(AttackBaseState, self).__init__()
        self.timer = 2
        self.leftRight = 2


    def onEnter(self):
        super(AttackBaseState, self).onEnter()
        self.timer = 2
        self.lookAround()

    def onLeave(self):
        super(AttackBaseState, self).onLeave()
        self.DriveState.DriveState.TimeDriveForward(3)
        # Go to wandering behaviour

    def onUpdate(self, delta):
        super(AttackBaseState, self).onUpdate(delta)
        self.timer -= delta
        if self.leftRight != 2:
            self.lookAround()
        else:
            if self.robotData.motorLeft.speed == 0 and self.robotData.motorRight.speed == 0:
                self.DriveState.DriveState.TimeDriveForward(2)

    """
    Makes the robot turn on the spot to look around its environment to see whether it can see the base of an opposing team.
    """
    def lookAround(self):
        gyro = self.robotData.gyroscope
        curOrientation = gyro[5]        # Current orientation expressed in amount of degrees turned from initial orientation
        if self.leftRight == 2:
            self.leftRight = random.randint(0, 1)  # 0 if left, 1 if right
            if self.leftRight == 0:
                self.leftRight = -1
        # Do pole and colour detection here; note: look for a base of a different colour
        baseFound = False
        if not baseFound: 
            self.DriveState.DriveState.TurnDegrees(5 * self.leftRight)
        elif baseFound: # this should include an 'and' where it states there is no white (snow) in sight
            # Drive either to the left or right (depends on leftRight), and turn back the same amount of degrees afterward
            self.DriveState.DriveState.TurnDegrees(90 * self.leftRight)
            self.DriveState.DriveState.TimeDriveForward(1)
            self.DriveState.DriveState.TurnDegrees(135 * (-1*self.leftRight))
        elif baseFound: # this should include an 'and' where it states there is white (snow) in sight
            self.DriveState.DriveState.TimeDriveForward(2)
            self.leftRight = 2
            return