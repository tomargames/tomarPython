#!/Users/tomar/Anaconda3/python.exe
"""
Created on Sat May 27 16:34:21 2017 by tomar
#!/usr/bin/python
#!/Users/tomar/Anaconda3/python.exe
"""
import json
import sys
try:
	import gUtils
except:
	sys.path.append("..")
	import gUtils

class Songs(object):
	def __init__(self):
		'''
cardDict records are lists of:
[0] title
[1] deck
[2] list of tags -- from the notes table
[3] notes --from the notes table
[4] songbook -- file name in media folder
[5] wikipedia link
tag types:
	A artist
	B beats per minute
	C collection
	G genre
	H hit chart position peak
	K key
	M miscellaneous musical things
	O capo position
	P play list
	Y year
	Z harmonica key
security settings:
	authS gives you public tags + wikipedia link
	authT gives you all tags + media links
	authA gives you all of the above plus notes
		'''
#		with codecs.open("marieSongBook2.json",'r',encoding='utf8') as cards:
		with open("marieSongBook.json") as cards:
			self.cardDict = json.load(cards)
#		self.tagGroup = {"A":{"H":"Artist", "S":"1em", "F":"beige", "B":"green"}
		self.tagGroup = {"A":"Artist",
						"B":"BPM",
						"C":"Collection",
						"G":"Genre",
						"H":"Chart",
						"K":"Key",
						"M":"Music",
						"O":"Capo",
						"P":"PlayList",
						"Y":"Year",
						"Z":"Harmonica"}
		self.tagOrder = ["A", "Y", "G", "H", "C", "K", "B", "M", "P", "O", "Z"]
		self.tagDict = {}
		self.deckDict = {}
		self.publicTags = ["A", "C", "G", "H", "Y"]
		# structure of tagDict is {type: {tag: [id, id, id]}}
		for c in self.cardDict:
			for t in self.cardDict[c][2]:
				type = t[0:1]
				tag = t[1:]
				#if type not in self.tagOrder:
					#print("unknown type {}".format(type))
				if type in self.tagDict:
					if tag in self.tagDict[type]:
						self.tagDict[type][tag].append(c)
					else:
						self.tagDict[type][tag] = [c]
				else:
					#print("type is {}, tag is {}, c is {}".format(type, tag, c))
					self.tagDict[type] = {}
					self.tagDict[type][tag] = [c]
			# print('deck is {}'.format(self.cardDict[c][1]))
			if self.cardDict[c][1] in self.deckDict:
				self.deckDict[self.cardDict[c][1]].append(c)
			else:
				self.deckDict[self.cardDict[c][1]] = [c]
			# print('deckDict is {}'.format(self.deckDict))
		# ultimately, i'd like to sort this in descending length of list
		for type in self.tagDict:
			for tag in self.tagDict[type]:
				self.tagDict[type][tag] = sorted(self.tagDict[type][tag])
	def displayTagsByType(self, type):
		'''
		type appears as a link, with a hidden div of all the tags of that type
		'''
		returnHtml = '''
			<br><a class="textL" style="color: green; font-size: 1.2em;" href="javascript:;" onClick=javascript:toggleDiv("div{}")>{} ({})</a>
			'''.format(type, self.tagGroup[type], len(self.tagDict[type]))
		returnHtml += '<div id="div{}" style="display:none;";>'.format(type)
		returnHtml += '<table width=90%><tr valign=top>'
		dTags = sorted(self.tagDict[type])
		columns = 7
