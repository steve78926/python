#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

#host = '192.168.152.132'
host = '192.168.64.157'
user = 'salt'
passwd = '123456'
db = 'test'
try:
    conn = MySQLdb.connect(host=host, user=user, passwd=passwd,db=db, use_unicode=True)    #不能用connection(),必须用connect() ， 关键字参数passwd 不是password, db 不是database
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