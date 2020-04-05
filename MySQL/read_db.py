"""
    读数据库操作
"""
import pymysql

db = pymysql.connect(host = 'localhost',
                     user = 'root',
                     passwd = 'cao10300',
                     database = 'stu',
                     charset = 'utf8',
                     )
cur = db.cursor()

sql = "select * from class_1 where age = 22;"

# 执行语句 cur 拥有了查询结果
cur.execute(sql)
one_row = cur.fetchone()
print(one_row)

cur.close()
db.close()