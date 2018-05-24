
import BaseState
import time

class ReturnToBaseState(BaseState):

    def __init__(self):
        super(ReturnToBaseState, self).__init__()
        self.timer = 2

    def onEnter(self):
        super(ReturnToBaseState, self).onEnter()
        self.timer = 2

    def onLeave(self):
        super(ReturnToBaseState, self).onLeave()

    def onUpdate(self, delta):
        super(ReturnToBaseState, self).onUpdate(delta)
        self.timer -= delta

