import pymysql.cursors

class DBConnection:
    
    @staticmethod
    def getConnection():
        return pymysql.connect(host='localhost',
                             user='root',
                             db='stock',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)