#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector
from dbconfig import db_cfg

try:
    conn = mysql.connector.connect(host=db_cfg['host'],
                                   user=db_cfg['user'],
                                   password=db_cfg['password'],
                                   database=db_cfg['database'],
                                   use_unicode=True)    # use_unicode=True 表示使用unicode编码
    cursor = conn.cursor()
    droptab = 'DROP TABLE IF EXISTS user2'
    cursor.execute(droptab)
    createtable = 'create table user2 (id varchar(20) primary key, name varchar(20), age INTEGER)'
    cursor.execute(createtable)

    id = 0
    while id < 100:
        insertdata = "insert into user2 (id,name,age) values('%s', '%s',%d)" % (str(id), 'user' + str(id),id)
        cursor.execute(insertdata)
        id += 1
    query = 'select * from user2'
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        for col in row:
            print col,  #变量加逗号，输出时不换行
        print "\n"
except mysql.connector.Error as e:
    print "mysql error message: %s" % e
finally:
    cursor.close()
    conn.close()


