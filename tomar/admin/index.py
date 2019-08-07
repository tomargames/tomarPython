#!/Users/tomar/Anaconda3/python.exe
"""
Created on 1/13/2017
#!/usr/bin/python
#!/Users/tomar/Anaconda3/python.exe
@author: marie
"""
import sys
import os
try:
	import gUtils
	import Users
except:
	sys.path.append("..")
	import gUtils
	import Users
import cgi
import random
print("Content-type: text/html \n")
print('''
<html><head><title>Admin</title>
<LINK REL='StyleSheet' HREF='/python/tomar.css?{}'  TYPE='text/css' TITLE='ToMarStyle' MEDIA='screen'>
<link href='//fonts.googleapis.com/css?family=Didact Gothic' rel='stylesheet'>
<script src="https://apis.google.com/js/platform.js" async defer></script>
<meta name="google-signin-client_id" content="932688745244-i4vfeap5jgu8id5dagrc49786vvs0qrf.apps.googleusercontent.com">
</head>
<body>
'''.format(random.randrange(9999), random.randrange(9999)))
print('''
<script>
function submitForm()
{
	document.gForm.oper.value = "upd";
	document.gForm.submit();
}
function goTo(x)
{
	gForm.action = x;
	gForm.submit();
}
function pBox(x, y)
{
	perm = 0;
	for (i = 0; i < y; i++)
	{
		a = "c" + x + i;
		if (document.getElementById(a).checked == true)
		{ 
			perm += 2 ** i;
		}
	}
	document.getElementById("i" + x).value = ((perm).toString(32)).toUpperCase();
}
</script>
''')
form = cgi.FieldStorage() # instantiate only once!
gid = form.getvalue('gId', '')	#remove default
name = form.getvalue('gName', '')	#remove default
gMail = form.getvalue('gMail', '')	#remove default
gImg = form.getvalue('gImage', '')	#remove default
oper = form.getvalue('oper','')
print('''
<form name="gForm" method="POST" action="#">
<input type="hidden" name="gId" value="{}">
<input type="hidden" name="gName" value="{}">
<input type="hidden" name="gMail" value="{}">
<input type="hidden" name="gImage" value="{}">
<input type="hidden" name="oper">
'''.format(gid, name, gMail, gImg))
if gid == '':
	gUtils.googleSignIn()
else:
	users = Users.Users()
	auth = users.authenticate(gid, name, gMail, gImg, users.ADMIN)
	print(auth[1])
	if auth[0] == '1':
		if oper == 'upd':
			for n in users.userDict:
#				print('form value p{} is {}'.format(n, form.getvalue('p{}'.format(n))))
				users.userDict[n]["P"] = form.getvalue('p{}'.format(n), '')
			users.saveFile()
		print('<table border=1>')
		print('<tr><th></th><th></th><th>Perm</th>')
		for a in sorted(users.appDict):
			print('<th>{}</th>'.format(users.appDict[a]["N"]))
		print('</tr>')
		for n in sorted(users.userDict):
			print(users.displayUser(n))
		print('</table><br><br><input type="button" onClick="javascript:submitForm();" value="Update">')
	else:
		print('''
Welcome to ToMarGames Friends and Family!<br><br>It looks like you've landed on a page you don't have permission to access.
				''')
print('</form></body></html>')