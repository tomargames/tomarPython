#!/Users/tomar/Anaconda3/python.exe
'''
#!/usr/bin/python
#!/Users/tomar/Anaconda3/python.exe
'''
from __future__ import division
from __future__ import nested_scopes
from __future__ import generators
from __future__ import division
from __future__ import absolute_import
from __future__ import with_statement
from __future__ import print_function
from __future__ import unicode_literals
import cgi
import random
print("Content-type: text/html \n")
print('''
<html><head><title>ToMarFriendsAndFamily</title>
<LINK REL='StyleSheet' HREF='/python/tomar.css?%s'  TYPE='text/css' TITLE='ToMarStyle' MEDIA='screen'>
<link href='//fonts.googleapis.com/css?family=Didact Gothic' rel='stylesheet'>
</head><body>
''' % random.randrange(9999))
form = cgi.FieldStorage() # instantiate only once!
auth = form.getvalue('auth', '')
name = form.getvalue('name', '')
#auth = "tm217043487053246691286"
'''
' if you don't come in with a valid auth already posted, you will be sent to the login page
'''
if auth[0:2] != 'tm':
	print('<script> window.location = "gLogin.py"; </script>')
print('''
<h1 style="margin: 0px; color: beige; background-color: green; text-align: center">ToMarGames</h1>
<h5 style="margin: 0px; color: lightblue; background-color: green; text-align: center">%s</h5>
<br><br>

<form name="nForm" method="POST" action="nine/index.py">
	<input type="hidden" name="auth" value="%s">
	<input type="hidden" name="name" value="%s">
	<input class="buttonF" style="color: beige; background-color: indigo;" type="submit" value="Enneagram">
</form>
''' % (name, auth, name))
print('''
<form name="tForm" method="POST" action="tea/index.py">
	<input type="hidden" name="auth" value="%s">
	<input type="hidden" name="name" value="%s">
	<input class="buttonF" style="color: beige; background-color: indigo;" type="submit" value="Tea">
</form>
''' % (auth, name))
if auth == "tm217043487053246691286":
	print('''
<form name="aForm" method="POST" action="admin.py">
	<input type="hidden" name="auth" value="%s">
	<input type="hidden" name="name" value="%s">
	<input class="buttonF" style="color: beige; background-color: indigo;" type="submit" value="Admin">
</form>
	''' % (auth, name))
print("</body></html>")