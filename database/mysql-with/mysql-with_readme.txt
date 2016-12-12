dbconfgig.py：定义数据库的配置，其本身是一个字典，包括host, user, password, database
mysql_decorate_innodb.py：定义了一个类,传入表名，可以创建表，插入数据，查询所有
mysql-exec.py: 导入模块mysql_decorate_innodb，可以用简洁的方式创建表，插入数据，查询所有。
mysql_wrap.py: 功能同mysql_decorate_innodb.py