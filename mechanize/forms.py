#!usr/bin/python

import mechanize

br=mechanize.Browser()
br.open('login formurl')

for form in br.forms():
	#print(form)

	br.select_form(nr=0)
	br.form['email']='xyz@gmail.com'
	br.form['password']='xyz@1234'
	br.submit()

	for link in br.links():
	 	print(link.url + ':' + link.text)