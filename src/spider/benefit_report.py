class BenefitReport:
    def __init__(self,code,data):
        self.code=code
        self.date=data[0]
        self.total_revenue=data[1] #营业总收入
        self.operating_revenue=data[2] #营业收入
        self.total_operating_costs=data[3]  #营业总成本
        self.operating_costs = data[4] #营业成本
        self.business_taxes_and_surcharges=data[5] #营业税金及附加
        self.marketing_costs=data[6]    #销售费用
        self.managing_costs =data[7]   #管理费用
        self.research_and_development_expense=data[8] #研发费用
        self.financing_costs=data[9]    #财务费用
        self.interest_expense=data[10]  #利息费用
        self.interest_revenue=data[11]  #利息收入
        self.assets_devaluation=data[12]#资产减值损失
        self.investment_income=data[13] #投资收益
        self.partner_company_income=data[14] #联营企业投资收益
        self.disposal_assets_income=data[15]#资产处置收益
        self.other_income=data[16]  #其他收益
        self.sales_profit=data[17]  #营业利润
        self.non_business_income=data[18] #营业外收入
        self.non_business_expenditure=data[20] #营业外支出
        self.total_profit=data[22] #利润总额
        self.income_tax_expense=data[24] #所得税费用
        self.net_profit=data[25]    #净利润
        self.recurrent_net_profit=data[29] #扣非净利润

