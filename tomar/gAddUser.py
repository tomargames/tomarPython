#!/Users/tomar/Anaconda3/python.exe
"""
Created on Thu Dec 15 23:37:54 2016
tm9Save -- will save progress on form
@author: tomar
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
'''
This is sent scrambled google id and name, a password, and the srcApp 
all is sent to user object to validate and store, and returns to the app
Incorrect password will send you to ToMarGames Menu
'''
form = cgi.FieldStorage() # instantiate only once!
tmUser = user.user()
print("Content-type: text/html \n")
if tmUser.registerUser(form.getvalue('gId', 'error'), form.getvalue('gName', ''), form.getvalue('passPhrase', 'error')) == False:
	print('<script> window.location="/ToMar2015/Menu"; </script>')
else:	
	print(''' 
	<html>
	<head>
		<title>ToMarLogin3</title>
		<LINK REL='StyleSheet' HREF='/python/tomar.css'  TYPE='text/css' TITLE='ToMarStyle' MEDIA='screen'>
	</head>
	<body>
	''')
	srcApp = form.getfirst('srcApp', '')
	with open("tmList.json") as uData:
		tmUsers = json.load(uData)
	tmUsers[gId] = gName
	outfile = open('tmList.json', 'w')
	json.dump(tmUsers, outfile, default = utils.jdefault)
	outfile.close()
	print(''' 
	<form name="gForm" method="POST" action="%s">
		<input type="hidden" name="auth" value="tm%s">
		<input type="hidden" name="name" value="%s">
	</form>
	<script>gForm.submit(); </script></body></html>
		''' % (srcApp, gId, form.getvalue('gName', '')))
