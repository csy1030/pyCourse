"""
    用数据库 eDict 中查找单词解释
"""
import pymysql
class SearchWord:
    def __init__(self,word=''):
        self.word = word
        self.db = pymysql.connect(
            host='localhost',
            user='root',
            port=3306,
            password='cao10300',
            database='eDict',
            charset='utf8',
        )
        self.cur = self.db.cursor()

    def search(self):
        sql = "select translation from EnWords where word = '%s'" % self.word
        self.cur.execute(sql)
        trans = self.cur.fetchone()
        if trans:
            return trans
        else:
            return 'No'

    def record(self, name, word, trans):
        # sql = "insert into search_history (name,word,translation) values ('%s','%s','%s');" %(name,word,trans)
        # self.cur.execute(sql)
        self.cur.execute("insert into search_history (name,word,translation) values ('%s','%s','%s');" %(name,word,trans))
        self.db.commit()
        self.cur.close()
        # return sql

    def get_history(self,name):
        sql = "select name,word,translation,date_format(time, '%%y-%%m-%%d %%h:%%i:%%s') from search_history where name = %s;"
        self.cur.execute(sql,name)
        data = self.cur.fetchall()
        self.cur.close()
        return data



