
from BaseState import BaseState
import time

class BeingChargedState(BaseState):

    def __init__(self):
        super(BeingChargedState, self).__init__()
        self.timer = 2

    def onEnter(self):
        super(BeingChargedState, self).onEnter()
        self.timer = 2

    def onLeave(self):
        super(BeingChargedState, self).onLeave()

    def onUpdate(self, delta):
        super(BeingChargedState, self).onUpdate(delta)
        self.timer -= delta

