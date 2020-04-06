from download_report import DownloadReport
from download_volume import DownloadVolume
from business_feature_analysis import BusinessFeatureAnalysis

if __name__ == "__main__":
    code = "002027"
    DownloadReport(code,"C:\\Users\\Administrator\\Downloads\\").saveReport()
    DownloadVolume(code).download()
    BusinessFeatureAnalysis(code).output()
