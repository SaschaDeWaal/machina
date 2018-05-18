

class BaseState(object):

    def __init__(self):
        self.nextBehavior = None
        self.leftMotor = None
        self.rightMotor = None
        self.sensorBridge = None


    def setVariables(self, leftMotor, rightMotor, sensorBridge):
        self.leftMotor = leftMotor
        self.rightMotor = rightMotor
        self.sensorBridge = sensorBridge;

    def goToState(self, newState):
        """ call this to tell the system this behaviour has failed """
        self.nextBehavior = newState

    def onEnter(self):
        """ Called when this behavior starts """
        pass

    def onLeave(self):
        """ Called when this behavior stops """
        pass

    def onUpdate(self, delta):
        """ Called every frame """
        pass
