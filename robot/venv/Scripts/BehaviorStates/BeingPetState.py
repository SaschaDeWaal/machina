
from BaseState import BaseState
import time

class BeingPetState(BaseState):

    def __init__(self):
        super(BeingPetState, self).__init__()
        self.timer = 3
        self.beingPet = False
        self.stateName = "BeingPetState"

    def onEnter(self):
        super(BeingPetState, self).onEnter()
        self.timer = 3
        self.beingPet = False

    def onLeave(self):
        super(BeingPetState, self).onLeave()

    """
    Keeps track of the beingPet variable, which is set to True/False depending on light sensor input.
    If pet for 3 seconds, the robot's arousal will decrease.
    """
    def onUpdate(self, delta):
        super(BeingPetState, self).onUpdate(delta)
        print self.robotData.getLight()
        if self.robotData.light[0] > 200 and self.robotData.light[1] > 200 and self.robotData.light[2] > 200:
            self.beingPet = True
        self.timer -= delta
        if self.timer <= 0:
            self.robotData.setArousal(self.robotData.arousal - 1)
            self.timer = 3
        if not self.beingPet:
            self.onLeave()
        #if not self.robotData.isBeingPetted:
        #    self.onLeave()