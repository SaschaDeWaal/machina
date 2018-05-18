
class RobotData:

    def __init__(self, motorLeft, motorRight):
        self.happiness = 0
        self.efficientness = 0
        self.motorLeft = motorLeft
        self.motorRight = motorRight

    def setData(self, motorRight, motorLeft):
        self.motorRight = motorRight
        self.motorLeft = motorLeft


