import pymysql.cursors
from db_connection import DBConnection
import json
import pandas as pd
import itertools
from collections import defaultdict

class BusinessFeatureAnalysis:
    def __init__(self,code):
        self.code=code

    def queryData(self):
        connection=DBConnection.getConnection()
        try:

            with connection.cursor() as cursor:
                sql = "SELECT * FROM `financial_report` WHERE `stock_code`=%s order by report_peroid desc"
                cursor.execute(sql, (self.code,))
                result = cursor.fetchall()
                reportList=[]
                for item in result:
                    reportList.append(item)
                # sql="select * from financial_report where stock_code=%s order by report_peroid desc limit 1"
                # cursor.execute(sql,(self.code,))
                # result=cursor.fetchone()

                # if reportList[:1][0]["report_peroid"] != result["report_peroid"] :
                #     reportList.insert(0,result)
            return reportList
        finally:
            connection.close()

    def output(self):

        peroid=[]
        revenu_growth_rate=[] #营收增速
        profit_growth_rate=[]
        recurrent_net_profit_growth_rate=[] #扣非净利润增速
        gross_profit_ratio=[] #毛利率
        four_fee_ratio=[]     #四费
        marketing_costs_ratio=[] #销售费用率
        managing_costs_ratio=[]  #管理费用率
        research_and_development_expense_ratio=[] #研发费用率
        financing_costs_ratio=[]    #财务费用率
        leverage_ratio=[] #资产负债率

        bills_accounts_receivable_ratio=[] #应收账款占收入
        days_sales_of_outstanding=[] #应收账款周转天数

        fixed_assets_ratio=[]  #固定资产比重
        roe=[]
        net_profit_margin=[] #净利率
        total_assets_turnover=[] #总资产周转率
        financial_leverage=[]   #财务杠杆

        total_assets_growth_rate=[] #总资产周转率
        
        cash_revenu_ratio=[] #经营性现金流/收入
        cash_profit_ratio=[] #经营性现金流/利润

        reportAllList=self.queryData()
        reportMap = {report["report_peroid"]:report for report in reportAllList}
        reportList= list(filter(lambda x: x["quarter"] ==4, reportAllList)) #取年度
        reportList.insert(0,reportAllList[:1][0])

        for report in reportList:
            peroid.append(report["report_peroid"])
            main_report=json.loads(report["main_report"])
            revenu=main_report["revenu"]
            revenu_growth_rate.append(main_report["revenu_growth_rate"])
            profit_growth_rate.append(main_report["profit_growth_rate"])
            recurrent_net_profit_growth_rate.append(main_report["recurrent_net_profit_growth_rate"])
            gross_profit_ratio.append(main_report["gross_profit_ratio"])
            leverage_ratio.append(main_report["leverage_ratio"])
            days_sales_of_outstanding.append(main_report["days_sales_of_outstanding"])

            roe.append(main_report["roe"])
            net_profit_margin.append(main_report["net_profit_margin"])

            benefit_report=json.loads(report["benefit_report"])

            marketing_costs=self.getNum(benefit_report["marketing_costs"])
            managing_costs=self.getNum(benefit_report["managing_costs"])
            research_and_development_expense=self.getNum(benefit_report["research_and_development_expense"])
            financing_costs=self.getNum(benefit_report["financing_costs"])

            four_fee_ratio.append(self.percentage(marketing_costs+managing_costs+research_and_development_expense+financing_costs,revenu))
            marketing_costs_ratio.append(self.percentage(marketing_costs,revenu))
            managing_costs_ratio.append(self.percentage(managing_costs,revenu))
            research_and_development_expense_ratio.append(self.percentage(research_and_development_expense,revenu))
            financing_costs_ratio.append(self.percentage(financing_costs,revenu))


            debt_report=json.loads(report["debt_report"])
            bills_accounts_receivable_ratio.append(self.percentage(self.getNum(debt_report["bills_accounts_receivable"]),revenu))
            fixed_assets_ratio.append(self.percentage(self.getNum(debt_report["total_fixed_assets"]),self.getNum(debt_report["total_assets"])))
            financial_leverage.append(self.round(1/(1-(self.getNum(debt_report["total_liabilities"])/self.getNum(debt_report["total_assets"])))))

            #总资产周转率
            total_assets_turnover.append(self.get_total_assets_turnover(report["report_peroid"],reportMap)) 
        
            #total_assets_growth_rate
            before_peroid = self.getBeforeYear(report["report_peroid"])
            if reportMap.get(before_peroid,None) :
                before_debt_report=json.loads(reportMap[before_peroid]["debt_report"])
                before_peroid_total_asset = self.getNum(before_debt_report["total_assets"])
                current_total_asset = self.getNum(debt_report["total_assets"])
                total_assets_growth_rate.append(self.percentage(current_total_asset-before_peroid_total_asset,before_peroid_total_asset))
            else:
                total_assets_growth_rate.append("--")  
            #
            cash_report = json.loads(report["cash_report"])     
            cash_revenu_ratio.append(self.percentage(self.getNum(cash_report["cash_from_selling_commodities_or_offering_labor"]),revenu))
            cash_profit_ratio.append(self.percentage(self.getNum(cash_report["cash_flow_generated_from_operating_activities_net_amount"]),self.getNum(main_report["profit"])))

        print(peroid)
        print(total_assets_growth_rate)
        dict = {
            '报告期':peroid,
            'roe':roe,
            '净利率':net_profit_margin,
            '总资产周转率':total_assets_turnover,
            '财务杠杆':financial_leverage,
            '营收增速':revenu_growth_rate,
            '利润增速':profit_growth_rate,
            '扣非净利润增速': recurrent_net_profit_growth_rate,
            '毛利率':gross_profit_ratio,
            '四项费用率':four_fee_ratio,
            '销售费用率':marketing_costs_ratio,
            '管理费用率':managing_costs_ratio,
            '研发费用率':research_and_development_expense_ratio,
            '财务费用率':financing_costs_ratio,
            '资产负债率':leverage_ratio,
            '应收账款占收入':bills_accounts_receivable_ratio,
            '应收账款周转天数':days_sales_of_outstanding,
            '固定资产占总资产比重':fixed_assets_ratio,
            '总资产增长率':total_assets_growth_rate,
            '销售收现比':cash_revenu_ratio,
            '经营性现金流/净利润':cash_profit_ratio
            }
 
        # creating a dataframe from a dictionary 
        df = pd.DataFrame(dict)
        df.to_csv("{0}生意特性.csv".format(self.code),index=False)

    
    def get_total_assets_turnover(self,peroid,reportMap):
        year =peroid[:4]
        revenu=0
        total_asset=0
        num=0

        for report in reportMap.values():
            if report["report_peroid"][:4]== year:
                if report["main_report"] != None  and report["debt_report"]!=None:
                    main_report=json.loads(report["main_report"])
                    if self.getNum(main_report["revenu"])>revenu :
                        revenu= self.getNum(main_report["revenu"])
                    debt_report=json.loads(report["debt_report"])
                    total_asset=total_asset+self.getNum(debt_report["total_assets"])
                    num=num+1
        
        return self.round(revenu/(total_asset/num))

    def getBeforeYear(self,peroid):
        before=int(peroid[:4])-1
        return str(before)+peroid[4:]

    def getElement(self,list,index):
        try:
            return list[index]
        except Exception:
            return None

    def percentage(self,num,sum):
        return format(num/sum,'.2%')
    
    def round(self,num):
        return round(num,3)

    def getNum(self,num):
        try:
            return float(num)
        except Exception:
            return 0

if __name__=="__main__":
    # reportList = BusinessFeatureAnalysis(300596).queryData()
    # reportMap = {report["report_peroid"]:report for report in reportList}
    # print(reportMap)
    BusinessFeatureAnalysis(300596).output()