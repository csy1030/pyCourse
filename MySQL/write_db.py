"""
    写数据库练习
"""
import pymysql

db = pymysql.connect(host = 'localhost',
                     user = 'root',
                     passwd = 'cao10300',
                     database = 'stu',
                     charset = 'utf8',
                     )
cur = db.cursor()

try:
    sql = "insert into interest values \
        (5,'Amy','draw,sing','A','2220','1565235','good')"
    cur.execute(sql)
    print('1')
    # 修改操作
    sql = "update interest set price = 6666 \
    where name = 'Frank';"
    cur.execute(sql)
    print('1')
    # 删除操作
    sql = "delete from class_1 where score < 20;"
    cur.execute(sql)

    db.commit()
except Exception as e:
    db.rollback()
    print(e)

