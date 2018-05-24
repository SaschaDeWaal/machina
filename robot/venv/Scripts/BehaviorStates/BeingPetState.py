
import BaseState
import time

class BeingPetState(BaseState):

    def __init__(self):
        super(BeingPetState, self).__init__()
        self.timer = 2

    def onEnter(self):
        super(BeingPetState, self).onEnter()
        self.timer = 2

    def onLeave(self):
        super(BeingPetState, self).onLeave()

    def onUpdate(self, delta):
        super(BeingPetState, self).onUpdate(delta)
        self.timer -= delta

