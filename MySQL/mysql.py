"""
    pymysql 基本流程演示
"""

import pymysql
db = pymysql.connect(host = 'localhost',
                     user = 'root',
                     port = 3306,
                     password = 'cao10300',
                     database = 'stu',
                     charset = 'utf8')
# 获取游标
cur = db.cursor()

# 数据操作 填入SQL语句
cur.execute("insert into class_1 values (6,'James',27,'m',79);")

# 将数据提交到数据库
db.commit()




# 关闭游标和数据库连接
cur.close()
db.close()
