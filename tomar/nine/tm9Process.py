#!/Users/tomar/Anaconda3/python.exe
"""
Created on Sun Dec  4 23:28:36 2016
#!/usr/bin/python
#!/Users/tomar/Anaconda3/python.exe
"""
from __future__ import division
from __future__ import nested_scopes
from __future__ import generators
from __future__ import division
from __future__ import absolute_import
from __future__ import with_statement
from __future__ import print_function
from __future__ import unicode_literals
import json
import cgi
import sys
try:
    import utils
except:
    sys.path.append("..")
    import utils    

print("Content-type: text/html \n")
print('''
<html><head><title>ToMar Enneagram results</title>
<LINK REL='StyleSheet' HREF='/python/tomar.css'  TYPE='text/css' TITLE='ToMarStyle' MEDIA='screen'>
</head><body>
''')
form = cgi.FieldStorage() # instantiate only once!
auth = form.getvalue('auth', '')
name = form.getvalue('name', '')
#auth = "tm217043487053246691286"
if auth[0:2] == 'tm':
	with open("eqsave.json") as uData:
		users = json.load(uData)
	for n, u in enumerate(users):
		if u["id"] == auth[2:] and "date" not in u:		#this is an open record for this id
			u["date"] = utils.dateTime()[0]
			break
	outfile = open('eqsave.json', 'w')
	json.dump(users, outfile)
	outfile.close()
else:
	print("Unable to process input")
print('''
<form name="gForm" method="POST" action="index.py">
	<input type="hidden" name="auth" value="%s">
	<input type="hidden" name="name" value="%s">
</form>
<script> gForm.submit(); </script>
</body></html>
''' % (auth, name))

