#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
from dbconfig import db_cfg

try:
    conn = MySQLdb.connect(host=db_cfg['host'],
                           user=db_cfg['user'],
                           passwd=db_cfg['password'],
                           db=db_cfg['database'],
                           use_unicode=True)    #不能用connection(),必须用connect() ， 关键字参数passwd 不是password, db 不是database
    cursor = conn.cursor()
    sql0 = "create table user (id varchar(20) PRIMARY KEY, name varchar(20))"
    query = "select * from user"

    id = 11
    while id < 100:
        sql = "insert into user (id,name) values ('%s','%s');" % (str(id),'user' + str(id))
        cursor.execute(sql)
        id += 1
    cursor.execute(query)
    data = cursor.fetchall()
    for m,n in data:
        print m + "    " + n

except MySQLdb.Error as e:
    print "MySQLdb Error message: %s" % e

finally:
    cursor.close()
    conn.close()
    print "close database connection"