import pymysql.cursors
from db_connection import DBConnection
import json

connection=DBConnection.getConnection()
try:

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT trading_report FROM `trading_report` WHERE `stock_code`=%s"
        cursor.execute(sql, ('300596',))
        result = cursor.fetchall()
        pb=10
        pe=100
        pbitem=""
        peitem=""
        for item in result:
            report=json.loads(item["trading_report"])
            if report["pb"]<pb:
                pb=report["pb"]
                pbitem=item
            if report["pe"]<pe:
                pe=report["pe"]
                peitem=item
        print("min pe:{0} min pb:{1}".format(pe,pb))
        print(pbitem)
        print(peitem)
finally:
    connection.close()