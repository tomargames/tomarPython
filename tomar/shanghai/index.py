#!/Users/tomar/Anaconda3/python.exe
"""
Created on Sat May 27 16:34:21 2017 by tomar
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
import Shanghai
print("Content-type: text/html \n")
print('''
<html><head><title>Shanghai</title>
<script src="/python/utils.js"></script>
<LINK REL='StyleSheet' HREF='/python/songs.css?{}'  TYPE='text/css' TITLE='ToMarStyle' MEDIA='screen'>
<LINK REL='StyleSheet' HREF='/python/tomar.css?{}'  TYPE='text/css' TITLE='ToMarStyle' MEDIA='screen'>
<link href='//fonts.googleapis.com/css?family=Didact Gothic' rel='stylesheet'>
<script src="https://apis.google.com/js/platform.js" async defer></script>
<meta name="google-signin-client_id" content="932688745244-i4vfeap5jgu8id5dagrc49786vvs0qrf.apps.googleusercontent.com">
'''.format(random.randrange(9999), random.randrange(9999)))
gUtils.modalDiv()
form = cgi.FieldStorage() # instantiate only once!
gid = form.getvalue('gId', '')	#remove default
name = form.getvalue('gName', '')	#remove default
gMail = form.getvalue('gMail', '')	#remove default
gImg = form.getvalue('gImage', '')	#remove default
oper = form.getvalue('oper','')
gUtils.toggleDivFunction()
print('''
<form name="gForm" method="POST" action="#">
<input type="hidden" name="gId" value="{}">
<input type="hidden" name="gName" value="{}">
<input type="hidden" name="gMail" value="{}">
<input type="hidden" name="gImage" value="{}">
<input type="hidden" name="oper">
</form>
'''.format(gid, name, gMail, gImg))
if gid == '':
	gUtils.googleSignIn()
else:
	users = Users.Users()
	authS = users.authenticate(gid, name, gMail, gImg, users.SHANGHAI)		# gets you into shanghai
	print(authS[1])
	if authS[0] == '1':
		shg = Shanghai.Shanghai()
		print('''
<div id="app" align="center">
	<canvas id="dbCanvas" width="1100" height="650">
		Your browser does not support the canvas element.
	</canvas>
		''')
		print(shg.setUpScript(gid, shg.recordGame(gid, oper)))
		print(shg.modalDisplay())
		print('''
	</tbody></table>
  </form></dialog>
	<script src="/python/shanghai.js"></script>
</div>				''')
		Shanghai.aboutTheGame()
	else:
		print('''
Welcome to ToMarGames Friends and Family!<br><br>It looks like you've landed on a page you don't have permission to access.
				''')
print('</body></html>')