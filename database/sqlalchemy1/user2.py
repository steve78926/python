# -*- coding: utf8 -*-
#desc: MySQLdb驱动：
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User2(Base):
    __tablename__ = 'user2'

    id = Column(String(20),primary_key = True)
    name = Column(String(20))

engine = create_engine('mysql:mysqldb://salt:123456@192.168.152.132:3306/test')  #'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名',  注意：1. mysqldb不要写成MySQLdb, 2. mysqldb可以省略
DBSession = sessionmaker(bind=engine)

session = DBSession()
new_user = User2(id='7', name='Bob7')
user = session.query(User2).filter(User2.id == '7').one()
print 'type:', type(user)
print 'name:', user.name
session.close()
