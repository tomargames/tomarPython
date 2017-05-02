#!/Users/tomar/Anaconda3/python.exe
from __future__ import division
from __future__ import nested_scopes
from __future__ import generators
from __future__ import division
from __future__ import absolute_import
from __future__ import with_statement
from __future__ import print_function
from __future__ import unicode_literals
import json
import sys
try:
	import utils
except:
	sys.path.append("..")
	import utils    
import cgi
print("Content-type: text/html \n")
def formatRecord(recordIn, questions):
	''' scores a dated saved enneagram record '''
	''' formats a <tr> to display counters '''
	counters = {}
	for q in questions:
		if q["K"] in recordIn.keys():
			ch = int(recordIn[q["K"]]) - 1			# this is the statement chosen
			ev = q["S"][ch]["E"]					# enneagram value of that statement
			if ev in counters.keys():			# questions[0]["S"][0]["E"]
				counters[ev] += 1
			else:
				counters[ev] = 1
	fString = '<tr style="font-size: 1.2em"><td class="textL">' + utils.formatDate(u["date"]) + '</td>'
	for c in sorted(counters.items(), key=lambda ect: ect[1]):
		fString += '<td class="textL"><b>' + c[0] + '</b>: ' + utils.formatNumber(c[1], 3) + '</td>'
	return fString + '</tr>'
print('''
<html><head><title>Enneagram</title>
<LINK REL='StyleSheet' HREF='/python/tomar.css'  TYPE='text/css' TITLE='ToMarStyle' MEDIA='screen'>
<link href='//fonts.googleapis.com/css?family=Didact Gothic' rel='stylesheet'>
</head><body>
<h2 style="margin: 0px; color: beige; background-color: green; text-align: center">ToMarGames</h2>
<h3 style="margin: 0px; color: beige; background-color: green; text-align: center">Enneagrams</h3>
''')
form = cgi.FieldStorage() # instantiate only once!
auth = form.getvalue('auth', '')
name = form.getvalue('name', '')
eTypes = {"1": "Reformer", "2": "Helper", "3": "Achiever", "4": "Individualist", "5": "Investigator", "6": "Loyalist", "7": "Enthusiast", "8": "Challenger", "9": "Peacemaker"}
auth = "tm217043487053246691286"
if auth[0:2] != 'tm':
	print('<script> window.location = "../gLogin.py?srcApp=nine"; </script>')
else:	
	with open("nine/eqs.json") as qData:
		questions = json.load(qData)
	with open("nine/eqsave.json") as uData:
		users = json.load(uData)
	first = True
	for u in users:
		if u["id"] == auth[2:]:
			if "date" not in u:
				saverecord = u
				break
			else:
				if first:
					first = False
					print('''
					<table><tr valign="top"><td style="background-color: #dddd88; "><table>
					<tr><td colspan="2" class="textL" style="color: #dddd88; background-color: darkblue; font-size: 1.5em;">Enneagram Types</td></tr>
					''')
					for t in sorted(eTypes):
						print('''
						<tr><td class="textC" style="color: #dddd88; background-color: darkblue; font-size: 1.3em;">%s</td>
							<td class="textL"><a href="%s">The %s</a></td></tr>
						''' %(t, "https://www.enneagraminstitute.com/type-" + t, eTypes[t]))
					print('''
					</table></td>
					<td><h4 style="margin: 0px; color: beige; background-color: purple; text-align: left">Past results for %s</h4>
					<table>
					''' % name)
				print(formatRecord(u, questions))
	else:
		saverecord = {}
	print('</table></td></tr></table>')
