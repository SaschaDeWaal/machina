"""
Aggressive wander state, rapid acceleration
Also 'challenges' other robots when coming across them
"""

import BaseState
import time

class AngeredState(BaseState):

    def __init__(self):
        super(AngeredState, self).__init__()
        self.timer = 2

    def onEnter(self):
        super(AngeredState, self).onEnter()
        self.timer = 2

    def onLeave(self):
        super(AngeredState, self).onLeave()

    def onUpdate(self, delta):
        super(AngeredState, self).onUpdate(delta)
        self.timer -= delta

