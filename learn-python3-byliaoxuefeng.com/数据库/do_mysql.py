#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########## prepare ##########

# install mysql-connector-python:
# pip3 install mysql-connector-python-rf --allow-external mysql-connector-python #基本不成功
#下面的才有用
# wget https://cdn.mysql.com/Downloads/Connector-Python/mysql-connector-python-2.1.3.zip
# unzip mysql-connector-python-2.1.3.zip
# cd mysql-connector-python-2.1.3
# python setup.py install

import mysql.connector

# change root password to yours:
conn = mysql.connector.connect(user='root', password='vagrant', database='test')

cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))
print('rowcount =', cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()