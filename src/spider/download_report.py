import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class DownloadReport:

    def __init__(self):
        self.driver = webdriver.Chrome()
        # chrome_options =Options()
        # chrome_options.add_argument('--headless')
        # self.driver = webdriver.Chrome(options=chrome_options)

    def download(self,code,name):
        print("download report code: %s name: %s"% (code,name))
        self.driver.get("http://stockpage.10jqka.com.cn/"+code+"/finance/")
        self.driver.switch_to.frame("dataifm")
        if name :
            self.driver.find_element_by_link_text(name).click()
        self.driver.find_element_by_id("exportButton").click()
        time.sleep(3)

    def getReport(self,code):
        self.download(code,"主要指标")
        # self.download(code,"资产负债表")    
        # self.download(code,"利润表")  
        # self.download(code,"现金流量表")  

if __name__ == "__main__":
    code = sys.argv[1]
    DownloadReport().getReport(code)
