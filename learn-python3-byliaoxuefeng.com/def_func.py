#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#在python-cli下面可以用命令：from abstest import my_abs 导入函数到cli下，abstest为文件名(abstest.py)，函数名是my_abs

import math

def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

def move(x, y, step, angle=0):
	nx = x + step + math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny

n = my_abs(-20)
print(n)

x, y = move(100, 100, 60, math.pi / 6)
print(x, ',',y)

# TypeError: bad operand type:
# my_abs('123')