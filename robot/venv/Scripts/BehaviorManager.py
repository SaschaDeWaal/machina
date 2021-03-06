from threading import Thread
import time

from BehaviorStates.BaseState import BaseState
from BehaviorStates.IdleState import IdleState
from BehaviorStates.ShakenState import ShakenState
from BehaviorStates.AngeredState import AngeredState
from BehaviorStates.BeingPetState import BeingPetState
from BehaviorStates.ReturnToBaseState import ReturnToBaseState
from BehaviorStates.RemoveSnowState import RemoveSnowState
from BehaviorStates.AttackBaseState import AttackBaseState
from BehaviorStates.DriveState import DriveState

states = {
    "IdleState": IdleState,
    "BaseState": BaseState,
    "ShakenState": ShakenState,
    "AngeredState": AngeredState,
    "BeingPetState": BeingPetState,
    "ReturnToBaseState": ReturnToBaseState,
    "RemoveSnowState": RemoveSnowState,
    "AttackBaseState": AttackBaseState,
    "DriveState": DriveState
}

class BehaviorManager:

    def __init__(self, robotData):
        print "Create behavior manager with default behavior 'IdleState'"

        self.robotData = robotData
        self.lastTime = time.time()
        self.active = False
        self.thread = None

        self.currentState = BaseState()
        self.setState("IdleState")

    def start(self):
        """ Start the behavior manager in a new thread """

        self.active = True
        self.thread = Thread(target=self.loop, args=())
        self.thread.start()

    def stop(self):
        """ Stop the behavior thread. This will also stop the current behavior """
        self.active = False


    def setState(self, new_state_name):
        """ Change the current behavior state """
        if not (self.currentState.stateName == new_state_name):       # Ensuring the same state can't be entered while in that state
            print "left state: " + self.currentState.stateName
            self.currentState.onLeave()
            self.currentState = states[new_state_name]()
            self.currentState.setRobotData(self.robotData)
            self.currentState.onEnter()
            print "enter new state: '" + new_state_name + "'"

    def loop(self):
        while self.active:
            delta = time.time() - self.lastTime
            self.lastTime = time.time()

            if self.currentState.nextBehavior is None:
                self.currentState.onUpdate(delta)
            else:
                if not (self.currentState.stateName == self.currentState.nextBehavior):
                    self.setState(self.currentState.nextBehavior)
                else:
                    self.currentState.onUpdate(delta)

