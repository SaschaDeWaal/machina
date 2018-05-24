
import BaseState
import time

class ShakenState(BaseState):

    def __init__(self):
        super(ShakenState, self).__init__()
        self.timer = 2

    def onEnter(self):
        super(ShakenState, self).onEnter()
        self.timer = 2

    def onLeave(self):
        super(ShakenState, self).onLeave()

    def onUpdate(self, delta):
        super(ShakenState, self).onUpdate(delta)
        self.timer -= delta

