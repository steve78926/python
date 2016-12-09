# -*- coding: utf-8 -*-
import mysql.connector
from mysql_conn import conn

cursor = conn.cursor()
droptab = 'DROP TABLE IF EXISTS student'
cursor.execute(droptab)
createtab = "create table student (id varchar(10) primary key, name varchar(20), age int)"
cursor.execute(createtab)

id = 0
while id < 100:
    insdata = "insert into student(id, name, age) values ('%s', '%s', '%d')" % ('000' + str(id),  'student' + str(id), id+3)
    cursor.execute(insdata)
    #conn.commit()
    id += 1
query = 'select * from student limit 10'
try:
    cursor.execute(query)
    rows = cursor.fetchall()
except mysql.connector.Error,e:
    try:
        print 'mysql error: [%d]: %s' % (e.args[0], e.args[1])
    except IndexError:
        print "mysql connector error: %s" % str(e)

print "%s\t\t%s\t\t\t%s" % ('id', 'name', 'age')
for id,name,age in rows:
    print "%s\t\t%s\t\t%s" % (id, name, age)
cursor.close()
conn.close()
