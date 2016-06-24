#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#dict
d = {
	'a':99,
	'b':44,
	'c':33
}
print('d[\'a\'] = %d' % d['a'])
print('d[\'b\'] = %d' % d['b'])
print('d[\'c\'] = %d' % d['c'])
print('d.get(\'dd\', -1) = %d' % d.get('dd',-1))



#set
s1 = set([1, 1, 2, 3, 4, 5])
print(s1)
s2 = set([2,3,4])
print(s1 & s2)
print(s1 | s2)