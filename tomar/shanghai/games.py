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
import utils
import cgi
import random
import json
print("Content-type: text/html \n")
print('''
<html><head><title>Shanghai Game History</title>
<script src="/python/utils.js"></script>
<LINK REL='StyleSheet' HREF='/python/songs.css?{}'  TYPE='text/css' TITLE='ToMarStyle' MEDIA='screen'>
<LINK REL='StyleSheet' HREF='/python/tomar.css?{}'  TYPE='text/css' TITLE='ToMarStyle' MEDIA='screen'>
<link href='//fonts.googleapis.com/css?family=Didact Gothic' rel='stylesheet'>
<script src="https://apis.google.com/js/platform.js" async defer></script>
<meta name="google-signin-client_id" content="932688745244-i4vfeap5jgu8id5dagrc49786vvs0qrf.apps.googleusercontent.com">
'''.format(random.randrange(9999), random.randrange(9999)))
gUtils.goTo()
gUtils.toggleDiv()
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
</form>
'''.format(gid, name, gMail, gImg))
#gid = "106932376942135580175"
if gid == '':
	gUtils.googleSignIn()
else:
	users = Users.Users()
	authS = users.authenticate(gid, name, gMail, gImg, users.SHANGHAI)		# gets you into shanghai
	authA = users.authenticate(gid, name, gMail, gImg, users.ADMIN)
	print(authS[1])
	if authS[0] == '1':
		with open("games.json") as gData:
			games = json.load(gData)
		gDict = {}
		for g in games:
			id = g["I"]
			if (id in gDict):
				gDict[id].append((g["T"], g["M"]))
			else:
				gDict[id] = [((g["T"], g["M"]))]
		if authA[0] == '1':
			for u in sorted(gDict):
				print('''<br><a class="textL" style="color: blue; font-size: 1.2em;" href="javascript:'" ''')
				print(''' onClick=javascript:toggleDiv("div{}")>{} ({})</a>'''.format(u, u, len(gDict[u])))
				print('''<div id="div{}" style="display:none;";>'''.format(u))
				print('''<table border=0><tr><th>Date</th><th>Moves</th>''')
				for g in gDict[u]:
					print('''<tr><td>{}</td><td class="textR">{}</td></tr>'''.format(utils.formatDate(g[0][0:8]), g[1]))
				print('''</table>''')
				print('''</div>''')
		else:
			print('''<table border=0><tr><th>Date</th><th>Moves</th>''')
			for g in gDict[gid]:
				print('''<tr><td>{}</td><td class="textR">{}</td></tr>'''.format(utils.formatDate(g[0][0:8]), g[1]))
			print('''</table>''')
	else:
		print('''
Welcome to ToMarGames Friends and Family!<br><br>It looks like you've landed on a page you don't have permission to access.
				''')
print('</body></html>')