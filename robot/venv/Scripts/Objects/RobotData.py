import time
import random

class RobotData:
    """ Here we can store data of the robot. This can be used and modified by the behaviours."""

    def __init__(self, motorLeft, motorRight, arduinoBridge):
        self.happiness = 0
        self.efficientness = 0
        self.arousal = 1                        # Parameter that indicates the anger level within a robot.
                                                # As it increases, the robot should move more aggressively
                                                # Should have a value between 1 and 10 (inclusive)
        self.isBeingPetted = False  # Whether robot is being petted, depends on light sensor input

        self.motorLeft = motorLeft
        self.motorRight = motorRight
        self.arduinoBridge = arduinoBridge
        self.gyroscope = [0, 0, 0]              # and gyroscope for balance
        self.accel = [0, 0, 0]                  # 3 numbers for acceleration in x,y,z direction
        self.timer = 5
        self.light = [0,0,0]
        #self.teamCol = random.randint(0,2)
        self.teamCol = 1
        self.arduinoBridge.setTeamColour(self.teamCol)

    # Setter for the arousal parameter.
    def setArousal(self, value):
        self.arousal = value
        self.capArousal()

    def getGyro(self):
        #print self.arduinoBridge.lastData["gyroscoop"]
        self.gyroscope = self.arduinoBridge.lastData["gyroscoop"]
        return self.arduinoBridge.lastData["gyroscoop"]

    def getAccel(self):
        self.accel = self.arduinoBridge.lastData["accelerator"]
        return self.arduinoBridge.lastData["accelerator"]

    def getLight(self):
        self.light = self.arduinoBridge.lastData["light"]
        return self.arduinoBridge.lastData["light"]

    # Used to ensure arousal won't go above 10, or below 1.
    def capArousal(self):
        if self.arousal > 10:
            self.arousal = 10
        elif self.arousal < 1:
            self.arousal = 1


    """
    Handled in BeingPetState, but kept here inb4 it'll be necessary somehow
    """
    # Function that should decrease arousal level depending on how long the robot is being pet
    def pettingEffect(self, timeStarted):
        # Something with a timer...?
        if True: #if arduinobridge.something -> if light sensor is above some value
            self.isBeingPetted = True
            # go to BeingPetState
        else:
            self.isBeingPetted = False

    """
    Function that takes the supposed directions and speeds for both motors to change.
    A negative number indicates the motor should drive backward
    """
    def MotorBehaviour(self, speedLeft, speedRight):
        self.motorLeft.setSpeed(speedLeft)
        self.motorRight.setSpeed(speedRight)