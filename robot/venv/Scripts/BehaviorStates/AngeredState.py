"""
Aggressive wander state, rapid acceleration
Also 'challenges' other robots when coming across them
"""

from BaseState import BaseState
import time
from DriveState import DriveState
import random

class AngeredState(DriveState):

    def __init__(self):
        super(AngeredState, self).__init__()
        self.timer = random.uniform(10, 15)
        self.stateName = "AngeredState"
        random.uniform(10, 15)
        self.angerTime = random.uniform(10, 15)

    def onEnter(self):
        super(AngeredState, self).onEnter()
        self.robotData.arduinoBridge.setTeamColour(3)           # Takes on red colour
        self.timer = random.uniform(10, 15)
        self.angerTime = random.uniform(10, 15)
        self.AngerMovement()
        #self.onLeave()

    def onLeave(self):
        self.robotData.arduinoBridge.setTeamColour(self.robotData.teamCol)
        super(AngeredState, self).onLeave()
        #super(AngeredState, self).goToState("BaseState")
        BaseState.goToState(self, "DriveState")

    def onUpdate(self, delta):
        super(AngeredState, self).onUpdate(delta)
        self.timer -= delta
        self.angerTime -= delta
        if self.timer <= 0:
            self.onLeave()
        elif self.angerTime <= 0:
            self.onLeave()

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
        #super(AngeredState, self).SetCurFunction(100000, "TurnDegrees", super(AngeredState,self).degreesTurned - 10)
        super(AngeredState, self).SetCurFunction(100000, "TurnDegrees", super(AngeredState, self).GetDegsTurned() - 10)
        #super(AngeredState, self).TurnDegrees(super(AngeredState, self)._degreesTurned - 10)
        super(AngeredState, self).SetCurFunction(0.5, "TimeDriveForward", 0)
        #super(AngeredState, self).TimeDriveForward(0.5)
        super(AngeredState, self).SetCurFunction(0.5, "TimeDriveBackward", 0)
        #super(AngeredState, self).TimeDriveBackward(0.5)
        super(AngeredState, self).SetCurFunction(0.5, "TimeDriveForward", 0)
        #super(AngeredState, self).TimeDriveForward(0.5)
        super(AngeredState, self).SetCurFunction(0.5, "TimeDriveBackward", 0)
        #super(AngeredState, self).TimeDriveBackward(0.5)
        #super(AngeredState, self).SetCurFunction(100000, "TurnDegrees", super(AngeredState, self).degreesTurned + 20)
        super(AngeredState, self).SetCurFunction(100000, "TurnDegrees", super(AngeredState, self).GetDegsTurned() + 20)
        #super(AngeredState, self).TurnDegrees(super(AngeredState, self)._degreesTurned + 20)
        super(AngeredState, self).SetCurFunction(0.5, "TimeDriveForward", 0)
        #super(AngeredState, self).TimeDriveForward(0.5)
        super(AngeredState, self).SetCurFunction(0.5, "TimeDriveBackward", 0)
        #super(AngeredState, self).TimeDriveBackward(0.5)
        super(AngeredState, self).SetCurFunction(0.5, "TimeDriveForward", 0)
        #super(AngeredState, self).TimeDriveForward(0.5)
        super(AngeredState, self).SetCurFunction(0.5, "TimeDriveBackward", 0)
        #super(AngeredState, self).TimeDriveBackward(0.5)
        #super(AngeredState, self).SetCurFunction(100000, "TurnDegrees", super(AngeredState, self).degreesTurned - 10)
        super(AngeredState, self).SetCurFunction(100000, "TurnDegrees", super(AngeredState, self).GetDegsTurned() - 10)
        #super(AngeredState, self).TurnDegrees(super(AngeredState, self)._degreesTurned - 10)
        #self.onLeave()

