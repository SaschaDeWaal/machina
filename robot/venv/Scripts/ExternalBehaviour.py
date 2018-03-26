from DriveMotor import DriveMotor
import InternalBehaviour
import time
import Sensor

"""

File/class that's supposed to be used to the apparent behaviour of the robot.
This includes things such as doing a victory dance, the specifics of which are dependant on the parameters
found in InternalBehaviour.

"""

class ExternalBehaviour:

<<<<<<< HEAD
    def __init__(self, leftMotor, rightMotor):
        self._motorLeft = leftMotor
        self._motorRight = rightMotor
        _motor.setDirection(1)
=======
    def __init__(self, motorLeft, motorRight):
        self._motorLeft = motorLeft
        self._motorRight = motorRight
        #_motorA.setDirection(1)
<<<<<<< HEAD
        InternalBehaviour._funFrust = 5 #test
=======
>>>>>>> bdb8d7be68fdf2f9480d18658935a468cabe5823
>>>>>>> e8d3e842501e70bc7b3e7dad96a9b952bc0ed9d0