#		divide into 6 columns, make each a cell
		col = int(len(dTags)/columns)
		if len(dTags) % columns > 0:
			col += 1
		# print('{} items, split into {} columns of {} each'.format(len(self.tagDict[type]), columns, col))
		for i in range(columns):
			returnHtml += '<td>'
			for j in range(col):
				idx = i * col + j
				# print('i is {}, j is {}, idx is {}'.format(i, j, idx))
				if  idx >= len(dTags):
					break
				returnHtml += '<a href=javascript:fetch("{}")>{}</a><br>'.format(type+dTags[idx], dTags[idx])
			returnHtml += '</td>'
		returnHtml += '</tr></table></div>'
		return returnHtml
	def browse(self, sec):
		returnHtml = ''
		# returnHtml = '<table><tr>'
		# for d in self.deckDict:
			# returnHtml += '''<td><button class="buttonF" id="b{}" style="background-color: green; color: beige; font-size: 0.8em" value="in" onClick="toggleDeck('b{}')">{} ({})</button></td>'''.format(d, 
				# d, d, len(self.deckDict[d]))
		# returnHtml += '</tr></table>'
		for t in self.tagOrder:
			if (t in self.publicTags) or (sec == '1'):
				returnHtml += self.displayTagsByType(t)
		return returnHtml
	def displaySongList(self, L, secS, secT, secA):
		''' L is a list of songIds
			output is a <table> with a <tr> for each song in the list
			format of each line will be [title link to detail][deck id][list of tags]
		'''
		columnColors = ["green", "red", "black", "purple", "blue"]
		rowColors = ["beige","lightcyan"]
		returnHtml = '<table id="detailTable" border=1 width=100%>'
		returnHtml += '<tr class="songHeader" style="background-color: {};">'.format(rowColors[0])
		returnHtml += '<th><a style="color: {};" href="javascript:sortTable(0);">Title ({})</a></th>'.format(columnColors[0], len(L))
		returnHtml += '<th><a style="color: {};" href="javascript:sortTable(1);">Deck</a></th>'.format(columnColors[1 % len(columnColors)])
		for n, t in enumerate(self.tagOrder):
			if (t in self.publicTags) or (secT == '1'):
				returnHtml += '<th><a style="color: {};" href="javascript:sortTable({});">{}</a></th>'.format(columnColors[(n + 2) % len(columnColors)], n + 2, self.tagGroup[t])
		returnHtml += '<th style="color: {};">Links</th></tr>'.format(columnColors[4])
		wikiHtml = '<script>var wikiDisplays = {'
		if (secT == '1'):
			mediaHtml = 'var mediaDisplays = {'
		else:
			mediaHtml = ''
		if (secA == '1'):
			noteHtml = 'var noteDisplays = {'
		else:
			noteHtml = ''
		for s in L:			#for every song
			if (self.cardDict[s][1] == "marieNme"):
				rowColor = 1
			else:
				rowColor = 0
			returnHtml += '<tr valign="top"class="songDetail" style="background-color: {};">'.format(rowColors[rowColor])
			returnHtml += '<td style="color: {};">{}</td>'.format(columnColors[0 % len(columnColors)], self.cardDict[s][0])
			#returnHtml += '<td style="color: {};">{}</td>'.format(columnColors[1 % len(columnColors)], self.deckName[self.cardDict[s][1]])
			returnHtml += '<td style="color: {};">{}</td>'.format(columnColors[1 % len(columnColors)], self.cardDict[s][1])
			for n, t in enumerate(self.tagOrder):
				if (t in self.publicTags) or (secT == '1'):
					returnHtml += '<td>'
					for tag in self.cardDict[s][2]:			#for each tag that matches
						if (tag[0:1] == t):
							returnHtml += '<a href=javascript:fetch("{}"); style="color:{};">{}</a><br>'.format(tag, columnColors[(n + 2) % len(columnColors)],tag[1:])
					returnHtml += '</td>'
			if (secT == '1'):
				returnHtml += '<td class="songDetail" style="color: red;">'
				if self.cardDict[s][3] != '':
					returnHtml += '<a class="songDetail" style="text-decoration: none;" href=javascript:showNote("{}")>N</a>'.format(s)
					noteHtml += '"{}": "{}", '.format(s, self.cardDict[s][3])
				if self.cardDict[s][4] != '':
					returnHtml += '<a class="songDetail" style="text-decoration: none;" href=javascript:showPage("{}")>M</a>'.format(self.cardDict[s][4])
					mediaHtml += '"{}": "{}", '.format(s, self.cardDict[s][4])
				if self.cardDict[s][5] != '':
					returnHtml += '<a class="songDetail" style="text-decoration: none;" href=javascript:showWiki("{}")>W</a>'.format(self.cardDict[s][5])
					wikiHtml += '"{}": "{}", '.format(s, self.cardDict[s][5])
				returnHtml += '</td>'
			returnHtml += '</tr>'
		returnHtml += '</table>'
		if (secT == '1'):
			mediaHtml += '}; '
		if (secA == '1'):
			noteHtml += '}; '
		wikiHtml += '}; </script>'
		return (returnHtml, noteHtml, mediaHtml, wikiHtml)
	def getSongsByTag(self, t):
		return self.tagDict[t[0]][t[1:]]
	def getSongsByDeck(self, t):
		return self.deckDict[t]
songbook = Songs()
#l = songbook.getSongsByTag('AJoniMitchell')
#print(songbook.displaySongList(l, 3))
# print(songbook.browse(1))
# print(songbook.displayTagsByType('K'))
#for t in songbook.tagOrder:
#	print(songbook.displayTagsByType(t))
#l = songbook.displaySongList(songbook.getSongsByTag('ALauraNyro'), 3)
#printl)
