# %%
from StateAbstract import Context, State

class search(Context):
    def __init__(self):
        super().__init__()
        self.addState(SQLState("SQL"))
        self.addState(MongoState("Mongo"))
        self.setQuery("SQL, SELECT * FORM db WHERE 1=1")
    
    def getQuery(self):
        return self._getStateInfo()

    def setQuery(self, query):
        return self._setStateInfo(query)
    
    def run_search(self):
        state = self.getState()
        if isinstance(state, State):
            state.behavior(self.getQuery())

class SQLState(State):
    def __init__(self, name):
        super().__init__(name)
    
    def isMatch(self, stateInfo):
        return stateInfo.split(',')[0] == "SQL"
    
    def behavior(self, stateInfo):
        print(f'run stateInfo: {stateInfo}')

class MongoState(State):
    def __init__(self, name):
        super().__init__(name)
    
    def isMatch(self, stateInfo):
        return stateInfo.split(',')[0] == "Mongo"
    
    def behavior(self, stateInfo):
        print(f'run stateInfo: {stateInfo}')
# %%
s = search()
s.run_search()

s.setQuery("Mongo, {'$match':{'key':'val'}}")
s.run_search()
# %%
