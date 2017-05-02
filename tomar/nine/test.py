#!/Users/tomar/Anaconda3/python.exe
"""
Created on Thu Dec 15 23:37:54 2016
tm9Save -- will save progress on form
@author: tomar
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
if there is an open eqsave record for this id, replace it with a processed record
'''	
with open("eqsave.json") as uData:
    users = json.load(uData)
saveRecord = users[0]    
with open("eqs.json") as qData:
    questions = json.load(qData)
#print(saveRecord)
counters = {}
for q in questions:
    ch = int(saveRecord.get(q["K"], 0)) - 1
    print(''' %s %s ''' % (q["D"], saveRecord.get(q["K"], 0)))
    if q["S"][ch]["E"] in counters.keys():
        counters[q["S"][ch]["E"]] += 1
    else:    
        counters[q["S"][ch]["E"]] = 1
for c in sorted(counters.items(), key=lambda ect: ect[1], reverse=True):
    print("Enneagram Type: %s   Count: %s " % (c[0], c[1]))
