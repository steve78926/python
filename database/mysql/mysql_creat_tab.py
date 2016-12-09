# -*- coding: utf-8 -*-
import mysql.connector
from mysql_conn import conn
tabname = 'student_in'

cursor = conn.cursor()
droptab = 'DROP TABLE IF EXISTS %s' % tabname
cursor.execute(droptab)
createtab = "create table %s (id varchar(10) primary key, name varchar(20), age int) engine=innodb" % tabname
cursor.execute(createtab)

id = 0
while id < 10:
    insdata = "insert into %s (id, name, age) values ('%s', '%s', '%d')" % (tabname,'000' + str(id),  'student' + str(id), id+3)
    cursor.execute(insdata)
    conn.commit()
    id += 1
query = 'select * from student limit 10'

cursor.close()
conn.close()
