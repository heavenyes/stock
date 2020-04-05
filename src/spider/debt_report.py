class DebtReport:
    def __init__(self,code,data):
        self.code=code
        self.date=data[0]
        self.money_funds=data[2]  #货币资金
        self.bills_accounts_receivable=data[3] #应收票据及应收账款
        self.bills_receivable=data[4] #应收票据
        self.accounts_receivable=data[5] #应收账款
        self.prepaid_accounts=data[6] #预付款项
        self.other_receivable=data[7] #其他应收款
        self.inventory=data[9]        #存货
        self.other_current_assets=data[10] #其他流动资产
        self.total_current_assets=data[11] #流动资产合计
        self.long_term_investment_on_stocks=data[13] #长期股权投资
        self.investment_real_estate=data[14] #投资性房地产
        self.total_fixed_assets=data[15] #固定资产合计(元)
        self.fixed_assets=data[16] #固定资产
        self.total_construction_in_progress=data[17] #在建工程合计
        self.construction_in_progress=data[18] #在建工程
        self.engineer_material=data[19] #工程物资
        self.intangible_assets=data[20] #无形资产
        self.goodwill=data[21] #商誉
        self.long_term_deferred_expense=data[22] #长期待摊费用
        self.deferred_income_tax_assets=data[23] #递延所得税资产
        self.other_non_current_assets = data[24] #其他非流动性资产
        self.total_non_current_assets = data[25] #非流动资产合计
        self.total_assets=data[26]               #资产合计

        self.short_term_borrowing=data[28]       #短期借款
        self.bills_account_payable=data[29]      #应付票据及账款
        self.bills_payable=data[30]              #应付票据
        self.accounts_payable=data[31]           #应付账款
        self.accounts_received_in_advance=data[32] #预收款项
        self.payroll_payable=data[33]            #应付职工薪酬
        self.taxes_and_dues_payable=data[34]     #应交税费
        self.toal_other_payables=data[35]        #其他应付款合计
        self.interest_payable=data[36]           #应付利息
        self.dividend_payable=data[37]           #应付股利
        self.other_payables=data[38]             #其他应付款
        self.total_current_liabilities=data[40]      #流动负债合计
        self.long_term_borrowing=data[42]            #长期借款
        self.deferred_income_tax_liabilities=data[43]#递延所得税负债
        self.deferred_income_non_current_liabilities=data[44]#递延收益非流动负债
        self.other_non_current_liabilities=data[45]      #其他非流动负债
        self.total_non_current_liabilities=data[46]      #非流动负债合计
        self.total_liabilities=data[47]                  #负债合计