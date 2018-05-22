import sys
from Objects.DriveMotor import DriveMotor
from Objects.ArduinoBridge import ArduinoBridge
from Objects.RobotData import RobotData;
from BehaviorManager import BehaviorManager

# Create objects
leftMotor = DriveMotor(35, 37)
rightMotor = DriveMotor(36, 38)
arduinoBridge = ArduinoBridge()
RobotData = RobotData(leftMotor, rightMotor, arduinoBridge)
behaviorManager = BehaviorManager(RobotData)

# start behavior
behaviorManager.start()

# wait on exit
raw_input("Press Enter to exit")

#stop all threads
arduinoBridge.stop()
behaviorManager.stop()
sys.exit()




