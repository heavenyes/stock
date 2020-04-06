import time
class MainReport:

     def __init__(self,code,name,data):
        self.code=code
        self.name=name
        self.date=time.strftime("%Y-%m-%d",time.localtime(data["report_date"]/1000))
        self.operating_revenue=data["total_revenue"][0] #营业收入
        self.operating_revenue_growth_rate=data["operating_income_yoy"][0]     #营收增长率
        self.net_profit=data["net_profit_atsopc"][0] #净利润
        self.net_profit_growth_rate=data["net_profit_atsopc_yoy"][0] #净利润同比增长
        self.recurrent_net_profit=data["net_profit_after_nrgal_atsolc"][0]  # 扣非净利润
        self.recurrent_net_profit_growth_rate=data["np_atsopc_nrgal_yoy"][0] # 扣非净利润同比增长

        self.roe=data["avg_roe"][0]  #净资产收益率
        self.roa=data["net_interest_of_total_assets"][0]  #总资产报酬率

        self.net_profit_margin=data["net_selling_rate"][0]        #净利率
        self.gross_profit_ratio=data["gross_selling_rate"][0]      #毛利率
        
        self.leverage_ratio=data["asset_liab_ratio"][0]    #资产负债率
        self.financial_leverage=data["equity_multiplier"][0] #权益乘数
        self.current_ratio=data["current_ratio"][0]        #流动比率
        self.quick_ratio=data["quick_ratio"][0]            #速动比率


        #运营能力 各项财务指标解释 https://wiki.mbalib.com/wiki/
        self.days_sales_of_inventory=data["inventory_turnover_days"][0] # 存货周转天数
        self.days_sales_of_outstanding=data["receivable_turnover_days"][0]  # 应收账款周转天数
        self.cash_conversion_cycle=data["cash_cycle"][0]  #现金循环周期
        self.operating_cycle=data["operating_cycle"][0]            # 营业周期
        self.total_assets_turnover=data["total_capital_turnover"][0] #总资产周转率
        self.inventory_turnover=data["inventory_turnover"][0]      # 存货周转率
        self.receivables_turnover_ratio=data["account_receivable_turnover"][0] #应收账款周转率
        self.account_payable_turnover_rate=data["accounts_payable_turnover"][0]#应付账款周转率
        self.current_assets_turnover=data["current_asset_turnover_rate"][0]     #流动资产周转率
        self.fixed_asset_turnover=data["fixed_asset_turnover_ratio"][0]  #固定资产周转率
        