import sys

from Objects.DriveMotor import DriveMotor
from Objects.SensorBridge import SensorBridge
from Objects.Camera import Camera
#import ExternalBehaviour

#create motors
leftMotor = DriveMotor(35, 37)
rightMotor = DriveMotor(36, 38)

#exBeh = ExternalBehaviour.ExternalBehaviour(leftMotor, rightMotor)

sensorBridge = SensorBridge()
camera = Camera()

#wait until exit
while raw_input('Exit? (y): ') != 'y':
    print ""

#stop all
#sensorBridge.stop()
camera.stop()
sys.exit()




