class MainReport:

     def __init__(self,code,data):
        self.code=code
        self.date=data[0]              
        self.profit=data[1]
        self.profit_growth_rate=data[2]
        self.recurrent_net_profit=data[3]  # 扣非净利润
        self.recurrent_net_profit_growth_rate=data[4]
        self.revenu=data[5]
        self.revenu_growth_rate=data[6]
        self.net_profit_margin=data[12]        #净利率
        self.gross_profit_ratio=data[13]      #毛利率
        self.roe=data[14]
        self.operating_cycle=data[16]            #营业周期
        self.inventory_turnover=data[17]      #存货周转率
        self.days_sales_of_inventory=data[18] #存货周转天数
        self.days_sales_of_outstanding=data[19]  #应收账款周转天数
        self.leverage_ratio=data[24]             #资产负债率