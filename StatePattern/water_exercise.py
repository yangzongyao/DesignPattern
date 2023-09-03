# %%
from StateAbstract import Context, State

class Water(Context):
    def __init__(self):
        super().__init__()
        self.addState(SolidState("固態"))
        self.addState(LiquidState("液態"))
        self.addState(GaseousState("氣態"))
        self.setTemperature(25)
    
    def getTemperature(self):
        return self._getStateInfo()
    
    def setTemperature(self, temperature):
        return self._setStateInfo(temperature)
    
    def riseTemperature(self, step):
        self._setStateInfo(self.getTemperature() + step)

    def reduceTemperature(self, step):
        self.setTemperature(self.getTemperature() - step)

    def behavior(self):
        state = self.getState()
        if(isinstance(state, State)):
            print(f'now stateInfo: {self._getStateInfo()}')
            state.behavior()

def singleton(obj, *args, **kwargs):
    "類別所實體化的物件永遠是唯一"
    instance = {}
    def _singleton(*args, **kwargs):
        if obj not in instance:
            instance[obj] = obj(*args, **kwargs)
        return instance[obj]
    return _singleton

@singleton
class SolidState(State):
    def __init__(self, name):
        self._name = name
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo < 0
        
@singleton
class LiquidState(State):
    def __init__(self, name):
        self._name = name
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo >= 0 and stateInfo < 100

@singleton
class GaseousState(State):
    def __init__(self, name):
        self._name = name
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo >= 100

# %%
water = Water()
water.behavior()
print('-----------------')
water.setTemperature(101)
water.behavior()
print('-----------------')
water.reduceTemperature(20)
water.behavior()
print('-----------------')
water.setTemperature(-20)
water.behavior()
print('-----------------')
water.riseTemperature(43)
water.behavior()
# %%
