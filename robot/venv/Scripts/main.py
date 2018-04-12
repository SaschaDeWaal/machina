import time
import thread
import sys

from DriveMotor import DriveMotor
from SensorBridge import SensorBridge
#import ExternalBehaviour

#create motors
leftMotor = DriveMotor(35, 37)
rightMotor = DriveMotor(36, 38)

#exBeh = ExternalBehaviour.ExternalBehaviour(leftMotor, rightMotor)

sensorBridge = SensorBridge()

#wait until exit
while raw_input('Exit? (y): ') != 'y':
    print "msg index: " + sensorBridge.lastData['index']


sensorBridge.stop()
sys.exit()




