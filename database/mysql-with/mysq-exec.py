from mysql_decorate_innodb import MySQLhandler

data = {'id':'004','name':'student004','age':14}
db = MySQLhandler('student_out')
db.insert(data)
db.query()
