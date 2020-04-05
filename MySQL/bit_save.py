"""
    二进制存储
"""

import pymysql

db = pymysql.connect(host = 'localhost',
                     user = 'root',
                     passwd = 'cao10300',
                     database = 'stu',
                     charset = 'utf8',
                     )
cur = db.cursor()

# 存储文件
with open('tesla.jpg','rb') as fd:
    data = fd.read()
try:
    sql = "insert into Images values (2,'tesla.jpg',%s);"
    cur.execute(sql,[data])
    db.commit()
except Exception as e:
    db.rollback()
    print(e)

sql = "select * from Images where filename = 'tesla.jpg';"
cur.execute(sql)
image = cur.fetchone()
with open(image[1],'wb') as fd:
    fd.write(image[2])

cur.close()
db.close()

