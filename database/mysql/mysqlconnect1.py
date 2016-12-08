#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector

host = '192.168.152.132'
user = 'salt'
password = '123456'
database='test'

try:
    conn = mysql.connector.connect(host=host,user=user,password=password,database=database,use_unicode=True)    # use_unicode=True 表示使用unicode编码
    cursor = conn.cursor()
    #createtable = 'create table user2 (id varchar(20) primary key, name varchar(20))'
    deldata = 'delete from user2'
    #cursor.execute(createtable)
    cursor.execute(deldata)
    id = 0
    while id < 100:
        insertdata = "insert into user2 (id,name) values('%s', '%s')" % (str(id), 'user' + str(id))
        cursor.execute(insertdata)
        id += 1
    query = 'select * from user2'
    cursor.execute(query)
    data = cursor.fetchall()
    for id, name in data:
        print id + '    '+ name
except mysql.connector.Error as e:
    print "mysql error message: %s" % e
finally:
    cursor.close()
    conn.close()


