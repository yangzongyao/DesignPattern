# %%
from self_ObserverAbstract import Observer, Observerable
from datetime import datetime
import numpy as np

class ai_training_pipeline(Observerable):
    def __init__(self) -> None:
        super().__init__()
    
    def training(self):
        while True:
            if not self._isError():
                print('training...')
            else:
                self.notifyObserver()
                break

    def _isError(self):
        return np.random.choice([0, 1], p=[0.8, 0.2])

class epoch_check(Observer):
    def update(self):
        s = """epoch error, pleace check batch"""
        print(s)

class ping_check(Observer):
    def update(self):
        s = """ping error, pleace check connect"""
        print(s)


if __name__ == '__main__':
    ai = ai_training_pipeline()
    ai.addObserver(epoch_check)
    ai.addObserver(ping_check)
    ai.training()
# %%
