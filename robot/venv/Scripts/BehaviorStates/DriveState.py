
import BaseState
import time

class DriveState(BaseState):

    def __init__(self):
        super(DriveState, self).__init__()
        self.timer = 2

    def onEnter(self):
        super(DriveState, self).onEnter()
        self.timer = 2

    def onLeave(self):
        super(DriveState, self).onLeave()

    def onUpdate(self, delta):
        super(DriveState, self).onUpdate(delta)
        self.timer -= delta

