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
import utils
import user
'''
This is sent google id and name, as well as a folder to return to after run
id is given to user object to scramble and check registration -- if good, returns to caller
if new id, presents an input box to accept a password, and forward everything to gAddUser
'''
form = cgi.FieldStorage() # instantiate only once!
tmUser = user.user()
gId = tmUser.encodeID(form.getvalue('gId', 'error'))
gName = form.getvalue('gName', 'error')
#gId = 'bagjdcdhgjecbdffiabhf'
#gName = 'tester'
srcApp = form.getvalue('srcApp', '.')
srcApp += '/index.py'
print("Content-type: text/html \n")
print("gAccreq: %s %s" % (form.getvalue('gId', 'error'), gName))
print('''
<html>
<head>
	<title>ToMarLogin2</title>
	<LINK REL='StyleSheet' HREF='/python/tomar.css'  TYPE='text/css' TITLE='ToMarStyle' MEDIA='screen'>
</head>
<body>
''')
print("""gId is %s""" % gId )
if tmUser.isRegisteredUser(gId):
	print('''
<form name="gForm" method="POST" action="%s">
	<input type="hidden" name="auth" value="tm%s">
	<input type="hidden" name="name" value="%s">
</form>
<script> gForm.submit(); </script>
	''' % (srcApp, gId, gName))
else:
	print('''
You must be new! Did marie give you a password?

<form name="addForm" method="POST" action="gAddUser.py">
<input type="text" name="passPhrase"><br><br>
<input type="hidden" name="gId" value="%s">
<input type="hidden" name="gName" value="%s">
<input type="hidden" name="srcApp" value="%s">
<input type="submit" class="buttonF" style="background-color: green" value="Add me!" onClick="validateUser()">
</form>
</body>
</html>
	''' % (gId, gName, srcApp))