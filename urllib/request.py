import urllib.request

Data = b'somedata'
req=urllib.request.Request(url='domain-name', data=Data,method='PUT')
with urllib.request.urlopen(req) as f:
	pass
print(f.status)
print(f.reason)