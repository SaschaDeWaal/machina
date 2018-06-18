
import BaseState
import time
import DriveState
import random

class ShakenState(DriveState):

    def __init__(self):
        super(ShakenState, self).__init__()
        self.timer = 2
        self.randNum = random.randrange(0, 7, 1)

    def onEnter(self):
        super(ShakenState, self).onEnter()
        self.randNum = random.randrange(0, 7, 1)

    def onLeave(self):
        super(ShakenState, self).onLeave()
        super(ShakenState, self).MotorBehaviour(0,0)

    """
    Update function
    A timer is set between 1 and 4 seconds. This timer determines how long the robot will drive in one of 8 manners
    randNum determines in what configuration the robot will drive around for -timer- amount of seconds.
    shakyMoves is called every frame to modify the speed with the time passed since last frame.
    """
    def onUpdate(self, delta):
        super(ShakenState, self).onUpdate(delta)
        self.timer -= delta
        if self.timer <= 0:
            self.timer = random.randrange(1, 4, 0.5)
            self.randNum = random.randrange(0, 7, 1)
        self.shakyMoves(delta)


    """
    Shaken movement is taken care of here.
    Based on randNum, the robot drives forward, backward, left, or right.
    The speed at which is done so depends on the arousal level, and the amount of time spent driving in the current direction.
    Whatever direction the robot is driving in, it'll either be modified with a bias towards the right or left.
    This causes the robot to speed up in that direction while driving in that direction, resulting in 'drunk' behaviour.
    """
    def shakyMoves(self, delta):
        arMod = 800 * super(ShakenState, self).robotData.arousal   # Modifier to motor power based on robot's arousal
        timeMod = 10000 * delta
        if self.randNum == 0:
            super(ShakenState, self).MotorBehaviour(1000 + arMod, 1000 + arMod + timeMod)
        elif self.randNum == 1:
            super(ShakenState, self).MotorBehaviour(1000 + arMod + timeMod, 1000 + arMod)
        elif self.randNum == 2:
            super(ShakenState, self).MotorBehaviour(1000 + arMod, -1000 - arMod - timeMod)
        elif self.randNum == 3:
            super(ShakenState, self).MotorBehaviour(1000 + arMod + timeMod, -1000 - arMod)
        elif self.randNum == 4:
            super(ShakenState, self).MotorBehaviour(-1000 - arMod, 1000 + arMod + timeMod)
        elif self.randNum == 5:
            super(ShakenState, self).MotorBehaviour(-1000 - arMod - timeMod, 1000 + arMod)
        elif self.randNum == 6:
            super(ShakenState, self).MotorBehaviour(-1000 - arMod, -1000 - arMod - timeMod)
        elif self.randNum == 7:
            super(ShakenState, self).MotorBehaviour(-1000 - arMod - timeMod, -1000 - arMod)