#!usr/bin/python

#python3 -m pip install paramiko
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='localhost', port='22', username='sachin', password='Password@123')
stdin, stdout, stderr = ssh.exec_command('cat /etc/passwd')

for line in stdout.readlines():
	print(line.strip())

ssh.close()
