#!/Users/tomar/Anaconda3/python.exe
"""
Created on Fri Jan 20 17:47:12 2017
#!/usr/bin/python
#!/Users/tomar/Anaconda3/python.exe

This sets up data objects and repositories for the following enneagram objects:
	questions is the repository of dict objects, 144 of them
	results is a list of dict records for users
"""
import sys
import json
try:
	import utils
except:
	sys.path.append("..")
	import utils

class enneagram(object):
	def __init__(self):
		""" loads questions and records and types
			questions: a list of dicts, one dict for each of 144 questions
				{"S": list of statements[2]
					{"S": text of statement
					 "E": eValue of statement, if chosen}
				 "D": display decimal value (1 - 144)
				 "K": display base12 value (00 - BB)}
			records: a list of dicts, one dict for each submission
				{"id": scrambled goodleID
				 "date": populated when record submitted, otherwise blank
				 key-value pairs for whichever K values were chosen}
			types: dict of enneagram types and their associated names
		"""
		with open("eqs.json") as qData:
			self.questions = json.load(qData)
		with open("eqsave.json") as uData:
			self.records = json.load(uData)
		self.types = {"1": "Reformer", "2": "Helper", "3": "Achiever", "4": "Individualist", "5": "Investigator", "6": "Loyalist", "7": "Enthusiast", "8": "Challenger", "9": "Peacemaker"}
	def scoreRecord(self, recordIn):
		''' scores a dated saved enneagram record, and returns a dict of counters '''
		counters = {}
		for q in self.questions:
			if q["K"] in recordIn.keys():
				ch = int(recordIn[q["K"]]) - 1			# this is the statement chosen
				ev = q["S"][ch]["E"]					# enneagram value of that statement
				if ev in counters.keys():			# questions[0]["S"][0]["E"]
					counters[ev] += 1
				else:
					counters[ev] = 1
		return counters
