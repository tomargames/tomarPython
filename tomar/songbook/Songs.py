#!/Users/tomar/Anaconda3/python.exe
"""
Created on Sat May 27 16:34:21 2017 by tomar
#!/usr/bin/python3
#!/Users/tomar/Anaconda3/python.exe
"""
import json
import sys
import codecs
try:
	import gUtils
	import utils
except:
	sys.path.append("..")
	import gUtils
	import utils

class Songs(object):
	def __init__(self):
		'''
cardDict records are lists of:
[0] title
[1] deck
[2] list of tags -- from the notes table
[3] wikipedia link
[4] lyrics link
[5] time
[6] songbook -- file name in media folder
[7] notes --from the notes table
tag types:
	A artist
	B beats per minute
	C collection
	G genre
	H hit chart position peak
	K key
	M miscellaneous musical things
	O capo position
	Q polarity
	S source
	Y year
	Z harmonica key
		'''
		with codecs.open("marieSongBook.json",'r',encoding='utf8') as cards:
			cardDict = json.load(cards)
			self.tagGroup = {"A":"Artist",
						"B":"BPM",
						"C":"Collection",
						"G":"Group",
						"H":"BB",
						"K":"Key",
						"M":"Misc",
						"O":"C",
						"Q":"P",
						"S":"People",
						"Y":"Year",
						"Z":"Hm"}
		self.tagOrder = ["A", "Y", "G", "H", "C", "K", "B", "M", "Q", "O", "Z", "S"]
		self.tagDict = {}		# contains a list of cardIds
		self.deckDict = {}		# tuple: [0] is a list of cardIds, [1] is a list of tags
		self.songDict = {}		# each entry is a dict version of the list loaded from json
		self.tagData = {"A": ["cornflowerblue", "indigo", "Artist"],
					 "C": ["lightcyan", "darkcyan", "Album"],
					 "G": ["lightgreen", "darkgreen", "Group"],
					 "S": ["lightcoral", "darkred", "Person"],
					 "Y": ["lightgoldenrodyellow", "darkgoldenrod", "Year"],
					 "Z": ["lightcyan", "darkcyan", "Hmnca"]}
		self.publicTags = ["A", "C", "H", "Y"]
		self.marked = []
		# structure of tagDict is {type: {tag: [id, id, id]}}
		for c in cardDict:
			self.songDict[c] = {}
			self.songDict[c]["Title"] = cardDict[c][0]
			self.songDict[c]["Deck"] = cardDict[c][1]
			self.songDict[c]["Tags"] = cardDict[c][2]
			self.songDict[c]["Wiki"] = cardDict[c][3]
			self.songDict[c]["Lyrics"] = cardDict[c][4]
			self.songDict[c]["Time"] = cardDict[c][5]
			self.songDict[c]["SB"] = cardDict[c][6]
			self.songDict[c]["Notes"] = cardDict[c][7]
			if self.songDict[c]["Deck"] not in self.deckDict:
				self.deckDict[self.songDict[c]["Deck"]] = ([], [])
			self.deckDict[self.songDict[c]["Deck"]][0].append(c)
			for t in self.songDict[c]["Tags"]:
				type = t[0:1]
				tag = t[1:]
				if "marked" == t:
					self.marked.append(c)
#				elif type not in self.tagOrder:
#					print("unknown type {}".format(type))
				if type in self.tagDict:
					if tag in self.tagDict[type]:
						self.tagDict[type][tag].append(c)
					else:
						self.tagDict[type][tag] = [c]
						self.deckDict[self.songDict[c]["Deck"]][1].append(t)
				else:
					#print("type is {}, tag is {}, c is {}".format(type, tag, c))
					self.tagDict[type] = {}
					self.tagDict[type][tag] = [c]
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
		colors = ['pink', 'hotpink', 'plum', 'mediumpurple', 'lightsalmon', 'lightcoral',
		'khaki', 'yellow', 'palegreen', 'yellowgreen', 'lightblue','lightskyblue']
		dTags = sorted(self.tagDict[type])
		columns = 7
