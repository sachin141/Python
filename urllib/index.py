#!usr/bin/python
import urllib.request

httpResponse = urllib.request.urlopen("domain-name")
#print status code of website
print(httpResponse.code)

#print html of webpage
print(httpResponse.read())

#http response object
print(dir(httpResponse))

print(httpResponse.headers)
