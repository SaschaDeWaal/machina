import random

class BaseState(object):
    """ This is the base state. All other behaviors should inheritance from this object.
    If a event/other inheritance should be called/fired all the time, you can do it here """

    def __init__(self):
        self.nextBehavior = None
        self.robotData = None
        self.gyro = self.robotData.gyroscope

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

    """
    Mainly performs checks to see what state should be transitioned to, based on sensor input.
    """
    def onUpdate(self, delta):
        """ Called every frame """
        randInt = random.randrange(1, 50, 1)
        if randInt == 42 and self.robotData.arousal > 6:
            self.goToState("AngeredState")
        deltaGyro = self.gyro - self.robotData.gyroscope        # Take the difference between the current and previous values of the gyroscope
        if deltaGyro[0] + deltaGyro[1] + deltaGyro[2] > 100:
            # go to beingShakenState, as it's being jostled
            self.goToState("ShakenState")
        if self.gyro[1] > 100:
            # go to beingPetState, as it's being picked up
            self.goToState("BeingPetState")
        if self.robotData.arousal > 7:
            # go to AngeredState
            self.goToState("AngeredState")
        self.gyro = self.robotData.gyroscope
        pass

    def DetermineNextState(self):
        self.gyro = self.robotData.gyroscope
        if self.gyro[1] > 100:
            # go to beingPetState, as it's being picked up
            self.goToState("BeingPetState")