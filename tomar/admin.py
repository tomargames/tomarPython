#!/Users/tomar/Anaconda3/python.exe
"""
Created on 1/13/2017
#!/usr/bin/python
#!/Users/tomar/Anaconda3/python.exe
@author: marie
"""
from __future__ import division
from __future__ import nested_scopes
from __future__ import generators
from __future__ import division
from __future__ import absolute_import
from __future__ import with_statement
from __future__ import print_function
from __future__ import unicode_literals
import cgi
import json
import utils
import user
print("Content-type: text/html \n")
form = cgi.FieldStorage() # instantiate only once!
auth = form.getvalue('auth', '')
name = form.getvalue('name', '')
auth = "tm217043487053246691286"
if auth != "tm217043487053246691286":
	print('<script> window.location = "gLogin.py"; </script>')
else:
	print('''
<html>
<head>
	<title>ToMarAdmin</title>
<LINK REL='StyleSheet' HREF='/python/tomar.css?%s'  TYPE='text/css' TITLE='ToMarStyle' MEDIA='screen'>
<link href='//fonts.googleapis.com/css?family=Didact Gothic' rel='stylesheet'>
</head>
<body>
<h2 style="margin: 0px; color: beige; background-color: green; text-align: center"><a style="color: beige; text-decoration: none;" href="javascript:document.menuForm.submit(); ">ToMarGames</a></h2>
<h3>ToMarUsers</h3>
<table border="1">
	''')
	tmUsers = user.user().users
	for n in tmUsers:
		print('''
	<tr><td class="textC">%s</td><td class="textC">%s</td></tr>
		''' % (n["I"], n["N"]))
	print('''
</table>
<h3>Enneagrams</h3>
<table border="1">
	''')
	with open("nine/eqsave.json") as uData:
		users = json.load(uData)
	for u in users:
		if "date" in u:					#finalized records
			print('''
<tr><td>%s</td></tr>
			''' % u)
	print('''
</table>
<form name="menuForm" method="POST" action="index.py">
<input type="hidden" name="auth" value="%s">
<input type="hidden" name="name" value="%s">
</form>
</body></html>
	''' % (auth, name))
