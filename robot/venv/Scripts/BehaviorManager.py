from threading import Thread
import time

from BehaviorStates.BaseState import BaseState
from BehaviorStates.IdleState import IdleState

states = {
    "IdleState": IdleState,
    "BaseState": BaseState
}

class BehaviorManager:

    def __init__(self, leftMotor, rightMotor, sensorBridge):
        self.leftMotor = leftMotor
        self.rightMotor = rightMotor
        self.sensorBridge = sensorBridge

        self.currentState = BaseState()
        self.setState("IdleState")
        self.lastTime = time.time()
        self.active = False

    def start(self):
        self.active = True
        self.thread = Thread(target=self.loop, args=())
        self.thread.start()

    def stop(self):
        self.active = False

    def setState(self, new_state_name):
        self.currentState.onLeave()
        self.currentState = states[new_state_name]()
        self.currentState.setVariables(self.leftMotor, self.rightMotor, self.sensorBridge)
        self.currentState.onEnter()

        print "enter new state: '" + new_state_name + "'"

    def loop(self):
        while self.active:
            delta = time.time() - self.lastTime;
            self.lastTime = time.time();

            if self.currentState.nextBehavior is None:
                self.currentState.onUpdate(delta)
            else:
                self.setState(self.currentState.nextBehavior)
