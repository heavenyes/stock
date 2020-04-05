import time 

class TradingReport:
    def __init__(self,code,data):
        self.code=code
        self.date= time.strftime("%Y-%m-%d",time.localtime(data[0]/1000))
        self.volumn=data[1]
        self.open=data[2]
        self.high=data[3]
        self.low=data[4]
        self.close=data[5]
        self.chg=data[6]
        self.percent=data[7]
        self.turnoverrate=data[8]
        self.amount=data[9]
        self.volume_post=data[10]
        self.amount_post=data[11]
        self.pe=data[12]
        self.pb=data[13]
        self.ps=data[14]
        self.pcf=data[15]
        self.market_capital=data[16]
        self.balance=data[17]
