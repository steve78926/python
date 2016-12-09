# -*- coding:utf8 -*-

import database.sqlite3
conn = database.sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id,name) values (\'1\', \'Michael\')')
cursor.rowcount
cursor.close()
conn.commit()
conn.close()