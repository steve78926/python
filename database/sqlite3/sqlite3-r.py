# -*- coding: utf-8 -*-
import database.sqlite3

conn = database.sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('select * from user where id=?', ('1',))
values = cursor.fetchall()
print values
cursor.close()
conn.close()