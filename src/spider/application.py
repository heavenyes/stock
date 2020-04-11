from download_report import DownloadReport
from business_feature_analysis import BusinessFeatureAnalysis

if __name__ == "__main__":
    code = "SZ002706"
    DownloadReport(code).download(20)
    BusinessFeatureAnalysis(code).output()
