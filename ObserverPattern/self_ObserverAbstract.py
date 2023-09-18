# %%
# 引入python 抽象類別套件
from abc import ABCMeta, abstractmethod

class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass

class Observerable:
    def __init__(self) -> None:
        self._observer = []
    def addObserver(self, observer):
        self._observer.append(observer)
    def remoteObserver(self, observer):
        self._observer.remove(observer)
    def notifyObserver(self):
        for observer in self._observer:
            observer.update(self)
# %%
