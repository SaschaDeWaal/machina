
import BaseState
import time

class BeingPetState(BaseState):

    def __init__(self):
        super(BeingPetState, self).__init__()
        self.timer = 5

    def onEnter(self):
        super(BeingPetState, self).onEnter()
        self.timer = 5

    def onLeave(self):
        super(BeingPetState, self).onLeave()

    def onUpdate(self, delta):
        super(BeingPetState, self).onUpdate(delta)
        self.timer -= delta
        if self.timer <= 0:
            self.robotData.setArousal(self.robotData.arousal - 1)
            self.timer = 5
        if not self.robotData.isBeingPetted:
            self.onLeave()