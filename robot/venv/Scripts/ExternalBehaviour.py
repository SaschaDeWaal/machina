from DriveMotor import DriveMotor
from InternalBehaviour import InternalBehaviour


class ExternalBehaviour:


    def __init__(self, leftMotor, rightMotor):
        self._motorLeft = leftMotor
        self._motorRight = rightMotor
        _motor.setDirection(1)

    def __init__(self, motorLeft, motorRight):
        self._motorLeft = motorLeft
        self._motorRight = motorRight
        #_motorA.setDirection(1)



