# -*- coding:utf8 -*-

from contextlib import contextmanager
from dbconfig import db_cfg
import MySQLdb



class MySQLhandler(object):

    def __init__(self,tabname):
        self.tabname = tabname

    @contextmanager
    def db_handler(self,commit=False):
        try:
            conn = MySQLdb.connect(host=db_cfg['host'],       #注意数据库的连接conn必须包含在db_handler里，否则mysql.exec.py里的create, insert,query函数不能同时执行，报错close a closed connection
                       user=db_cfg['user'],
                       passwd=db_cfg['password'],
                       db = db_cfg['database'],
                       use_unicode = True)
            cursor = conn.cursor()
            yield cursor
        except MySQLdb.Error,e:
            print "MySQL error: %s" % str(e)
        else:                                   #如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
            if commit:
                cursor.execute('commit')
        finally:
            cursor.close()
            conn.close()

    def create(self):
        with self.db_handler() as cursor:
            droptab = 'DROP TABLE IF EXISTS %s' % self.tabname
            creattab = "create table %s (id varchar(10) primary key,name varchar(20), age int) engine=innodb" % self.tabname
            cursor.execute(droptab)
            cursor.execute(creattab)

    def insert(self,data):
        with self.db_handler(commit=True) as cursor:
            sql = "insert into " + self.tabname + "(id, name,age) values(%s, %s, %s)"    #注意: age在mysql表里定义的是int, 但data字典里age是字符串, 且这里也是用%s表示，但最终并不影响插入数据
            cursor.execute(sql,(data['id'], data['name'], data['age']))    #虽然age在mysql里定义为int, 但insert into student (id,name,age) values ('007','student4','2980'); 这条语句执行正常

    def query(self):
        with self.db_handler() as cursor:
            sql = 'select * from %s' % self.tabname
            cursor.execute(sql)
            res = cursor.fetchall()
            for row in res:
                for col in row:
                    print col,
                print "\r\n"
