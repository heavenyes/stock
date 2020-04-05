from enum import Enum
class ReportType(Enum):
    MAIN="main",  #主要指标
    DEBT="debt",   #资产负债表
    BENEFIT="benefit",  #利润表
    CASH="cash",     #现金流量 