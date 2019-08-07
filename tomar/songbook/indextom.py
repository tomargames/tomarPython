#!/Users/tomar/Anaconda3/python.exe
"""
Created on Sat May 27 16:34:21 2017 by tomar
#!/usr/bin/python3
#!/Program Files/Anaconda3/python.exe
"""
import sys
import io
import os
import codecs
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
    if sys.stdout.encoding == 'UTF_8':
        print(x.encode('UTF_8', 'xmlcharrefreplace').decode('utf8'))
    else:
        print(x.encode('ascii', 'xmlcharrefreplace').decode('utf8'))

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
gid = form.getvalue('gId', '')    #remove default
name = form.getvalue('gName', '')    #remove default
gMail = form.getvalue('gMail', '')    #remove default
gImg = form.getvalue('gImage', '')    #remove default
oper = form.getvalue('oper','')

#gid = '106932376942135580175'
gUtils.toggleDivFunction()
print('''
<script>
// open media file in new window
function showPage(x)
{
    window.open('/python/media/' + x);
}
function showWiki(x)
{
    window.open(x);
}
function fetch(x)
{
    gForm.oper.value = x;
    gForm.submit();
}
function newSearch()
{
    gForm.oper.value = '';
    gForm.submit();
}
function sortTable(col)
{
  var table, rows, switching, i, x, y, shouldSwitch;
  table = document.getElementById("detailTable");
  switching = true;
  /*Make a loop that will continue until no switching has been done:*/
  while (switching)
  {
    //start by saying: no switching is done:
    switching = false;
    rows = table.getElementsByTagName("TR");
    /*Loop through all table rows (except the
    first, which contains table headers):*/
    for (i = 1; i < (rows.length - 1); i++)
    {
      //start by saying there should be no switching:
      shouldSwitch = false;
      /*Get the two elements you want to compare,
      one from current row and one from the next:*/
      x = rows[i].getElementsByTagName("TD")[col];
      y = rows[i + 1].getElementsByTagName("TD")[col];
      //check if the two rows should switch place:
      if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
        //if so, mark as a switch and break the loop:
        shouldSwitch= true;
        break;
      }
    }
    if (shouldSwitch) {
      /*If a switch has been marked, make the switch and mark that a switch has been done:*/
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
    }
  }
}
</script>
''')
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
    authS = users.authenticate(gid, name, gMail, gImg, users.SONGBOOK)        # gets you into songbook public tags
    authA = users.authenticate(gid, name, gMail, gImg, users.ADMIN)            # gets you notes
    authT = users.authenticate(gid, name, gMail, gImg, users.TEA)            # gets you all tags and media
    print(authS[1])
    if authS[0] == '1':
        songbook = Songs.Songs()
        if oper == '':            #display search stuff
            renderHtml(songbook.browse(authS[0]))
        else:
             results = songbook.displaySongList(songbook.getSongsByTag(urllib.parse.unquote(oper, encoding='utf-8', errors='replace')), authS[0])
             renderHtml(sys.stdout.encoding)
             renderHtml(results[1])
             renderHtml(results[2])
             renderHtml(results[3])
             renderHtml(results[0])
#             print(results[1])
#             print(results[2])
#             print(results[3])
#             print(results[0])            
    else:
        print('''
Welcome to ToMarGames Friends and Family!<br><br>It looks like you've landed on a page you don't have permission to access.
                ''')
print('</body></html>')