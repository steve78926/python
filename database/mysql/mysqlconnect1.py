#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector

#host = '192.168.152.132'
host = '192.168.64.157'
user = 'salt'
password = '123456'
database='test'

try:
    conn = mysql.connector.connect(host=host,user=user,password=password,database=database,use_unicode=True)    # use_unicode=True 表示使用unicode编码
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
            print "%s, " % col
        print "\n"
except mysql.connector.Error as e:
    print "mysql error message: %s" % e
finally:
    cursor.close()
    conn.close()


