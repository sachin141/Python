import urllib.request

Data = b'somedata'
req=urllib.request.Request(url='http://example.com', data=Data,method='PUT')
with urllib.request.urlopen(req) as f:
	pass
print(f.status)
print(f.reason)