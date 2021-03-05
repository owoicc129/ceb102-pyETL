import pandas as pd
import pymysql

host = 'localhost'
port = 3306
user = 'root'
passwd = '2482'
db = 'TESTDB'
charset = 'utf8mb4'

# 建立連線
conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
print('Successfully connected!')

# 建立游標
cursor = conn.cursor()

df=pd.read_csv('./104_jobList.csv')
for x,i in enumerate(df.values):
    a=str(x)+",'"+i[0]+"','"+i[1]+"','"+i[2]+"'"


    sql = 'INSERT INTO job104 (id,公司名稱,職位名稱,工作內容)'+' VALUES('+a
    sql = sql + ');'
    # print(sql)
    cursor.execute(sql)


conn.commit()
cursor.close()
conn.close()
