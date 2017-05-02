#!/Users/tomar/Anaconda3/python.exe
"""
Created on Mon Dec 26 14:28:31 2016

@author: tomar
"""
import utils
import json

with open("tmList.json") as uData:
	tmUsers = json.load(uData)
for u in tmUsers.keys():
    print(utils.scramble(tmUsers[u], 12))
