#-*- coding: utf8 -*-

import mysql.connector
from dbconfig import db_cfg

conn = mysql.connector.connect(host=db_cfg['host'],
                               user=db_cfg['user'],
                               password=db_cfg['password'],
                               database=db_cfg['database'],
                               use_unicode=True)