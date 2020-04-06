import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd 
from report_type import ReportType
from main_report import MainReport
from debt_report import DebtReport
from benefit_report import BenefitReport
from cash_report import CashReport
from trading_report import TradingReport
import json
import pymysql.cursors
from db_connection import DBConnection
from requests_html import HTML

class DownloadReport:

    def __init__(self,code):
        self.code=code
        self.driver = webdriver.Chrome()

        # chrome_options =Options()
        # chrome_options.add_argument('--headless')
        # self.driver = webdriver.Chrome(options=chrome_options)

    def getQuarter(self,peroid):
        month = peroid[5:7]
        if month == "03":
            return 1
        elif month=="06":
            return 2
        elif month =="09":
            return 3
        elif month =="12":
            return 4

    def downloadMainReport(self,count):
        self.driver.get("https://xueqiu.com/snowman/S/{0}".format(self.code))
        currentTime=int(time.time())*1000
        self.driver.get("https://stock.xueqiu.com/v5/stock/finance/cn/indicator.json?symbol={0}&type=all&is_detail=true&count={1}&timestamp={2}".format(self.code,count,currentTime))
        html=HTML(html=self.driver.page_source)
        resp=html.find("pre",first=True).text
        data=json.loads(resp)
        reportList=[]
        for item in data["data"]["list"]:
            report=MainReport(self.code,data["data"]["quote_name"],item)
            reportList.append(report)
        sql="INSERT INTO `financial_report` (`stock_code`,`stock_name`,`report_peroid`,`quarter`,`main_report`,create_time,update_time) VALUES (%s, %s,%s,%s,%s,now(),now()) on duplicate key update main_report=%s,update_time=now()"           
        self.saveReport(sql,reportList)

    def downloadBenefitReport(self,count):
        self.driver.get("https://xueqiu.com/snowman/S/{0}".format(self.code))
        currentTime=int(time.time())*1000
        self.driver.get("https://stock.xueqiu.com/v5/stock/finance/cn/income.json?symbol={0}&type=all&is_detail=true&count={1}&timestamp={2}".format(self.code,count,currentTime))
        html=HTML(html=self.driver.page_source)
        resp=html.find("pre",first=True).text
        data=json.loads(resp)
        reportList=[]
        for item in data["data"]["list"]:
            report=BenefitReport(self.code,data["data"]["quote_name"],item)
            reportList.append(report)
        sql="INSERT INTO `financial_report` (`stock_code`,`stock_name`,`report_peroid`,`quarter`,`benefit_report`,create_time,update_time) VALUES (%s, %s,%s,%s,%s,now(),now()) on duplicate key update benefit_report=%s,update_time=now()"           
        self.saveReport(sql,reportList)

    def downloadDebtReport(self,count):
        self.driver.get("https://xueqiu.com/snowman/S/{0}".format(self.code))
        currentTime=int(time.time())*1000
        self.driver.get("https://stock.xueqiu.com/v5/stock/finance/cn/balance.json?symbol={0}&type=all&is_detail=true&count={1}&timestamp={2}".format(self.code,count,currentTime))
        html=HTML(html=self.driver.page_source)
        resp=html.find("pre",first=True).text
        data=json.loads(resp)
        reportList=[]
        for item in data["data"]["list"]:
            report=DebtReport(self.code,data["data"]["quote_name"],item)
            reportList.append(report)
        sql="INSERT INTO `financial_report` (`stock_code`,`stock_name`,`report_peroid`,`quarter`,`debt_report`,create_time,update_time) VALUES (%s, %s,%s,%s,%s,now(),now()) on duplicate key update debt_report=%s,update_time=now()"           
        self.saveReport(sql,reportList)

    def downloadCashReport(self,count):
        self.driver.get("https://xueqiu.com/snowman/S/{0}".format(self.code))
        currentTime=int(time.time())*1000
        self.driver.get("https://stock.xueqiu.com/v5/stock/finance/cn/cash_flow.json?symbol={0}&type=all&is_detail=true&count={1}&timestamp={2}".format(self.code,count,currentTime))
        html=HTML(html=self.driver.page_source)
        resp=html.find("pre",first=True).text
        data=json.loads(resp)
        reportList=[]
        for item in data["data"]["list"]:
            report=CashReport(self.code,data["data"]["quote_name"],item)
            reportList.append(report)
        sql="INSERT INTO `financial_report` (`stock_code`,`stock_name`,`report_peroid`,`quarter`,`cash_report`,create_time,update_time) VALUES (%s, %s,%s,%s,%s,now(),now()) on duplicate key update cash_report=%s,update_time=now()"           
        self.saveReport(sql,reportList)

    def saveReport(self,sql,reportList):
        connection = DBConnection.getConnection()
        try:
            with connection.cursor() as cursor:
                for report in reportList:
                    cursor.execute(sql, (report.code,report.name,report.date, self.getQuarter(report.date),json.dumps(report,default=lambda obj: obj.__dict__),json.dumps(report,default=lambda obj: obj.__dict__)))
            connection.commit()
        finally:
            connection.close()    

    def downloadVolumeReport(self):
      
        self.driver.get("https://xueqiu.com/S/{0}".format(self.code))
        begin=int(time.time())*1000
        self.driver.get("https://stock.xueqiu.com/v5/stock/chart/kline.json?symbol="+str(self.code)+"&begin="+str(begin)+"&period=month&type=before&count=-142&indicator=kline,pe,pb,ps,pcf,market_capital,agt,ggt,balance")
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

    def download(self,count):
        self.downloadMainReport(count)
        time.sleep(3)
        self.downloadDebtReport(count)
        time.sleep(3)
        self.downloadBenefitReport(count)
        time.sleep(3)
        self.downloadCashReport(count)
        time.sleep(3)
        self.downloadVolumeReport()
        time.sleep(3)

if __name__ == "__main__":
    DownloadReport("SZ300596").download(20)
