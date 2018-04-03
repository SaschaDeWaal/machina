import time
import thread
from NetworkManager import NetworkManager
from DriveMotor import DriveMotor
import ExternalBehaviour

def startNetwork():
    networkManager.startConnection()

#create motors
leftMotor = DriveMotor(35, 37)
rightMotor = DriveMotor(36, 38)

exBeh = ExternalBehaviour.ExternalBehaviour(leftMotor, rightMotor)

networkManager = NetworkManager()
thread.start_new_thread(startNetwork, ())

for dir in range(-1, 2):
    leftMotor.setDirection(dir)
    rightMotor.setDirection(dir)
    for i in range(10, 30):
        leftMotor.setSpeed(i * 1000)
        rightMotor.setSpeed(i * 1000)
        print('speed: ' + str(i * 1000))
        networkManager.sendMessage(str(i * 1000) + ' dir: ' + str(dir))
        time.sleep(1)



leftMotor.setDirection(0)
rightMotor.setDirection(0)



