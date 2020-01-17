#!usr/bin/python
import urllib.parse
import urllib.request

url = 'http://www.domain/form'
values = {'name' : 'Michael Foord',
          'address' : 'india',
          'mobile' : 'xxxxxxxxxx' }

data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url,data)
with urllib.request.urlopen(req) as response:
	the_page = response.read()
	print(the_page)