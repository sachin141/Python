#!usr/bin/python

import socket

s=socket.socket()
print("socket created")

port=8001
s.bind(('', port))
print("socket bind to %s",port)

s.listen(2)

while True:
	c,addr = s.accept()
	print("connected from addr", addr)

	c.send("Connecting")
	c.close()


