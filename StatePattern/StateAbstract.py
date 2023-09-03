# %%
from abc import ABCMeta, abstractmethod

class Context(metaclass = ABCMeta):
    def __init__(self):
        self._states = []
        self._curState = None

    def addState(self, state):
        if state not in self._states:
            self._states.append(state)

    def changeState(self, state):
        if state is None:
            return False
        if self._curState is None:
            print(f'init {state.getName()}')
        else:
            print(f'{self._curState.getName()} convert to {state.getName()}')
        self._curState = state
        self.addState(state)    
        return True

    def getState(self):
        return self._curState

    def _setStateInfo(self, stateInfo):
        self._stateInfo = stateInfo
        for state in self._states:
            if state.isMatch(stateInfo):
                self.changeState(state)

    def _getStateInfo(self):
        return self._stateInfo

class State:
    def __init__(self, name):
        self._name = name
    def getName(self):
        return self._name
    def isMatch(self):
        '判斷裝態的stateInfo屬性是否屬於當前範圍'
        return False
    @abstractmethod
    def behavior(self):
        print(f'{self._name} behavior')
# %%
