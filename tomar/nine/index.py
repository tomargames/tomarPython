#!/Users/tomar/Anaconda3/python.exe
"""
Created on Sun Dec  4 23:28:36 2016
#!/usr/bin/python
#!/Users/tomar/Anaconda3/python.exe
"""
import sys
try:
	import utils
except:
	sys.path.append("..")
	import utils
import random
import json
import cgi

print("Content-type: text/html \n")
print('''
<html><head><title>Enneagram</title>
<LINK REL='StyleSheet' HREF='/python/tomar.css'  TYPE='text/css' TITLE='ToMarStyle' MEDIA='screen'>
<link href='//fonts.googleapis.com/css?family=Didact Gothic' rel='stylesheet'>
</head><body>
<h2 style="margin: 0px; color: beige; background-color: green; text-align: center"><a style="color: beige; text-decoration: none;" href="javascript:document.menuForm.submit();">ToMarGames</a></h2>
<h3 style="margin: 0px; color: beige; background-color: green; text-align: center">Enneagrams</h3>
''')
form = cgi.FieldStorage() # instantiate only once!
auth = form.getvalue('auth', '')
name = form.getvalue('name', '')
auth = "tm217043487053246691286"
if auth[0:2] != 'tm':
	print('<script> window.location = "../gLogin.py?srcApp=nine"; </script>')
else:
	import enneagram
	eData = enneagram.enneagram()
	first = True
	for u in eData.records:
		if u["id"] == auth[2:]:
			if "date" not in u:
				saverecord = u
				break
			else:
				if first:
					first = False
					print('''
					<table><tr valign="top"><td style="background-color: #dddd88; "><table>
					<tr><td colspan="2" class="textL" style="color: #darkblue; background-color: #dddd88; font-size: 1.5em;"><a href="https://www.enneagraminstitute.com/how-the-enneagram-system-works/">Enneagram Types</a></td></tr>
					''')
					for t in sorted(eData.types):
						print('''
						<tr><td class="textC" style="color: #dddd88; background-color: darkblue; font-size: 1.3em;">%s</td>
							<td class="textL"><a href="%s">The %s</a></td></tr>
						''' %(t, "https://www.enneagraminstitute.com/type-" + t, eData.types[t]))
					print('''
					</table></td>
<td><h4 style="margin: 0px; color: beige; background-color: purple; text-align: left">Past results for %s</h4>
					<table>
					''' % name)
				counters = eData.scoreRecord(u)
				fString = '<tr style="font-size: 1.2em"><td class="textL">' + utils.formatDate(u["date"]) + '</td>'
				for c in sorted(counters.items(), key=lambda ect: ect[1], reverse=True):
					fString += '<td class="textL"><b>' + c[0] + '</b>: ' + utils.formatNumber(c[1], 3) + '</td>'
				fString += '</tr>'
				print(fString)
	else:
		saverecord = {}
	print('</table></td></tr></table>')
	print('''
	<script>
	function validateForm()
	{
	''')
	for q in eData.questions:
		k = "You missed answering question "+q["D"]+":\\n\\n"+utils.scramble(q["S"][0]["S"], -9)+".\\n or \\n"+utils.scramble(q["S"][1]["S"], -9)+".\\n\\nOK to proceed without it, or Cancel to take another look. "
		print('if (document.getElementById("'+q["K"]+'0").checked == false && document.getElementById("'+q["K"]+'1").checked == false) ')
		print('{ document.getElementById("'+q["K"]+'0").focus(); if (confirm("'+k+'") != true) 	{ return; } }')
	print('''
		saveProgress();
		document.tm9Form.submit();
	}
	function saveProgress()
	{
		var formElement = document.querySelector("saveForm");
		var formData = new FormData(formElement);
		var request = new XMLHttpRequest();
		request.open("POST", "tm9Save.py");
		formData.append("id", "%s");
	''' % auth[2:])
	for q in questions:
		for i in range(2):
			print(' if (document.getElementById("'+q["K"]+str(i)+'").checked == true) { formData.append("'+q["K"]+'", '+str(i+1)+'); } ')
	print('''
		request.send(formData);
	}
	</script>
	<h2>Enneagram Survey</h2>
	<table>
	<form name="tm9Save" method="POST" action="tm9Save.py">
		<input type="hidden" name="id" value="%s">
	</form>
	<form name="menuForm" method="POST" action="../index.py">
		<input type="hidden" name="auth" value="%s">
		<input type="hidden" name="name" value="%s">
	</form>
	<form name="tm9Form" thod="POST" action="tm9Process.py">
		<input type="hidden" name="auth" value="%s">
		<input type="hidden" name="name" value="%s">
	''' % (auth[2:], auth, name, auth, name))
	print('<tr><td></td><td class="textL" style="color: brown">There are 144 pairs of statements. Choose the one from each pair that best describes you.<br>When you submit your responses, you will be given an additional chance to select something from any pairs where you did not make a selection.<br>If you "cancel", you will be taken back to that pair of statements; if you click "OK", it will leave that pair unanswered.<br>The blue "Save progress" button will store your responses, and reload them when you come back into the page.<br>The green "Submit responses" button will close and date your responses.<br>You may take this test as many times as you like, and you can see how your scores change over time.</td></tr>')
	print('<tr><td></td><td><hr></td></tr>')
	for q in questions:
		checked = 0
		if q["K"] in saverecord.keys():
			checked = int(saverecord[q["K"]])
		print ('<tr><td class="textL" style="color: darkblue">'+q["D"]+'</td><td><table>')
		for i in range(2):
			checkString = ''
			if checked - 1 == i:
				checkString = "checked"
			print ('''<tr><td class="textL" style="color: darkgreen"><input type="radio" name="%s" id="%s" value="%s" %s/> %s. </td></tr>
	  ''' % (q["K"], q["K"] + str(i), str(i), checkString, utils.scramble(q["S"][i]["S"], -9)))
		print ('<tr><td><hr></td></tr></table>')
		if int(q["D"]) % 12 == 0:
			print('<tr><td></td><td><table><tr><td><input type="input" class="buttonF" style="background-color: blue; color: beige; font-size: 1.1em" value="Save progress" onClick="saveProgress()"></td><td><img src="/python/330px-Enneagram.svg.png" height="80" width="80"></td><td><input type="input" class="buttonF" style="background-color: green; color: beige; font-size: 1.1em" value="Submit responses" onClick="validateForm()"></td></tr></table></td></tr>')
			print('<tr><td></td><td><hr></td></tr>')
	print("</form></table>")
	print("</body></html>")