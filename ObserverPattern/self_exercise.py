# %%
from ObserverAbstract import Observer, Observerable
from datetime import datetime

class WebApp(Observerable):
    def __init__(self):
        super().__init__()
        self.app = []
    
    def add_app(self, https):
        if not self.getResponse(https):
            self.notifyObervers({'https':https, 'time':datetime.now()})
        else:
            self.app.append(https)
            print(f'{https} 新增成功')


    def getResponse(self, https):
        return True if https == "127.0.0.1" else False
    

class app(Observer):
    def update(self, observable):
        print(
f"""
app({observable['https']}) response 異常,
異常發生時間: {observable["time"]},

        新增失敗
"""
        )

if __name__ == '__main__':
    web = WebApp()
    web.addObserver(app)
    web.add_app('127.0.0.1')
    web.add_app('192.168.0.1')
# %%
