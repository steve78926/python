#-*- coding: utf8 -*-

from contextlib import contextmanager
import MySQLdb
from dbconfig import db_cfg                     #dbconfig是数据库配置模块，db_cfg是数据库配置字典

class db_handler(object):

    @contextmanager                               #contextmanager装饰器是上下文管理，作用是将被装饰的函数变为可以with的对象
    def _get_serv(self):
        conn = MySQLdb.connect(host=db_cfg['host'],
                               user=db_cfg['user'],
                               passwd=db_cfg['password'],
                               db=db_cfg['database'],
                               use_unicode=True)
        cursor = conn.cursor()                  #生成游标
        try:
            yield cursor
        except MySQLdb.Error,e:
            print "mysql error message:%s" % str(e)
        finally:
            cursor.close()
            print "cursor close"
            conn.close()
            print "conn close"


    def insert(self,data):
        with self._get_serv() as cursor:                    #with 在其下的代码执行前进行准备工作，with之内的代码执行完成，再执行后续的清理工作
            sql = '''insert into user (id,name) values (%s,%s)'''     #表名不能带引号，如'user' 会报mysql语法错
            cursor.execute(sql,(data['id'],data['name']))

    def query(self,tabname,name):
        with self._get_serv() as cursor:
            sql = "select * from %s where name = '%s'" % (tabname,name)         #表名与其他参数可以这样写
            cursor.execute(sql)
            retdata = cursor.fetchall()
            for row in retdata:
                for col in row:
                    print col,                          # 在python 2.x里逗号表示不换行，即一条数据记录按行打印, 不能使用 print "%s," % col 这种方式
                print "\n"


data = {'id':'3','name':'mike3'}
db = db_handler()
db.insert(data)
db.query('user','mike3')
