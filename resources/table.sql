-- mysql version >5.7.8

CREATE DATABASE `stock` /*!40100 DEFAULT CHARACTER SET utf8 */

CREATE TABLE `financial_report` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '物理主键',
  `stock_code` varchar(32)   DEFAULT NULL COMMENT '股票代码',
  `stock_name` varchar(32)  DEFAULT NULL COMMENT '股票名称',
  `report_peroid` varchar(12) DEFAULT NULL COMMENT '报告期,yyyy-MM-dd',
  `quarter` int(11) DEFAULT NULL COMMENT '季度:1,2,3,4',
  `main_report` json DEFAULT NULL COMMENT '主要指标',
  `debt_report` json DEFAULT NULL COMMENT '资产负债表',
  `benefit_report` json DEFAULT NULL COMMENT '利润表',
  `cash_report` json DEFAULT NULL COMMENT '现金流量表',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `stock_code` (`stock_code`,`report_peroid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8


CREATE TABLE `trading_report` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '物理主键',
  `stock_code` varchar(32)  DEFAULT NULL COMMENT '股票代码',
  `stock_name` varchar(32)  DEFAULT NULL COMMENT '股票名称',
  `report_peroid` varchar(12)  DEFAULT NULL COMMENT '报告期,yyyy-MM-dd',
  `trading_report` json DEFAULT NULL COMMENT '主要指标',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `stock_code` (`stock_code`,`report_peroid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;