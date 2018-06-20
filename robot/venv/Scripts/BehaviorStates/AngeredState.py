"""
Aggressive wander state, rapid acceleration
Also 'challenges' other robots when coming across them
"""

#import BaseState
import time
from DriveState import DriveState

class AngeredState(DriveState):

    def __init__(self):
        super(AngeredState, self).__init__()
        self.timer = 2
        self.stateName = "AngeredState"

    def onEnter(self):
        super(AngeredState, self).onEnter()

        self.timer = 2
        self.AngerMovement()
        self.onLeave()

    def onLeave(self):
        super(AngeredState, self).onLeave()

    def onUpdate(self, delta):
        super(AngeredState, self).onUpdate(delta)
        self.timer -= delta

    """
    hardcoded set of movements to indicate frustration
    """
    def AngerMovement(self):
        super(AngeredState, self).SetCurFunction(0.5, "TimeDriveForward", 0)
        #super(AngeredState, self).TimeDriveForward(0.5)
        super(AngeredState, self).SetCurFunction(0.5, "TimeDriveBackward", 0)
        #super(AngeredState, self).TimeDriveBackward(0.5)
        super(AngeredState, self).SetCurFunction(0.5, "TimeDriveForward", 0)
        #super(AngeredState, self).TimeDriveForward(0.5)
        super(AngeredState, self).SetCurFunction(0.5, "TimeDriveBackward", 0)
        #super(AngeredState, self).TimeDriveBackward(0.5)
        super(AngeredState, self).SetCurFunction(100000, "TurnDegrees", super(AngeredState,self)._degreesTurned - 10)
        #super(AngeredState, self).TurnDegrees(super(AngeredState, self)._degreesTurned - 10)
        super(AngeredState, self).SetCurFunction(0.5, "TimeDriveForward", 0)
        #super(AngeredState, self).TimeDriveForward(0.5)
        super(AngeredState, self).SetCurFunction(0.5, "TimeDriveBackward", 0)
        #super(AngeredState, self).TimeDriveBackward(0.5)
        super(AngeredState, self).SetCurFunction(0.5, "TimeDriveForward", 0)
        #super(AngeredState, self).TimeDriveForward(0.5)
        super(AngeredState, self).SetCurFunction(0.5, "TimeDriveBackward", 0)
        #super(AngeredState, self).TimeDriveBackward(0.5)
        super(AngeredState, self).SetCurFunction(100000, "TurnDegrees", super(AngeredState, self)._degreesTurned + 20)
        #super(AngeredState, self).TurnDegrees(super(AngeredState, self)._degreesTurned + 20)
        super(AngeredState, self).SetCurFunction(0.5, "TimeDriveForward", 0)
        #super(AngeredState, self).TimeDriveForward(0.5)
        super(AngeredState, self).SetCurFunction(0.5, "TimeDriveBackward", 0)
        #super(AngeredState, self).TimeDriveBackward(0.5)
        super(AngeredState, self).SetCurFunction(0.5, "TimeDriveForward", 0)
        #super(AngeredState, self).TimeDriveForward(0.5)
        super(AngeredState, self).SetCurFunction(0.5, "TimeDriveBackward", 0)
        #super(AngeredState, self).TimeDriveBackward(0.5)
        super(AngeredState, self).SetCurFunction(100000, "TurnDegrees", super(AngeredState, self)._degreesTurned - 10)
        #super(AngeredState, self).TurnDegrees(super(AngeredState, self)._degreesTurned - 10)

