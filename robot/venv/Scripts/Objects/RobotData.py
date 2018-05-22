
class RobotData:
    """ Here we can store data of the robot. This can be used and modified by the behaviours."""

    def __init__(self, motorLeft, motorRight, arduinoBridge):
        self.happiness = 0
        self.efficientness = 0

        self.motorLeft = motorLeft
        self.motorRight = motorRight
        self.arduinoBridge = arduinoBridge
        


