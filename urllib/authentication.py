import urllib.request

auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(realm='PDQ Application',
	uri='http://138.201.30.146/logsight/login',
	emailId='logsight.watch7@gmail.com',
	password='Test@1234')
opener=urllib.request.build_opener(auth_handler)

urllib.request.install_opener(opener)
urllib.request.urlopen('http://138.201.30.146/logsight/login')