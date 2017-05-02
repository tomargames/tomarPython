#!/Users/tomar/Anaconda3/python.exe
"""
Created on Sun Jan 22 20:26:57 2017 by tomar
#!/usr/bin/python
#!/Users/tomar/Anaconda3/python.exe
"""
import json
import sys
try:
	import utils
except:
	sys.path.append("..")
	import utils


class Tea(object):
	def __init__(self):
		with open("teaDates.json") as dData:
			self.dates = json.load(dData)
		with open("teaPeople.json") as pData:
			self.people = json.load(pData)
	def make32(self, binaryIn):
		out32 = 0
		powerOf2 = 1
		for d in reversed(binaryIn):
			out32 += int(d) * powerOf2
			powerOf2 *= 2
		return '0123456789ABCDEFGHIJKLMNOPQRSTUV'[out32]
	def makeBinary(self, in32):
		idx = '0123456789ABCDEFGHIJKLMNOPQRSTUV'.index(in32)
		binaryOut = ''
		for po in [16, 8, 4, 2]:
			if idx > po:
				binaryOut += "1"
				idx -= po
			else:
				binaryOut += "0"
		return binaryOut + str(idx)
	def compressTeas(self, binaryIn):
		if len(binaryIn) < 6:
			return self.make32(binaryIn)
		else:
			return self.compressTeas(binaryIn[0:-5]) + self.make32(binaryIn[-5:])
	def explodeTeas(self, in32):
		binaryOut = ""
		teaList = []
		for c in in32:
			binaryOut += self.makeBinary(c)
		for c in range(len(binaryOut)):
			if binaryOut[c] == "1":
				teaList.append(self.dates[-c])
		return teaList
	def makeTd(self, content="test", align="L", color="black"):
		return '''<td class="text%s" style="color: %s">%s</td>''' % (align, color, content)
	def displayPerson(self, p):
		return ('''
<tr>%s %s %s %s</tr>
		''' % (self.makeTd(p["I"]), self.makeTd(p["N"],"L", "green"), self.makeTd(p["S"],"R", "blue"), self.makeTd(p["T"],"L", "purple")))
	def displayDate(self, d):
		return ('''
<tr>%s %s %s</tr>
		''' % (self.makeTd(d["I"]), self.makeTd(d["D"]), self.makeTd(d["L"])))

#tea = Tea()
#person = tea.people[69]
#print(person["N"])
#print(tea.explodeTeas(person))

#print(test.dates)
#for p in test.people:
#    p['T'] = test.compressTeas(p["T"])
#outfile = open('teaPeople.json', 'w')
#json.dump(test.people, outfile, default=utils.jdefault)
#outfile.close()
#print(test.compressTeas('11001100110011001100'))
#print(test.compressTeas('0000000100000000101111110111100000000'))
