# %%
# 引入python 抽象類別套件
from abc import ABCMeta, abstractmethod

class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, observable, object):
        pass

class Observerable:
    def __init__(self):
        self._observer = []
    def addObserver(self, observer):
        self._observer.append(observer)
    def removeObaserver(self, observer):
        self._observer.remove(observer)
    def notifyObervers(self, object=0):
        for o in self._observer:
            o.update(self, object)
# %%
