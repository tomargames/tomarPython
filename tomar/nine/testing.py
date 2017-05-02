#!/Users/tomar/Anaconda3/python.exe
"""
Created on Fri Jan 20 17:47:12 2017
#!/usr/bin/python
#!/Users/tomar/Anaconda3/python.exe
"""
import sys
import json
try:
	import utils
except:
	sys.path.append("..")
	import utils
print("Content-type: text/html \n")
#record = {}
#record["id"] = "217043487053246691286"
with open("eqs.json") as qData:
    questions = json.load(qData)
#for q in questions:
#    record[q["K"]] = "1"
#print(record)
#counters = {}
for q in questions:
	for s in range(2):
		ev = q["S"][s]["E"]					# enneagram value of that statement
		if ev in ('1', '3'):
			print('%s %s %s %s' %(q['K'], q['D'], ev, utils.scramble(q['S'][s]['S'], -9)))
