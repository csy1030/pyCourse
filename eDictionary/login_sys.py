"""
    注册 登录数据库
"""

import pymysql,sys

class LoginSys:
    def __init__(self,database,user_name,password = '0'):
        self.database = database
        self.user_name = user_name
        self.password = password
        self.db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    port = 3306,
    password = 'cao10300',
    database = 'eDict',
    charset = 'utf8',
)
        self.cur = self.db.cursor()

    # 判断用户名是否可用
    def is_avail(self):
        sql = "select * from %s where user_name = '%s';" % (self.database,self.user_name)
        self.cur.execute(sql)
        return False if self.cur.fetchall() else True

    def register(self):
        sql = "insert into %s (user_name,password) values ('%s','%s');"% (self.database,self.user_name,self.password)
        try:
            self.cur.execute(sql)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()

            return e

    def login(self):
        sql = "select * from %s where (user_name = '%s') and (password = '%s');" %(self.database,self.user_name,self.password)
        self.cur.execute(sql)
        return True if self.cur.fetchone() else False


if __name__ == '__main__':

    while True:
        handle = input("注册r/登录l/退出q?")
        if handle == 'r':
            while True:
                name = input("User name:")
                ls = LoginSys('user',name)
                if ls.is_avail():
                    pwd = input("Password:")
                    ls = LoginSys('user',name, pwd)
                    ls.register()
                    break
                else:
                    print("用户名已存在,请重新输入...")

        elif handle == 'l':
            name = input("User name:")
            pwd = input("Password:")
            ls = LoginSys('user',name,pwd)
            print("登录成功!") if ls.login() else print("用户名或密码错误..")

        elif handle == 'q':
            sys.exit("退出")
