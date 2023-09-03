# %%
from abc import ABCMeta, abstractclassmethod
from ObserverAbstract import Observer, Observerable

class Account(Observerable):
    def __init__(self):
        super().__init__()
        self._lastIp = {}
        self._lastRegion = {}
    def login(self, name, ip, time):
        # 取得登入地區
        region = self._getRegion(ip)
        # 判斷登入地區是否異常
        if self._isLongDistance(name, region):
            # 通知所有已註冊服務
            self.notifyObervers({"name":name, "ip":ip, "region":region, "time":time})
        self._lastRegion[name] = region
        self._lastIp[name] = ip

    # ip和地區對映函數
    def _getRegion(self, ip):
        ipRegion = {
            "127.0.0.1": "localhost",
            "10.15.73.38": "unimicron"
        }
        region = ipRegion.get(ip)
        return "" if region is None else region
    # 判斷登入異常函數
    def _isLongDistance(self, name, region):
        lastRegion = self._lastRegion.get(name)
        return lastRegion is not None and lastRegion != region

class SmsSender(Observer):
    def update(self, observable):
        print(
            f"""
            這是Sms服務
            注意，登入資訊異常，登入資訊如下：
            登入帳號: {observable["name"]},
            登入地區: {observable["region"]},
            登入ip: {observable["ip"]},
            登入時間: {observable["time"]}
            """
            )
        
class mailSender(Observer):
    def update(self, observable):
        print(
            f"""
            這是信件服務
            注意，登入資訊異常，登入資訊如下：
            登入帳號: {observable["name"]},
            登入地區: {observable["region"]},
            登入ip: {observable["ip"]},
            登入時間: {observable["time"]}
            """
            )

# %%
from datetime import datetime
if __name__ == '__main__':
    acount = Account()
    
    # 註冊sms異常服務
    acount.addObserver(SmsSender)
    # 註冊mail異常服務
    acount.addObserver(mailSender)
    acount.login('andy', '127.0.0.1', datetime.today())
    acount.login('andy', '10.15.73.38', datetime.now())
# %%
