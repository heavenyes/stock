class CrashReport:
    #现金流量表中英文对照
    def __init__(self,code,data):
        self.code=code
        self.date=data[0]
        # 经营活动产生的现金流量	 1. Cash Flow from Operating Activities
        self.cash_from_selling_commodities_or_offering_labor=data[2] #销售商品、提供劳务收到的现金流
        self.refund_of_tax_and_fee_received=data[3] #收到的税费返回
        self.other_cash_received_related_to_operating_activities=data[4] #收到其他与经营活动有关的现金
        self.cash_inflow_sub_total=data[5] #经营活动现金流入小计
        self.cash_paid_for_commodities_or_labor=data[6] #购买商品、接受劳务支付的现金
        self.cash_paid_to_and_for_employees=data[7] #支付给职工的薪酬
        self.taxes_and_fees_paid = data[8] #支付的各项税费
        self.other_cash_paid_related_to_operating_activities = data[9] #支付其他与经营活动有关的现金
        self.cash_out_flow_sub_total = data[10] #经营活动现金流出小计
        self.cash_flow_generated_from_operating_activities_net_amount=data[11]#经营活动产生的现金流量净额

        #投资活动产生的现金流量	    2. Cash Flow from Investing Activities
        self.cash_from_investment_withdrawal=data[13] #收回投资收到的现金
        self.cash_from_investment_income=data[14] #取得投资收益收到的现金
        self.net_cash_from_disposing_assets=data[15] #  处置固定资产、无形资产和其他长期资产所收回的现金净额
        self.other_cash_received_related_to_investing_activities=data[16] #收到其他与投资活动有关的现金
        self.cash_in_flow_sub_total=data[17] #投资活动现金流小计
        self.cash_paid_for_buying_assets=data[18]   #购建固定资产、无形资产和其他长期资产支付的现金(元)
        self.cash_paid_for_investment=data[19]   #投资支付的现金
        self.other_cash_paid_related_to_investing_activities=data[20] # 支付的其他与投资活动有关的现金
        self.cash_out_flow_sub_total=data[21]  #投资活动现金流出小计
        self.cash_flow_generated_from_investing_activities_net_amount=data[22]    #投资活动产生的现金流量净额

        #筹资活动产生的现金流量	    3. Cash Flow from Financing Activities
        self.cash_received_from_accepting_investment=data[24]  #吸收投资所收到的现金
        self.borrowings = data[26] #借款
        self.other_cash_received_related_to_financing_activities=data[27] #  收到的其它与筹资活动有关的现金
        self.financing_activities_cash_in_flow_sub_total=data[28] #现金流入小计
        self.cash_paid_for_debt=data[29]   #  偿还债务所支付的现金
        self.cash_paid_for_dividend_profit_or_interest=data[30] #分配股利、利润或偿付利息所支付的现金
        self.other_cash_paid_related_to_financing_activities=data[31] #支付的其它与筹资活动有关的现金
        self.financing_activities_cash_out_flow_sub_total=data[32]    #现金流出小计
        self.cash_flow_from_financing_activities_net_amount=data[33]  #  筹资活动产生的现金流量净额
        
        #
        self.foreign_currency_translation_gains_losses=data[34]   #汇率变动对现金的影响
        self.net_increase_of_cash_and_cash_equivalents=data[35]   #现金及现金等价物净增加额

        #补充资料：	    Supplementary Schedule： 　	　
        #现金流量附表项目	    Indirect Method 　	　
        #1、将净利润调节为经营活动现金流量	    1. Convert net profit to cash flow from operating activities


