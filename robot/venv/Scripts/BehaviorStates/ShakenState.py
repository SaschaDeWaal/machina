
import BaseState
import time
import DriveState
import random

class ShakenState(DriveState):

    def __init__(self):
        super(ShakenState, self).__init__()
        self.timer = 2
        self.randNum = random.randrange(0, 3, 1)

    def onEnter(self):
        super(ShakenState, self).onEnter()
        self.randNum = random.randrange(0, 3, 1)

    def onLeave(self):
        super(ShakenState, self).onLeave()
        super(ShakenState, self).MotorBehaviour(0,0)

    def onUpdate(self, delta):
        super(ShakenState, self).onUpdate(delta)
        self.timer -= delta
        if self.timer <= 0:
            self.timer = random.randrange(1, 4, 0.5)
            self.randNum = random.randrange(0, 3, 1)
        self.shakyMoves(delta)

    def shakyMoves(self, delta):
        arMod = 800 * super(ShakenState, self).robotData.arousal   # Modifier to motor power based on robot's arousal
        timeMod = 10000 * delta
        if self.randNum == 0:
            super(ShakenState, self).MotorBehaviour(1000 + arMod + timeMod, 1000 + arMod + timeMod)
        elif self.randNum == 1:
            super(ShakenState, self).MotorBehaviour(-1000 - arMod - timeMod, 1000 + arMod + timeMod)
        elif self.randNum == 2:
            super(ShakenState, self).MotorBehaviour(1000 + arMod + timeMod, -1000 - arMod - timeMod)
        elif self.randNum == 3:
            super(ShakenState, self).MotorBehaviour(-1000 - arMod - timeMod, -1000 - arMod - timeMod)
