#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import threading
import asyncio

@asyncio.coroutine
def wget(host):
	print('wget %s...(%s)' % (host,threading.currentThread()))
	connect = asyncio.open_connection(host, 80)
	reader, writer = yield from connect
	header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
	writer.write(header.encode('utf-8'))
	yield from writer.drain()
	while True:
		line = yield from reader.readline()
		if line == b'\r\n':
			print()
			break
		print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
	# Ignore the body, close the socket
	writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# wget www.sina.com.cn...
# wget www.163.com...
# wget www.sohu.com...
# www.163.com header > HTTP/1.0 302 Moved Temporarily
# www.163.com header > Server: Cdn Cache Server V2.0
# www.163.com header > Date: Tue, 10 May 2016 15:01:06 GMT
# www.163.com header > Content-Length: 0
# www.163.com header > Location: http://www.163.com/special/0077jt/error_isp.html
# www.163.com header > Connection: close

# www.sina.com.cn header > HTTP/1.1 200 OK
# www.sina.com.cn header > Content-Type: text/html
# www.sina.com.cn header > Vary: Accept-Encoding
# www.sina.com.cn header > X-Powered-By: shci_v1.03
# www.sina.com.cn header > Server: nginx
# www.sina.com.cn header > Date: Tue, 10 May 2016 15:00:41 GMT
# www.sina.com.cn header > Last-Modified: Tue, 10 May 2016 14:57:46 GMT
# www.sina.com.cn header > Expires: Tue, 10 May 2016 15:01:41 GMT
# www.sina.com.cn header > Cache-Control: max-age=60
# www.sina.com.cn header > Age: 25
# www.sina.com.cn header > Content-Length: 555130
# www.sina.com.cn header > X-Cache: HIT from xd33-98.sina.com.cn
# www.sina.com.cn header > Connection: close

# www.sohu.com header > HTTP/1.1 200 OK
# www.sohu.com header > Content-Type: text/html
# www.sohu.com header > Content-Length: 91250
# www.sohu.com header > Connection: close
# www.sohu.com header > Date: Tue, 10 May 2016 14:59:14 GMT
# www.sohu.com header > Server: SWS
# www.sohu.com header > Vary: Accept-Encoding
# www.sohu.com header > Cache-Control: no-transform, max-age=120
# www.sohu.com header > Expires: Tue, 10 May 2016 15:01:14 GMT
# www.sohu.com header > Last-Modified: Tue, 10 May 2016 14:57:15 GMT
# www.sohu.com header > Content-Encoding: gzip
# www.sohu.com header > X-RS: 10511343.19686393.11189627
# www.sohu.com header > FSS-Cache: HIT from 6185901.11035575.6864119
# www.sohu.com header > FSS-Proxy: Powered by 2633025.3943755.3297365