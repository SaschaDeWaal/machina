
from BaseState import BaseState
import time
from DriveState import DriveState
import random

class ShakenState(DriveState):

    def __init__(self):
        super(ShakenState, self).__init__()
        self.timer = round(random.uniform(1, 4), 1)
        self.randNum = random.randrange(0, 7, 1)
        self.stateName = "ShakenState"
        self.colourTimer = 0.5
        self.shakenTimer = 10

    def onEnter(self):
        super(ShakenState, self).onEnter()
        self.timer = round(random.uniform(1, 4), 1)
        self.randNum = random.randrange(0, 7, 1)
        self.colourTimer = 0.5
        self.shakenTimer = 10

    def onLeave(self):
        teamCol = self.robotData.teamCol
        self.robotData.arduinoBridge.setTeamColour(teamCol)
        super(ShakenState, self).MotorBehaviour(0,0)
        super(ShakenState, self).onLeave()
        BaseState.goToState(self, "DriveState")

    """
    Update function
    A timer is set between 1 and 4 seconds. This timer determines how long the robot will drive in one of 8 manners
    randNum determines in what configuration the robot will drive around for -timer- amount of seconds.
    shakyMoves is called every frame to modify the speed with the time passed since last frame.
    """
    def onUpdate(self, delta):
        super(ShakenState, self).onUpdate(delta)
        self.shakenTimer -= delta
        if self.shakenTimer <= 0:
            self.onLeave()
        self.timer -= delta
        self.colourTimer -= delta
        if self.colourTimer <= 0:
            self.colourTimer = round(random.uniform(0.25,1), 1)
            randCol = random.randint(0,8)
            self.robotData.arduinoBridge.setTeamColour(randCol)
        if self.timer <= 0:
            self.timer = round(random.uniform(1,4), 1)
            self.randNum = random.randrange(0, 7, 1)
        self.shakyMoves(delta)


    """
    Shaken movement is taken care of here.
    Based on randNum, the robot drives forward, backward, left, or right.
    The speed at which is done so depends on the arousal level, and the amount of time spent driving in the current direction.
    Whatever direction the robot is driving in, it'll either be modified with a bias towards the right or left.
    This causes the robot to speed up in that direction while driving in that direction, resulting in 'drunk' behaviour.
    """
    def shakyMoves(self, delta):
        print "RandNum: " + str(self.randNum)
        #arMod = 800 * super(DriveState, self).robotData.arousal   # Modifier to motor power based on robot's arousal
        arMod = 800 * super(ShakenState, self).GetArousal()
        timeMod = 40000 * delta
        if self.randNum == 0:
            #super(ShakenState, self).MotorBehaviour(1000 + arMod, 1000 + arMod + timeMod)                  # used these initially
            #self.robotData.MotorBehaviour(1000 + arMod, 1000 + arMod + timeMod)
            self.robotData.motorLeft.setSpeed(1000 + arMod)
            self.robotData.motorRight.setSpeed(1000 + arMod + timeMod)
        elif self.randNum == 1:
            #super(ShakenState, self).MotorBehaviour(1000 + arMod + timeMod, 1000 + arMod)
            #self.robotData.MotorBehaviour(1000 + arMod + timeMod, 1000 + arMod)
            self.robotData.motorLeft.setSpeed(1000 + arMod + timeMod)
            self.robotData.motorRight.setSpeed(1000 + arMod)
        elif self.randNum == 2:
            #super(ShakenState, self).MotorBehaviour(1000 + arMod, -1000 - arMod - timeMod)
            #self.robotData.MotorBehaviour(1000 + arMod, -1000 - arMod - timeMod)
            self.robotData.motorLeft.setSpeed(1000 + arMod)
            self.robotData.motorRight.setSpeed(-1000 - arMod - timeMod)
        elif self.randNum == 3:
            #super(ShakenState, self).MotorBehaviour(1000 + arMod + timeMod, -1000 - arMod)
            #self.robotData.MotorBehaviour(1000 + arMod + timeMod, -1000 - arMod)
            self.robotData.motorLeft.setSpeed(1000 + arMod + timeMod)
            self.robotData.motorRight.setSpeed(-1000 - arMod)
        elif self.randNum == 4:
            #super(ShakenState, self).MotorBehaviour(-1000 - arMod, 1000 + arMod + timeMod)
            #self.robotData.MotorBehaviour(-1000 - arMod, 1000 + arMod + timeMod)
            self.robotData.motorLeft.setSpeed(-1000 - arMod)
            self.robotData.motorRight.setSpeed(1000 + arMod + timeMod)
        elif self.randNum == 5:
            #super(ShakenState, self).MotorBehaviour(-1000 - arMod - timeMod, 1000 + arMod)
            #self.robotData.MotorBehaviour(-1000 - arMod - timeMod, 1000 + arMod)
            self.robotData.motorLeft.setSpeed(-1000 - arMod - timeMod)
            self.robotData.motorRight.setSpeed(1000 + arMod)
        elif self.randNum == 6:
            #super(ShakenState, self).MotorBehaviour(-1000 - arMod, -1000 - arMod - timeMod)
            #self.robotData.MotorBehaviour(-1000 - arMod, -1000 - arMod - timeMod)
            self.robotData.motorLeft.setSpeed(-1000 - arMod)
            self.robotData.motorRight.setSpeed(-1000 - arMod - timeMod)
        elif self.randNum == 7:
            #super(ShakenState, self).MotorBehaviour(-1000 - arMod - timeMod, -1000 - arMod)
            #self.robotData.MotorBehaviour(-1000 - arMod - timeMod, -1000 - arMod)
            self.robotData.motorLeft.setSpeed(-1000 - arMod - timeMod)
            self.robotData.motorRight.setSpeed(-1000 - arMod)