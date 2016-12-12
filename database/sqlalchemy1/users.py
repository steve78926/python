#-*- coding:utf8 -*-
#desc: mysqlconnector驱动
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

engine = create_engine('mysql+mysqlconnector://salt:123456@192.168.152.132:3306/test')  #'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
DBsession = sessionmaker(bind=engine)

session = DBsession()
new_user = User(id='8',name='Bob8')
session.add(new_user)
session.commit()
user = session.query(User).filter(User.id=='8').one()
print 'type:', type(user)
print 'name:',user.name
session.close()
