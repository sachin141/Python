#!usr/bin/python
import socket

s=socket.socket()

port=8001
s.connect(('',port))

print(s.recv(1456))
s.close()	