from selenium import webdriver
from requests_html import HTML

driver = webdriver.Chrome()
driver.get("https://xueqiu.com/S/SZ300596")
driver.get("https://stock.xueqiu.com/v5/stock/chart/kline.json?symbol=SZ300596&begin=1586174563037&period=month&type=before&count=-142&indicator=kline,pe,pb,ps,pcf,market_capital,agt,ggt,balance")
print(driver.page_source)

html=HTML(html=driver.page_source)

print(html.find("pre",first=True).text)