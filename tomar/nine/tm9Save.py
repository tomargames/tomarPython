#!/Users/tomar/Anaconda3/python.exe
"""
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
'''
eqsave is a json list of dicts, each dict is a save record
'''	
form = cgi.FieldStorage() # instantiate only once!
if form.getvalue('id',''):
	id = form.getvalue('id')
	saverecord = {"id": id}
	for i in range(144):
		k = utils.formatNumber(utils.baseConvert(i, 12), 2)
		if form.getvalue(k):
			saverecord[k] = form.getvalue(k)
	with open("eqsave.json") as uData:
		users = json.load(uData)
	for n, u in enumerate(users):
		if u["id"] == id and "date" not in u:		#this is an open record for this id
			users[n] = saverecord
			break
	else:											#if no record found for this id
		users.append(saverecord)
	outfile = open('eqsave.json', 'w')
	json.dump(users, outfile)
	outfile.close()
