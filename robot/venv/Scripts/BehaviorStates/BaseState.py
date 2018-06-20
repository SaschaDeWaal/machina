import random

class BaseState(object):
    """ This is the base state. All other behaviors should inheritance from this object.
    If a event/other inheritance should be called/fired all the time, you can do it here """

    def __init__(self):
        self.nextBehavior = None
        self.robotData = None

    def setRobotData(self, robotData):
        """ Set the robot data so the behavior can use and modify it. """
        self.robotData = robotData
        self.gyro = self.robotData.getGyro()
        self.accel = self.robotData.getAccel()

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
        print "gyroscope:" + ', '.join(str(f) for f in self.robotData.getGyro())
        print "accelerometer" + ', '.join(str(f) for f in self.robotData.getAccel())
        if randInt == 42 and self.robotData.arousal > 6:
            self.goToState("AngeredState")
        deltaGyro = self.CalcDeltaGyro()       # Take the difference between the current and previous values of the gyroscope
        deltaAccel = self.CalcDeltaAccel()
        print "DeltaAccel: " + str(deltaAccel)
        if deltaAccel > 100:
            # go to beingShakenState, as it's being jostled
            self.goToState("ShakenState")
        if self.accel[1] > 100:
            # go to beingPetState, as it's being picked up
            self.goToState("BeingPetState")
        if self.robotData.arousal > 7:
            # go to AngeredState
            self.goToState("AngeredState")
        self.accel = self.robotData.accel
        pass

    def DetermineNextState(self):
        self.gyro = self.robotData.gyroscope
        if self.gyro[1] > 100:
            # go to beingPetState, as it's being picked up
            self.goToState("BeingPetState")

    def CalcDeltaGyro(self):
        self.robotData.getGyro()
        dX = self.gyro[0] - self.robotData.gyroscope[0]
        dY = self.gyro[1] - self.robotData.gyroscope[1]
        dZ = self.gyro[2] - self.robotData.gyroscope[2]
        return dX + dY + dZ

    def CalcDeltaAccel(self):
        self.robotData.getAccel()
        dX = self.accel[0] - self.robotData.accel[0]
        dY = self.accel[1] - self.robotData.accel[1]
        dZ = self.accel[2] - self.robotData.accel[2]
        return dX + dY + dZ