#		divide into 6 columns, make each a cell
		col = int(len(dTags)/columns)
		if len(dTags) % columns > 0:
			col += 1
		# print('{} items, split into {} columns of {} each'.format(len(self.tagDict[type]), columns, col))
		for i in range(columns):
			returnHtml += '<td><table>'
			for j in range(col):
				idx = i * col + j
				if  idx >= len(dTags):
					break
				#print('i is {}, j is {}, idx is {}'.format(i, j, idx))
				numberOfSongs = len(self.tagDict[type][dTags[idx]])
				returnHtml += '<tr><td style="background-color: {}">'.format(colors[int(numberOfSongs / 10)])
				returnHtml += '<a href=javascript:fetch("T{}")>{} ({})</a></td></tr>'.format(type+dTags[idx], dTags[idx], numberOfSongs)
			returnHtml += '</table></td>'
		returnHtml += '</tr></table></div>'
		return returnHtml
	def deckList(self, cDecks):
		returnHtml = '<table><tr>'
		col = "#87CEFA"
		cTotal = 0
		decksHtml = ''
		for d in sorted(self.deckDict):
			if col == "#87CEFA":
				col = "#BA55D3"
			else:
				col = "#87CEFA"
			if cDecks[0] == '1':
				checked = " checked "
				cTotal += len(self.deckDict[d][0])
			else:
				checked = ''
			cDecks = cDecks[1:]
			dLink = '<a href=javascript:fetch("D{}")>{}</a>'.format(d, d)
			decksHtml += '''
<td style="background-color: {}; padding: 5px;">{} ({})<input type="checkbox" onchange=checkDecks() id="c{}" {}></td>
				'''.format(col, dLink, len(self.deckDict[d][0]),d, checked)
		returnHtml += '<td style="background-color: #87CEFA; padding: 5px;">Decks: ({})</td>{}</tr></table>'.format(cTotal, decksHtml)
		return returnHtml
	def browse(self, authT, cDecks):
		returnHtml = deckList(cDecks)
		for t in self.tagOrder:
			if (t in self.publicTags) or (authT == '1'):
				returnHtml += self.displayTagsByType(t)
		return returnHtml
	def tagsToUse(self, perm):
		if perm == 1:
			return self.publicTags[:]
		else:
			return self.tagOrder[:]
	def displaySong(self, id, perm):
		returnHtml = self.displaySongList([id], perm)[0]
		if perm == 3:
			returnHtml += '<br><span style="font-size: 1.2em; color: darkgreen; font-weight: bold;>"'
			returnHtml += self.songDict[id]["Notes"]
			returnHtml += '</span>'
		return returnHtml
	def displaySongList(self, L, perm):
		''' L is a list of songIds
			output is a <table> with a <tr> for each song in the list
			format of each line will be [title link to detail][deck id][list of tags]
		'''
		#print("in displaySongList, perm is {} ".format(perm))
		columnColors = ["green", "red", "black", "purple", "blue", "darkgoldenrod"]
		rowColors = ["beige","lightcyan"]
		returnHtml = '<table id="detailTable" border=1 width=100%><thead>'
		returnHtml += '<tr class="songHeader" style="background-color: mistyrose;">'
		returnHtml += '<th><a style="color: {};" href="javascript:sortTable(0);">Title ({})</a></th>'.format(columnColors[0], len(L))
		returnHtml += '<th><a style="color: {};" href="javascript:sortTable(1);">Deck</a></th>'.format(columnColors[1 % len(columnColors)])
		for n, t in enumerate(self.tagsToUse(perm)):
			returnHtml += '<th><a style="color: {};" href="javascript:sortTable({});">{}</a></th>'.format(columnColors[(n + 2) % len(columnColors)], n + 2, self.tagGroup[t])
		returnHtml += '<th><a style="color: black;" href="javascript:sortTable(14);">Time</a></th>'
		returnHtml += '<th style="color: {};">***</th></tr></thead><tbody>'.format(columnColors[5])
		wikiHtml = 'var wikiDisplays = {'
		lyricsHtml = 'var lyrics = {'
		if (perm > 1):
			mediaHtml = 'var mediaDisplays = {'
		else:
			mediaHtml = ''
		if (perm == 3):
			noteHtml = 'var noteDisplays = {'
		else:
			noteHtml = ''
		for s in L:			#for every song
			if (self.songDict[s]["Deck"] == "marieNme"):
				rowColor = 1
			else:
				rowColor = 0
			returnHtml += '<tr valign="top"class="songDetail" style="background-color: {};">'.format(rowColors[rowColor])
			returnHtml += '<td><a href=javascript:fetch("N{}"); style="color:{};">{}</a></td>'.format(s,columnColors[0 % len(columnColors)], self.songDict[s]["Title"])
			returnHtml += '<td><a href=javascript:fetch("D{}"); style="color: {};">{}</a></td>'.format(self.songDict[s]["Deck"], columnColors[1 % len(columnColors)], self.songDict[s]["Deck"])
			for n, t in enumerate(self.tagsToUse(perm)):
				returnHtml += '<td>'
				for tag in self.songDict[s]["Tags"]:			#for each tag that matches
					if (tag[0:1] == t):
						returnHtml += '<a href=javascript:fetch("T{}"); style="color:{};">{}</a><br>'.format(tag, columnColors[(n + 2) % len(columnColors)],tag[1:])
				returnHtml += '</td>'
			if self.songDict[s]["Time"] != '':				#time
				returnHtml += '<td class="songDetail" style="color: black;">{}</td>'.format(self.songDict[s]["Time"])
			else:
				returnHtml += '<td> </td>'
			returnHtml += '<td class="songDetail" style="color: green;">'
			if self.songDict[s]["Wiki"] != '':
				returnHtml += '<a class="songDetail" style="text-decoration: none;" href=javascript:openLink("{}")>W</a>'.format(self.songDict[s]["Wiki"])
				wikiHtml += '"{}": "{}", '.format(s, self.songDict[s]["Wiki"])
			if self.songDict[s]["Lyrics"] != '':
				returnHtml += '<a class="songDetail" style="text-decoration: none;" href=javascript:openLink("{}")>L</a>'.format(self.songDict[s]["Lyrics"])
				lyricsHtml += '"{}": "{}", '.format(s, self.songDict[s]["Lyrics"])
			if self.songDict[s]["SB"] != '':
				if (perm > 1):
					returnHtml += '<a class="songDetail" style="text-decoration: none;" href=javascript:showMedia("{}")>S</a>'.format(self.songDict[s]["SB"])
					mediaHtml += '"{}": "{}", '.format(s, self.songDict[s]["SB"])
			if self.songDict[s]["Notes"] != '':
				if perm == 3:
					returnHtml += '<a class="songDetail" style="text-decoration: none;" href=javascript:showNote("{}")>N</a>'.format(s)
					noteHtml += '"{}": "{}", '.format(s, self.songDict[s]["Notes"])
			if s in self.marked:
				returnHtml += '*'
			returnHtml += '</td>'
			returnHtml += '</tr>'
		returnHtml += '</tbody></table>'
		if (perm > 2):
			noteHtml += '}; '
		if (perm > 1):
			mediaHtml += '};'
		wikiHtml += '}; '
		lyricsHtml += '}; '
		return (returnHtml, noteHtml, wikiHtml, mediaHtml, lyricsHtml)
	def getSongsByTag(self, t, cDecks):
		tagged = self.tagDict[t[0]][t[1:]]		# all cards with that tag
		selDecks = []
		selCards = []
		for d in sorted(self.deckDict):
			if cDecks[0] == '1':
				selDecks.append(d)
			cDecks = cDecks[1:]
		for c in tagged:
			if self.songDict[c]["Deck"] in selDecks:
				selCards.append(c)
		return selCards
	def getSongsByDeck(self, t):
		return self.deckDict[t][0]
	def dataList(self, tag):
		returnHtml = '''<datalist id="{}List">'''.format(self.tagData[tag][2].lower())
		for t in sorted(self.tagDict[tag]):
			returnHtml += '''<option value="{}{}">{}({})</option>'''.format(tag, t, t, len(self.tagDict[tag][t]))
		returnHtml += '''</datalist>'''
		return returnHtml
	def searchBox(self, tag):
		return '''<input type="text" id="{}Search" list="{}List" onClick="javascript:searchTag('{}');" style="width:90px; color: {}; background-color: {};" placeHolder="{}s"><input type="button" style="color: {}; background-color: {}" value="{}" onClick="javascript:searchTag('{}');">'''.format(self.tagData[tag][2].lower(), self.tagData[tag][2].lower(), tag, self.tagData[tag][1], self.tagData[tag][0], self.tagData[tag][2].lower(), self.tagData[tag][0], self.tagData[tag][1],self.tagData[tag][2], tag)
	def jsFunctions(self, perm):
		returnHtml = '<script> var lastSortedCol = -1; '
		returnHtml += 'function checkDecks() { var val = ""; '
		for d in sorted(self.deckDict):
			returnHtml += '/* in deckDict loop for {} */'.format(d)

			returnHtml += 'if (document.getElementById("c{}").checked == true) '.format(d)
			returnHtml += '''
{
	val += '1';
}
else
{
	val += '0';
}
			'''
		returnHtml += ' document.gForm.decks.value = val; } '
		returnHtml += '''
// open media file in new window
function showMedia(x)
{
	window.open('/python/media/' + x);
}
function openLink(x)
{
	window.open(x);
}
function sortTable(col)
{
	//alert("coming in to sort " + col + ", last sorted was " + lastSortedCol);
	var table, rows, switching, i, x, y, shouldSwitch;
	table = document.getElementById("detailTable");
	switching = true;
	/*Make a loop that will continue until no switching has been done:*/
	while (switching)
	{
		switching = false;
		rows = table.getElementsByTagName("TR");
		/*Loop through all table rows (except the first, which contains table headers):*/
		for (i = 1; i < (rows.length - 1); i++)
		{
			shouldSwitch = false;
			/*Get the two elements you want to compare, one from current row and one from the next:*/
			x = rows[i].getElementsByTagName("TD")[col];
			y = rows[i + 1].getElementsByTagName("TD")[col];
			//check if the two rows should switch place:
			if (lastSortedCol == col)
			{
				if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase())
				{
					//if so, mark as a switch and break the loop:
					shouldSwitch= true;
					break;
				}
			}
			else if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase())
			{
				//if so, mark as a switch and break the loop:
				shouldSwitch= true;
				break;
			}
		}
		if (shouldSwitch)
		{
			/*If a switch has been marked, make the switch and mark that a switch has been done:*/
			rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
			switching = true;
		}
	}
	lastSortedCol = col;
}
function searchSongs()
{
	if (document.getElementById("songSearch").value > "")
	{
		if (isNaN(document.getElementById("songSearch").value))
		{
			alert("Sorry, marie doesn't have that song on her list.");
		}
		else
		{
			fetch("N" + document.getElementById("songSearch").value);
		}
	}
}
function searchTag(x)
{
	var tagData = {"A": "artist", "C": "album", "G": "group", "S": "person", "Y": "year", "Z": "hmnca"};
	tag = document.getElementById(tagData[x] + "Search").value;
	if (tag > "")
	{
		fetch("T" + tag);
	}
}
function prcArtists()
{
	alert("prcArtists()");
}
function advancedSearch()
{
	dialog.showModal();
	if (dialog.returnValue > '')
	{
		dialog.addEventListener('close', doTaken);
	}
}
function fetch(x)
{
	gForm.oper.value = x;
	gForm.submit();
}
</script>
<input type="text" id="songSearch" list="songList" onClick="javascript:searchSongs();" style="width:180px; color: slateblue; background-color: lightsteelblue;" placeHolder="song titles">
<input type="button" style="color: lightsteelblue; background-color:slateblue;" value="Song" onClick="javascript:searchSongs();">
		'''
		returnHtml += self.searchBox("A")
		if perm > 1:
			returnHtml += self.searchBox("G")
			returnHtml += self.searchBox("Y")
			returnHtml += self.searchBox("S")
			returnHtml += self.searchBox("C")
			returnHtml += self.searchBox("Z")
		if perm == 3:
			returnHtml += '''
<input type="button" style="color: azure; background-color:cornflowerblue;" value="Marked" onClick="javascript:fetch('M');">
<a href="javascript:advancedSearch();">More</a>
		'''
		returnHtml += '''
<datalist id="songList">
		'''
		for c in sorted(self.songDict):
			returnHtml += '''<option value="{}">{}</option>'''.format(c, self.songDict[c]["Title"])
		returnHtml += '''</datalist>'''
		returnHtml += self.dataList("A")
		if perm > 1:
			returnHtml += self.dataList("G")
			returnHtml += self.dataList("Y")
			returnHtml += self.dataList("S")
			returnHtml += self.dataList("C")
			returnHtml += self.dataList("Z")
		returnHtml += '''
<dialog id="dialog" style="background-color: lightsteelblue;">
<form method="dialog">
		'''
		#returnHtml += this.deckList(decks))
		returnHtml += '''
<select name="selArtists" multiple>
		'''
		for a in self.tagDict["A"]:
			returnHtml += '''<option value="A{}">{}</option>'''.format(a, a)
		returnHtml += '''
</select>
<input type="button" value="sel" onClick="javascript:prcArtists();">
<button id="cancel" value="">Cancel</button>
</form></dialog>
		'''
		return returnHtml

songbook = Songs()
#songbook.jsFunctions(3)