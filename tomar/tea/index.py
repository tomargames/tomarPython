#!/Users/tomar/Anaconda3/python.exe
"""
Created on Sun Jan 22 11:42:00 2017 by tomar
#!/usr/bin/python
#!/Users/tomar/Anaconda3/python.exe
"""
import sys
try:
	import utils
except:
	sys.path.append("..")
	import utils
import json
import cgi
import Tea
print("Content-type: text/html \n")
print('''
<html><head><title>Tea</title>
<LINK REL='StyleSheet' HREF='/python/tomar.css'  TYPE='text/css' TITLE='ToMarStyle' MEDIA='screen'>
<link href='//fonts.googleapis.com/css?family=Didact Gothic' rel='stylesheet'>
</head><body>
<h2 style="margin: 0px; color: beige; background-color: green; text-align: center"><a style="color: beige; text-decoration: none;" href="javascript: document.menuForm.submit();">ToMarGames</a></h2>
<h3 style="margin: 0px; color: beige; background-color: green; text-align: center">Tea</h3>
<table border="1">
<tr><td>ID</td><td>Date</td><td>Location</td><td>Host</td><td>Who Came</td></tr>
''')
form = cgi.FieldStorage() # instantiate only once!
auth = form.getvalue('auth', '')
name = form.getvalue('name', '')
auth = "tm217043487053246691286"
if auth[0:2] != 'tm':
	print('<script> window.location = "../gLogin.py?srcApp=tea"; </script>')
else:
	tea = Tea.Tea()
	for d in tea.dates:
		print(tea.displayDate(d))
