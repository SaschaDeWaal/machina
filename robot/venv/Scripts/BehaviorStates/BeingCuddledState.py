
import BaseState
import time

class BeingCuddledState(BaseState):

    def __init__(self):
        super(BeingCuddledState, self).__init__()
        self.timer = 2

    def onEnter(self):
        super(BeingCuddledState, self).onEnter()
        self.timer = 2

    def onLeave(self):
        super(BeingCuddledState, self).onLeave()

    def onUpdate(self, delta):
        super(BeingCuddledState, self).onUpdate(delta)
        self.timer -= delta

