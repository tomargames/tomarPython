#!/Users/tomar/Anaconda3/python.exe
"""
Created on Sat Nov 25 16:34:21 2017 by tomar
#!/usr/bin/python3
#!/Users/tomar/Anaconda3/python.exe
"""
import sys
try:
	import gUtils
	import Users
except:
	sys.path.append("..")
	import gUtils
	import Users
import cgi
import random
import Tea
print("Content-type: text/html \n")
print('''
<html><head><title>Tea</title>
<LINK REL='StyleSheet' HREF='/python/songs.css?{}'  TYPE='text/css' TITLE='ToMarStyle' MEDIA='screen'>
<LINK REL='StyleSheet' HREF='/python/tomar.css?{}'  TYPE='text/css' TITLE='ToMarStyle' MEDIA='screen'>
<link href='//fonts.googleapis.com/css?family=Didact Gothic' rel='stylesheet'>
<script src="https://apis.google.com/js/platform.js" async defer></script>
<meta name="google-signin-client_id" content="932688745244-i4vfeap5jgu8id5dagrc49786vvs0qrf.apps.googleusercontent.com">
</head>
<body>
'''.format(random.randrange(9999), random.randrange(9999)))
form = cgi.FieldStorage() # instantiate only once!
gid = form.getvalue('gId', '')	#remove default
name = form.getvalue('gName', '')	#remove default
gMail = form.getvalue('gMail', '')	#remove default
gImg = form.getvalue('gImage', '')	#remove default
oper = form.getvalue('oper','')
#gid = '106932376942135580175'
gUtils.toggleDivFunction()
print('''
<form name="gForm" method="POST" action="index.py">
<input type="hidden" name="gId" value="{}">
<input type="hidden" name="gName" value="{}">
<input type="hidden" name="gMail" value="{}">
<input type="hidden" name="gImage" value="{}">
<input type="hidden" name="oper" value="{}">
'''.format(gid, name, gMail, gImg, oper))
if gid == '':
	gUtils.googleSignIn()
else:
	users = Users.Users()
	authTea = users.authenticate(gid, name, gMail, gImg, users.TEA)
	authAdm = users.authenticate(gid, name, gMail, gImg, users.ADMIN)
	print(authTea[1])
	if authAdm[0] == '1':
		tea = Tea.Tea()
		if oper == 'add':
			print(tea.addNewPerson())
		else:
			print(tea.displayPerson(oper))
	else:
		print("Sorry, you are not authorized to use this page.")
print('</body></html>')