import pandas as pd 
from report_type import ReportType
from main_report import MainReport
from debt_report import DebtReport
from benefit_report import BenefitReport
from crash_report import CrashReport
import json
import pymysql.cursors


class ReportManager:
    
    def __init__(self,dir,code):
        self.dir = dir
        self.code = code

    def getConnection(self):
        return pymysql.connect(host='localhost',
                             user='root',
                             db='stock',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    def getFile(self,type:ReportType):
        return self.dir+"{0}_{1}_report.xls".format(self.code,type.value[0])

    def getReport(self,type:ReportType):
        file=self.getFile(type)
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
       
        return reportList  
    
        
    def saveReport(self,type:ReportType):
        reportList=self.getReport(type)
        connection = self.getConnection()
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
            return "INSERT INTO `financial _report` (`stock_code`, `report_peroid`,`quarter`,`main_report`,create_time,update_time) VALUES (%s, %s,%s,%s,now(),now()) on duplicate key update main_report=%s,update_time=now()"           
        elif type==ReportType.DEBT:
            return  "INSERT INTO `financial _report` (`stock_code`, `report_peroid`,`quarter`,`debt_report`,create_time,update_time) VALUES (%s, %s,%s,%s,now(),now()) on duplicate key update debt_report=%s,update_time=now()"
        elif type==ReportType.BENEFIT:
           return  "INSERT INTO `financial _report` (`stock_code`, `report_peroid`,`quarter`,`benefit_report`,create_time,update_time) VALUES (%s, %s,%s,%s,now(),now()) on duplicate key update benefit_report=%s,update_time=now()"                
        elif type==ReportType.CASH:
           return  "INSERT INTO `financial _report` (`stock_code`, `report_peroid`,`quarter`,`cash_report`,create_time,update_time) VALUES (%s, %s,%s,%s,now(),now()) on duplicate key update cash_report=%s,update_time=now()"                
        
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
    reportManager =  ReportManager("C:\\Users\\Administrator\\Downloads\\",300596)
    reportManager.saveReport(ReportType.MAIN)
    reportManager.saveReport(ReportType.DEBT)
    reportManager.saveReport(ReportType.BENEFIT)
    reportManager.saveReport(ReportType.CASH)
