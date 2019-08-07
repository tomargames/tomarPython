#!/Users/tomar/Anaconda3/python.exe
"""
Created on Sat May 27 16:34:21 2017 by tomar
#!/usr/bin/python3
#!/Users/tomar/Anaconda3/python.exe
"""
import sys
import urllib
try:
	import gUtils
	import Users
except:
	sys.path.append("..")
	import gUtils
	import Users
import cgi
import random
import Songs

def renderHtml(x):
	# for greek
	if sys.stdout.encoding == 'UTF_8':
		print(x.encode('UTF_8', 'xmlcharrefreplace').decode('utf8'))
	else:
		print(x.encode('ascii', 'xmlcharrefreplace').decode('utf8'))
def encodeHtml(x):
	return urllib.parse.unquote(x, encoding='utf-8', errors='replace') 
print("Content-type: text/html \n")
print('''
<html><head><title>SongBook</title>
<LINK REL='StyleSheet' HREF='/python/songs.css?{}'  TYPE='text/css' TITLE='ToMarStyle' MEDIA='screen'>
<LINK REL='StyleSheet' HREF='/python/tomar.css?{}'  TYPE='text/css' TITLE='ToMarStyle' MEDIA='screen'>
<link href='//fonts.googleapis.com/css?family=Didact Gothic' rel='stylesheet'>
<script src="https://apis.google.com/js/platform.js" async defer></script>
<meta name="google-signin-client_id" content="932688745244-i4vfeap5jgu8id5dagrc49786vvs0qrf.apps.googleusercontent.com">
</head>
<body>
'''.format(random.randrange(9999), random.randrange(9999)))
print('''
<!-- The Modal -->
<div id="myModal" class="modal">
  <!-- Modal content -->
  <div class="modal-content">
    <span class="close">&times;</span>
    <p id="nDisplay">filler</p>
  </div>
</div>
	''')
form = cgi.FieldStorage() # instantiate only once!
gid = form.getvalue('gId', '')	#remove default
name = form.getvalue('gName', '')	#remove default
gMail = form.getvalue('gMail', '')	#remove default
gImg = form.getvalue('gImage', '')	#remove default
oper = form.getvalue('oper','')
#gid = '106932376942135580175'
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
	authS = users.authenticate(gid, name, gMail, gImg, users.SONGBOOK)		# gets you into songbook public tags
	authA = users.authenticate(gid, name, gMail, gImg, users.ADMIN)			# gets you notes
	authT = users.authenticate(gid, name, gMail, gImg, users.TEA)			# gets you all tags and media
	authF = users.authenticate(gid, name, gMail, gImg, users.FF)			# gets you all tags and media
	if authA[0] == '1':
		perm = 3
	elif authT[0] == '1' and authF[0] == '1':
		perm = 3
	elif authT[0] == '1' or authF[0] == '1':
		perm = 2
	elif authS[0] == '1':
		perm = 1
	else:
		perm = 0
	#perm = 1						#uncomment to test permissions
	print(authS[1])
	if perm > 0:
		print("<!-- instantiating Songs() -->")
		songbook = Songs.Songs()
		print("<!-- all following comes from jsFunctions -->")
		renderHtml(songbook.jsFunctions(perm))
		print("<!-- end of jsFunctions --> <br>")
		#print("in index, oper is {}, perm is {}<br>".format(oper, perm))
		if (oper[0] == "N"):
			renderHtml(songbook.displaySong(encodeHtml(oper[1:]), perm))
		else:
			if (oper[0] == "T"):
				results = songbook.displaySongList(songbook.tagDict[oper[1:2]][encodeHtml(oper[2:])], perm)
			elif (oper[0] == "D"):
				results = songbook.displaySongList(songbook.getSongsByDeck(encodeHtml(oper[1:])), perm)
			elif (oper[0] == "M"):
				results = songbook.displaySongList(songbook.marked, perm)
			renderHtml('<script>{}'.format(results[1]))
			renderHtml(results[2])
			renderHtml(results[4])
			renderHtml('{}</script>'.format(results[3]))
			renderHtml(results[0])
	else:
		print('''
Welcome to ToMarGames Friends and Family!<br><br>It looks like you've landed on a page you don't have permission to access.
				''')
print('</body></html>')