from DriveMotor import DriveMotor


class ExternalBehaviour:

    def __init__(self, leftMotor, rightMotor):
        self._motorLeft = leftMotor
        self._motorRight = rightMotor
        _motor.setDirection(1)


