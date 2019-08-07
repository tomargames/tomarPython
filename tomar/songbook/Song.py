#!/Users/tomar/Anaconda3/python.exe
"""
Created on Sat May 27 16:34:21 2017 by tomar
#!/usr/bin/python3
#!/Users/tomar/Anaconda3/python.exe
"""
import json
import sqlite3
import sys
try:
	import utils
except:
	sys.path.append("..")
	import utils


'''
Converts anki data to json and stores it
Query returns list of tuples that become a list:
[0] title followed by notes field followed by songbook field -- from the notes table
[1] cardId -- from the cards table
[2] noteId  ---> this is the join field
[3] deckId -- from the cards table
[4] tags -- from the notes table

output file will be a dict by cardIndex, record is a List:
[0] title
[1] deck
[2] tagsList
[3] notes
[4] songbook field which will point to file in media folder
[5] wikipedia link
'''

conn = sqlite3.connect('collection.anki2')
c = conn.cursor()
dSel = "SELECT decks FROM col"
c.execute(dSel)
deckInfo = c.fetchall()
dInfo = json.loads(deckInfo[0][0])
deckDict = {}
#print(dInfo)
for d in dInfo:
    if dInfo[d]['name'][0:14] == 'music::marie::':
        deckDict[d] = dInfo[d]['name'][14:]
    elif dInfo[d]['name'][0:7] == 'music::':
        deckDict[d] = dInfo[d]['name'][7:]
    elif dInfo[d]['name'].find(' ') > -1:
        deckDict[d] = 'Current'
    else:
        deckDict[d] = dInfo[d]['name']
#print(deckDict)
sel = "SELECT b.flds, a.id, a.nid, a.did, b.tags"
sel += " FROM 'cards' a, 'notes' b where a.nid = b.id "
c.execute(sel)
cardList = sorted(c.fetchall())
cardDict = {}
cardNum = 0
for cl in cardList:
    temp = list(cl)   # now the tuple is a list
    #order of fields in temp[0] is
    #title, wiki, lyrics, ?, ?, notes
    #print(temp[0])
    if len(temp[0]) > temp[0].find('') + 1:
        temp.append(cl[0].split('')[1])   # now the notes are in [5]
        temp.append(cl[0].split('')[2])   # now the media are in [6]
        temp.append(cl[0].split('')[3])   # now the wiki link is in [7]
        temp.append(cl[0].split('')[4])   # now the lyrics link is in [8]
        temp.append(cl[0].split('')[5])   # now the lyrics link is in [9]
        temp[0] =   cl[0].split('')[0]    # title is now alone in [0]
    else:
        temp[0] = cl[0][0:-2] # strips delimiter from title
    if str(temp[3]) in deckDict:
        temp[3] = deckDict[str(temp[3])] # replace deckId with name from deckDict
    else:
        print("ERROR! {} not found for {}".format(temp[3], temp[0]))
    temp[4] = cl[4].split() # now tags are a list in [4]
    temp.pop(1) # remove cardId
    temp.pop(1) # remove noteId
    cardDict[utils.formatNumber(cardNum, 4)] = temp
    cardNum += 1
#outfile = open('marieSongBook.json', 'w')
outfile = open('marieSongBook.json', 'w', encoding='utf8')
#json.dump(cardDict, outfile)
json.dump(cardDict, outfile, ensure_ascii=False)
outfile.close()

