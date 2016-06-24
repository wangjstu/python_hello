#!/usr/bin/env python3
# -*-  coding: utf-8 -*-

# 注意:
# input()返回的是字符串
# 必须通过int()将字符串转换为整数
# 才能用于数值比较:

age = int(input('Iuput your age:'))

if age >= 18:
	print('adult, age %d' % age)
elif age >= 6:
	print('teenager, age %d' % age)
else:
	print('kid, age %d' % age)
