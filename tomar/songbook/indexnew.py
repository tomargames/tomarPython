#!/Program Files/Anaconda3/python.exe
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 16:34:21 2017 by tomar
#!/usr/bin/python
#!/Program Files/Anaconda3/python.exe
"""
from __future__ import nested_scopes
from __future__ import generators
from __future__ import division
from __future__ import absolute_import
from __future__ import with_statement
from __future__ import print_function
from __future__ import unicode_literals
import os
os.environ["chcp"] = "65001"
import sys
import io

try:
    import gUtils 
    import Users
except:
    sys.path.append("..")
    import gUtils
    import Users
import random
import cgi
import codecs
import Songsnew
class Logger(object):
    def __init__(self):
        #f = open(1, "a", encoding='utf8', closefd=False)
        sys.stdout = open(1,'a',encoding='utf8',errors="ignore")
        #sys.stdout = open(1,'a',encoding='utf8',errors='ignore')
        #sys.stdout = open(1,'a','utf8')
        #sys.stdout = codecs.getwriter("utf-8")
        #open(1, "a", encoding='utf8', closefd=False)
        self.terminal = sys.stdout
        self.log = open("C:\Apache24\htdocs\python\logfile.txt", "a", encoding='utf8')

    def write(self, message):
        self.log.write(message)
        self.terminal.write(message)
        

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass    
#        outfile = open('C:/Apache24/htdocs/tomar/songbook/returnHtml2.html', 'w', encoding='utf8')
#        outfile.write(results[1])
#        outfile.close()
#
#def printRAW(str):
#     RAWOut = open(1, 'w', encoding='utf8', closefd=False)
#     print(str, file=RAWOut)
#     RAWOut.flush()
#     RAWOut.close()
#sys.stdout = codecs.getwriter('utf8')(sys.stdout)     
sys.stdout = Logger()
#import codecs
#
#def make_streams_binary():
#    sys.stdin = sys.stdin.detach()
#    sys.stdout = sys.stdout.detach()
#
#sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())     
#print("Content-type: text/html; charset=utf-8 \n")
print('''
<html><head><title>SongBook</title>
<LINK REL='StyleSheet' HREF='/python/songs.css?{}'  TYPE='text/css' TITLE='ToMarStyle' MEDIA='screen'>
<LINK REL='StyleSheet' HREF='/python/tomar.css?{}'  TYPE='text/css' TITLE='ToMarStyle' MEDIA='screen'>
<link href='//fonts.googleapis.com/css?family=Open Sans' rel='stylesheet'>
<script src="https://apis.google.com/js/platform.js" async defer></script>
<meta name="google-signin-client_id" content="932688745244-i4vfeap5jgu8id5dagrc49786vvs0qrf.apps.googleusercontent.com">
</head>
<body>
'''.format(random.randrange(9999), random.randrange(9999)))
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
    level = users.authenticate(gid, name, gMail, gImg)
    gUtils.tmBanner('{}<br>{}'.format(name, users.userType(gid)), 'SongBook')
    songbook = Songsnew.Songs()
    if oper == '':            #display search stuff
        print(songbook.browse(level))
    else:
#        print(songbook.getSongsByTag(oper))
        results = songbook.displaySongList(songbook.getSongsByTag(oper), level)
        #results = songbook.displaySongList(['368'], level)
        #printRAW(results[1])
        #printRAW(results[0])
        #print("Χερουβικόν".encode("utf-8"))
        #@sys.stdout.write("Ûnicöde")
        #print("Ûnicöde Χερουβικόν")
        #print("Χερουβικόν")
        #print(sys.getdefaultencoding())
        #print(sys.stdout.encoding())
        outfile = open('C:/Apache24/htdocs/python/returnHtml2.html', 'w', encoding='utf8')
        outfile.write(results[1])
        outfile.close()
        outfile = open('C:/Apache24/htdocs/python/noteHtml2.html', 'w', encoding='utf8')
        outfile.write(results[0])
        outfile.close()
        #sys.stdout.buffer.write(b'abc')
        #sys.stdout.buffer.write(results[1])
        #sys.stdout.write(results[0])
        #sys.stdout.write(results[1])
        #sys.__stdout__.buffer.write(results[0])
        #printRAW(results[1])
#        print('''
#              <script> window.location ='/python/noteHtml2.html; 
#              </script>''')
        print(results[1])
        print(results[0])
print('</body></html>')