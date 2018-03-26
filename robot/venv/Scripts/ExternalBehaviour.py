from DriveMotor import DriveMotor


class ExternalBehaviour:

    def __init__(self, leftMotor, rightMotor):
        self._motorA = leftMotor
        self._motorB = rightMotor
        _motorA.setDirection(1)


