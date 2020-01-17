#!usr/bin/python
from pexpect import pxssh
import getpass

try:
	s = pxssh.pxssh()
	hostname = 'hostname'
	username = 'xxxxxx'
	password = 'xxxxxx'
	s.login(hostname, username, password) #login
	s.sendline('ls -s') #run command
	s.prompt() 
	print(s.before)
	s.logout()
except pxssh.ExceptionPxssh as e:
	print("login failed")
	print(e)
