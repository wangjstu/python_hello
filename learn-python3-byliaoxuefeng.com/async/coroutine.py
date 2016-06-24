#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def consumer():
	r = 'a'
	while True:
		print('While True:')
		n = yield r     #yield == 1:return r,sleeping...;2:awaking to assiged sended to n
		if not n:
			print('Here is not n:')
			return
		print('[CONSUMER] Consuming %s ...' % n)
		r = '200 OK'

def produce(c):
	r = c.send(None)
	print('send None return %s' %r)
	n = 0
	while n < 1:
		n = n +1
		print('[PRODUCER] Producing %s ...' %n)
		r = c.send(n)
		print('[PRODUCER] Consumer return: %s' %r)
	c.close()

c = consumer()
produce(c)


# While True:
# send None return a
# [PRODUCER] Producing 1 ...
# [CONSUMER] Consuming 1 ...
# While True:
# [PRODUCER] Consumer return: 200 OK