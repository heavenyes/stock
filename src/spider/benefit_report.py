import time
class BenefitReport:
    def __init__(self,code,name,data):
        self.code=code
        self.name=name
        self.date=time.strftime("%Y-%m-%d",time.localtime(data["report_date"]/1000))
        self.total_revenue=data["total_revenue"][0] #营业总收入
        self.operating_revenue=data["revenue"][0] #营业收入
        self.total_operating_costs=data["operating_costs"][0]  #营业总成本
        self.operating_costs = data["operating_cost"][0] #营业成本
        self.business_taxes_and_surcharges=data["operating_taxes_and_surcharge"][0] #营业税金及附加
        self.marketing_costs=data["sales_fee"][0]    #销售费用
        self.managing_costs =data["manage_fee"][0]   #管理费用
        self.research_and_development_expense=data["rad_cost"][0] #研发费用
        self.financing_costs=data["financing_expenses"][0]    #财务费用
        self.interest_expense=data["finance_cost_interest_fee"][0]  #利息费用
        self.interest_revenue=data["finance_cost_interest_income"][0]  #利息收入
        self.assets_devaluation=data["asset_impairment_loss"][0]#资产减值损失
        self.investment_income=data["invest_income"][0] #投资收益
        self.partner_company_income=data["invest_incomes_from_rr"][0] #联营企业投资收益
        self.disposal_assets_income=data["asset_disposal_income"][0]#资产处置收益
        self.other_income=data["other_income"][0]  #其他收益
        self.sales_profit=data["op"][0]  #营业利润
        self.non_business_income=data["non_operating_income"][0] #营业外收入
        self.non_business_expenditure=data["non_operating_payout"][0] #营业外支出
        self.total_profit=data["profit_total_amt"][0] #利润总额
        self.income_tax_expense=data["income_tax_expenses"][0] #所得税费用
        self.net_profit=data["net_profit"][0]    #净利润
        self.recurrent_net_profit=data["net_profit_after_nrgal_atsolc"][0] #扣非净利润

