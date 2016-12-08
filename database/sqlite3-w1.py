# -*- conding:utf-8 -*-

import sqlite3

try:
    conn = sqlite3.connect('test1.db')
    cursor = conn.cursor()
    cursor.execute('create table user ('
                   'id varchar(20) primary key, '
                   'name varchar(20))')
    cursor.execute('insert into user (id,name) values(\'1\', \'Michael\')')
    print cursor.rowcount
except sqlite3.Error as e:
    print e
finally:
    cursor.close()
    conn.commit()
    conn.close()
