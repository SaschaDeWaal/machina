
import BaseState
import time

class RemoveSnowState(BaseState):

    def __init__(self):
        super(RemoveSnowState, self).__init__()
        self.timer = 2

    def onEnter(self):
        super(RemoveSnowState, self).onEnter()
        self.timer = 2

    def onLeave(self):
        super(RemoveSnowState, self).onLeave()

    def onUpdate(self, delta):
        super(RemoveSnowState, self).onUpdate(delta)
        self.timer -= delta

