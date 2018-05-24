
import BaseState
import time

class AttackBaseState(BaseState):

    def __init__(self):
        super(AttackBaseState, self).__init__()
        self.timer = 2

    def onEnter(self):
        super(AttackBaseState, self).onEnter()
        self.timer = 2

    def onLeave(self):
        super(AttackBaseState, self).onLeave()

    def onUpdate(self, delta):
        super(AttackBaseState, self).onUpdate(delta)
        self.timer -= delta

