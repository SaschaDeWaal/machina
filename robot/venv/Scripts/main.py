import sys
from Objects.DriveMotor import DriveMotor
from Objects.SensorBridge import SensorBridge
from BehaviorManager import BehaviorManager;

#create motors
leftMotor = DriveMotor(35, 37)
rightMotor = DriveMotor(36, 38)
sensorBridge = SensorBridge()
behaviorManager = BehaviorManager(leftMotor, rightMotor, sensorBridge)

# start
behaviorManager.start()

raw_input("Press Enter to exit")

#stop all
sensorBridge.stop()
behaviorManager.stop()
sys.exit()




