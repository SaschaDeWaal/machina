

class BaseState(object):
    """ This is the base state. All other behaviors should inheritance from this object.
    If a event/other inheritance should be called/fired all the time, you can do it here """

    def __init__(self):
        self.nextBehavior = None
        self.robotData = None

    def setRobotData(self, robotData):
        """ Set the robot data so the behavior can use and modify it. """
        self.robotData = robotData

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
