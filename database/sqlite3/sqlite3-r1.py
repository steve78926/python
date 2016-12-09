# -*- coding: utf-8 -*-

import database.sqlite3

try:
    conn = database.sqlite3.connect('test1.db')
    cursor = conn.cursor()
    cursor.execute('select * from user where id=?',('1',))
    print cursor.fetchall()
except database.sqlite3.Error as e:
    print 'connect test1.db error, message: %s' % e
finally:
    cursor.close()
    conn.commit()
    conn.close()

