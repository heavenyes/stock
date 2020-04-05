from selenium import webdriver
from requests_html import HTML
import time
import json
from trading_report import TradingReport
import pymysql.cursors
from db_connection import DBConnection

class DownloadVolume:
    
    def __init__(self,code):
        self.code = code
        self.driver = webdriver.Chrome()

    def download(self):
        codeStr=self.getCode(self.code)
        self.driver.get("https://xueqiu.com/S/"+codeStr)
        begin=int(time.time())*1000
        self.driver.get("https://stock.xueqiu.com/v5/stock/chart/kline.json?symbol="+codeStr+"&begin="+str(begin)+"&period=month&type=before&count=-142&indicator=kline,pe,pb,ps,pcf,market_capital,agt,ggt,balance")
        html=HTML(html=self.driver.page_source)
        resp=html.find("pre",first=True).text
        data=json.loads(resp)
        tradingReportList=[]
        for item in data["data"]["item"]:
            report=TradingReport(self.code,item)
            tradingReportList.append(report)

        connection=DBConnection.getConnection()
        try:
            with connection.cursor() as cursor:
                for report in tradingReportList:
                   sql="INSERT INTO `trading_report` (`stock_code`, `report_peroid`,`trading_report`,create_time,update_time) VALUES (%s,%s,%s,now(),now()) on duplicate key update trading_report=%s,update_time=now()"           
                   cursor.execute(sql, (report.code,report.date, json.dumps(report,default=lambda obj: obj.__dict__),json.dumps(report,default=lambda obj: obj.__dict__)))
            connection.commit()
        finally:
            connection.close()
    
    def getCode(self,code):
        if str(code)[0:1]=='6':
            return "SH"+str(code)
        else:
            return "SZ"+str(code)

if __name__ =="__main__":
    DownloadVolume("300596").download()

