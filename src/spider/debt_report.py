import time
class DebtReport:
    def __init__(self,code,name,data):
        self.code=code
        self.name=name
        self.date=time.strftime("%Y-%m-%d",time.localtime(data["report_date"]/1000))
        self.money_funds=data["currency_funds"][0]  #货币资金
        self.bills_accounts_receivable=data["ar_and_br"][0] #应收票据及应收账款
        self.bills_receivable=data["bills_receivable"][0] #应收票据
        self.accounts_receivable=data["account_receivable"][0] #应收账款
        self.prepaid_accounts=data["pre_payment"][0] #预付款项
        self.other_receivable=data["othr_receivables"][0] #其他应收款
        self.inventory=data["inventory"][0]       #存货
        self.other_current_assets=data["othr_current_assets"][0] #其他流动资产
        self.total_current_assets=data["total_current_assets"][0] #流动资产合计
        #self.long_term_investment_on_stocks=data[13] #长期股权投资
        self.investment_real_estate=data["invest_property"][0] #投资性房地产
        self.total_fixed_assets=data["fixed_asset_sum"][0] #固定资产合计(元)
        self.fixed_assets=data["fixed_asset"][0] #固定资产
        self.total_construction_in_progress=data["construction_in_process_sum"][0] #在建工程合计
        self.construction_in_progress=data["construction_in_process"][0] #在建工程
        #self.engineer_material=data[19] #工程物资
        self.intangible_assets=data["intangible_assets"][0] #无形资产
        self.goodwill=data["goodwill"][0] #商誉
        self.long_term_deferred_expense=data["lt_deferred_expense"][0] #长期待摊费用
        self.deferred_income_tax_assets=data["dt_assets"][0] #递延所得税资产
        self.other_non_current_assets = data["othr_noncurrent_assets"][0] #其他非流动性资产
        self.total_non_current_assets = data["total_noncurrent_assets"][0] #非流动资产合计
        self.total_assets=data["total_assets"][0]               #资产合计

        self.short_term_borrowing=data["st_loan"][0]       #短期借款
        self.bills_account_payable=data["bp_and_ap"][0]    #应付票据及账款
        self.bills_payable=data["bill_payable"][0]         #应付票据
        self.accounts_payable=data["accounts_payable"][0]  #应付账款
        self.accounts_received_in_advance=data["pre_receivable"][0] #预收款项
        self.payroll_payable=data["payroll_payable"][0]    #应付职工薪酬
        self.taxes_and_dues_payable=data["tax_payable"][0] #应交税费
        #self.toal_other_payables=data[35]        #其他应付款合计
        self.interest_payable=data["interest_payable"][0]  #应付利息
        #self.dividend_payable=data[37]           #应付股利
        self.other_payables=data["othr_payables"][0]             #其他应付款
        self.total_current_liabilities=data["total_current_liab"][0]      #流动负债合计
        self.long_term_borrowing=data["lt_loan"][0]            #长期借款
        self.deferred_income_tax_liabilities=data["dt_liab"][0]#递延所得税负债
        self.deferred_income_non_current_liabilities=data["noncurrent_liab_di"][0]#递延收益非流动负债
        #self.other_non_current_liabilities=data[45]      #其他非流动负债
        self.total_non_current_liabilities=data["total_noncurrent_liab"]  #非流动负债合计
        self.total_liabilities=data["total_liab"][0]      #负债合计