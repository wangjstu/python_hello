#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#打印list:
print('list=======')
names = ['wang', 'li', 'zhang']
for name in names:
	print(name)

#打印数字
for x in range(10):
	print(x)


print('\n\n\n')



#计算1+2+3+...+100
print('while=======')
sum = 0
n = 1
while n<=100:
	sum= sum+n
	n=n+1
print(sum)

#计算1*2*3*...*100:
acc = 1
n = 1
while n<=100:
	acc = acc*n
	n = n+1
print(acc)
