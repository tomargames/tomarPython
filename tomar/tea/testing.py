#!/Users/tomar/Anaconda3/python.exe
"""
Created on Sun Jan 22 20:26:57 2017 by tomar
#!/usr/bin/python
#!/Users/tomar/Anaconda3/python.exe
"""
import json

def hexToBinary(inHex):
    if len(inHex) == 1:
        return
def jdefault(o):
	return o.__dict__
with open("teaDates.json") as dData:
    dates = json.load(dData)
with open("teaPeople.json") as pData:
    people = json.load(pData)
#print(dates)
print(people[0])
# 2017ef00 = 0000000100000000101111110111100000000
#for daterec in people:
#    print(daterec)
#    newDateRec = {}
#    for thing in daterec:
#        if type(daterec[thing]) == dict:
#            newDateRec[thing] = daterec[thing]['0']
#        else:
#            newDateRec[thing] = daterec[thing]
#    newDateRecs.append(newDateRec)
#print(newDateRecs)
#outfile = open('tPeople.json', 'w')
#json.dump(newDateRecs, outfile, default=jdefault)
#outfile.close()
