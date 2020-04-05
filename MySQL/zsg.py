"""
    增删改练习
"""

import pymysql

db = pymysql.connect(host = 'localhost',
                     user = 'root',
                     passwd = 'cao10300',
                     database = 'stu',
                     charset = 'utf8',
                     )
cur = db.cursor()

while True:
    name = input("Name:")
    age = input("Age:")
    sex = input("m or w:")
    score = input("Score:")


    sql = "insert into class_1 (name,age,sex,score) values \
          (%s,%s,%s,%s);"
    print('%s录入成功'%name)
    try:
        cur.execute(sql,[name,age,sex,score]) # 以列表形式传入
        db.commit()
    except Exception as e:
        db.rollback()  # 失败回滚到操作之前的状态
        print("Failed:",e)