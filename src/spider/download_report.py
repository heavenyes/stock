import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd 
from report_type import ReportType
from main_report import MainReport
from debt_report import DebtReport
from benefit_report import BenefitReport
from cash_report import CrashReport
import json
import pymysql.cursors
from db_connection import DBConnection

class DownloadReport:

    def __init__(self,code,dir):
        self.code=code
        self.dir=dir
        self.driver = webdriver.Chrome()

        # chrome_options =Options()
        # chrome_options.add_argument('--headless')
        # self.driver = webdriver.Chrome(options=chrome_options)

    def download(self,name):
        print("download report code: %s name: %s"% (self.code,name))
        self.driver.get("http://stockpage.10jqka.com.cn/"+str(self.code)+"/finance/")
        self.driver.switch_to.frame("dataifm")
        self.driver.find_element_by_link_text(name).click()
        time.sleep(1)
        self.driver.find_element_by_id("exportButton").click()
        time.sleep(3)

    def downloadReport(self):
        self.download("主要指标")
        self.download("资产负债表")    
        self.download("利润表")  
        self.download("现金流量表")  

    def saveReport(self):
        self.downloadReport()
        for type in [ReportType.MAIN,ReportType.DEBT,ReportType.BENEFIT,ReportType.CASH]:
            self.doSaveReport(type)

    def doSaveReport(self,type:ReportType):
        
        file=self.dir+"{0}_{1}_report.xls".format(self.code,type.value[0])
        df=pd.read_excel(file)
        reportList=[]
        for column in df.columns:
            
            if column == df.columns[0]:
                continue
            
            if type==ReportType.MAIN:
                report=MainReport(self.code,df[column].tolist())
            elif type== ReportType.DEBT:
                report=DebtReport(self.code,df[column].tolist())
            elif type==ReportType.BENEFIT:
                report=BenefitReport(self.code,df[column].tolist())
            elif type==ReportType.CASH:
                report=CrashReport(self.code,df[column].tolist())
            
            reportList.append(report)
        connection = DBConnection.getConnection()
        try:
            with connection.cursor() as cursor:
                for report in reportList:
                   sql=self.getSql(type)
                   cursor.execute(sql, (report.code,report.date, self.getQuarter(report.date),json.dumps(report,default=lambda obj: obj.__dict__),json.dumps(report,default=lambda obj: obj.__dict__)))
            connection.commit()
        finally:
            connection.close()
    
    def getSql(self,type):
        if type==ReportType.MAIN :
            return "INSERT INTO `financial_report` (`stock_code`, `report_peroid`,`quarter`,`main_report`,create_time,update_time) VALUES (%s, %s,%s,%s,now(),now()) on duplicate key update main_report=%s,update_time=now()"           
        elif type==ReportType.DEBT:
            return  "INSERT INTO `financial_report` (`stock_code`, `report_peroid`,`quarter`,`debt_report`,create_time,update_time) VALUES (%s, %s,%s,%s,now(),now()) on duplicate key update debt_report=%s,update_time=now()"
        elif type==ReportType.BENEFIT:
           return  "INSERT INTO `financial_report` (`stock_code`, `report_peroid`,`quarter`,`benefit_report`,create_time,update_time) VALUES (%s, %s,%s,%s,now(),now()) on duplicate key update benefit_report=%s,update_time=now()"                
        elif type==ReportType.CASH:
           return  "INSERT INTO `financial_report` (`stock_code`, `report_peroid`,`quarter`,`cash_report`,create_time,update_time) VALUES (%s, %s,%s,%s,now(),now()) on duplicate key update cash_report=%s,update_time=now()"                
        
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


if __name__ == "__main__":
    DownloadReport(300596,"C:\\Users\\Administrator\\Downloads\\").saveReport()
