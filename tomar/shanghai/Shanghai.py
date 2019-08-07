#!/Users/tomar/Anaconda3/python.exe
"""
Created on Wed Mar  7 15:04:03 2018 by tomar
#!/usr/bin/python3
#!/Users/tomar/Anaconda3/python.exe

shanghai
"""
import sys
try:
	import Users
except:
	sys.path.append("..")
	import Users
import utils
import json

def aboutTheGame():
    print('''
<br>About the Game
<ul class=green10>
	<li>There are 4 copies each of 36 different tiles.</li>
	<li>Remove matching pairs of tiles by clicking on tiles that are free.</li>
	<li>Tiles are free if they can slide to the right or the left.</li>
	<li>"Find" button will highlight visible tiles with selected character.</li>
	<li>"Taken" button searches previously taken tiles of selected character, and offers option to restore to that point.</li>
	<li>Puzzles can be solved down to 0 tiles.</li>
</ul>
    ''')

class Shanghai(object):
	def __init__(self):
		self.symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
		self.names = {}
		self.images = {}
		self.tileData = self.loadTileData()
	def setUpScript(self, gid, oper):
		returnHtml = '<script>'
		returnHtml += 'var stringMessage = "{}"; '.format(oper)
		returnHtml += 'var tileReady = []; '
		returnHtml += 'var tileImage = []; '
		returnHtml += 'var tileName = []; '
		users = Users.Users()
		if (users.auth(gid, users.TEA)):
			returnHtml += 'var TEA = true; '
		else:
			returnHtml += 'var TEA = false; '
		iCnt = 0
		for u in utils.randomSubset(list(users.imageList(gid)), 36):
			returnHtml += 'tileReady["{}"] = false; '.format(self.symbols[iCnt])
			returnHtml += 'tileName["{}"] = "{}"; '.format(self.symbols[iCnt], u[0])
			returnHtml += 'tileImage["{}"] = new Image(); '.format(self.symbols[iCnt])
			returnHtml += 'tileImage["{}"].onload = function() '.format(self.symbols[iCnt])
			returnHtml += '{ '
			returnHtml += 'tileReady["{}"] = true; '.format(self.symbols[iCnt])
			returnHtml += '}; '
			returnHtml += 'tileImage["{}"].src = "{}"; '.format(self.symbols[iCnt], u[1])
			self.names[self.symbols[iCnt]] = u[0]
			self.images[self.symbols[iCnt]] = u[1]
			iCnt += 1
		returnHtml += '</script>'
		return returnHtml
	def recordGame(self, gid, moves):
		if moves == '':
			return "Welcome to Shanghai!"
		rec = {}
		rec["I"] = gid
		rec["T"] = utils.timeStamp()
		rec["M"] = moves
		with open("games.json") as gjson:
			games = json.load(gjson)
		games.append(rec)
		outfile = open('games.json', 'w')
		json.dump(games, outfile)
		outfile.close()
		return 'Congratulations! You solved it in {} moves!'.format(moves)
	def modalDisplay(self):
		returnHtml = ''
		returnHtml += '''
<dialog id="dialog" style="background-color: lightgray;">
<form method="dialog">
<p>Click on a tile to search for it.</p>
<table border="0"><tbody>
		'''
		for row in range(6):
			returnHtml += '<tr>'
			i = row
			while i < len(self.symbols):
				if i < len(self.names):
					tName = self.names[self.symbols[i]]
					tImage = '{} <img src="{}" alt="" width="30px" height="30px">'.format(self.symbols[i],
						self.images[self.symbols[i]])
				else:
					tImage = self.symbols[i]
					tName = ''
				returnHtml += '<td><button type="submit" style="background-color: beige; " value="{}">{} {}</button></td>'.format(self.symbols[i], tImage, tName)
				i += 6
			returnHtml += '</tr>'
		returnHtml += '</table><br><br><button id="cancel" value="">Cancel</button>'
		return returnHtml
	def loadTileData(self):
		return [
		"1  2  1  0  2  0  ",
		"1  3  1  1  3  0  ",
		"1  4  1  2  4  0  ",
		"1  5  1  3  5  0  ",
		"1  6  1  4  6  0  ",
		"1  7  1  5  7  0  ",
		"1  8  1  6  8  0  ",
		"1  9  1  7  9  0  ",
		"1  10 1  8  10 0  ",
		"1  11 1  9  11 0  ",
		"1  12 1  10 12 0  ",
		"1  13 1  11 0  0  ",
		"2  4  1  0  14 0  ",
		"2  5  1  13 15 89 ",
		"2  6  1  14 16 90 ",
		"2  7  1  15 17 91 ",
		"2  8  1  16 18 92 ",
		"2  9  1  17 19 93 ",
		"2  10 1  18 20 94 ",
		"2  11 1  19 0  0  ",
		"3  3  1  0  22 0  ",
		"3  4  1  21 23 0  ",
		"3  5  1  22 24 95 ",
		"3  6  1  23 25 96 ",
		"3  7  1  24 26 97 ",
		"3  8  1  25 27 98 ",
		"3  9  1  26 28 99 ",
		"3  10 1  27 29 100",
		"3  11 1  28 30 0  ",
		"3  12 1  29 0  0  ",
		"4  2  1  85 32 0  ",
		"4  3  1  31 33 0  ",
		"4  4  1  32 34 0  ",
		"4  5  1  33 35 101",
		"4  6  1  34 36 102",
		"4  7  1  35 37 103",
		"4  8  1  36 38 104",
		"4  9  1  37 39 105",
		"4  10 1  38 40 106",
		"4  11 1  39 41 0  ",
		"4  12 1  40 42 0  ",
		"4  13 1  41 87 0  ",
		"5  2  1  85 44 0  ",
		"5  3  1  43 45 0  ",
		"5  4  1  44 46 0  ",
		"5  5  1  45 47 107",
		"5  6  1  46 48 108",
		"5  7  1  47 49 109",
		"5  8  1  48 50 110",
		"5  9  1  49 51 111",
		"5  10 1  50 52 112",
		"5  11 1  51 53 0  ",
		"5  12 1  52 54 0  ",
		"5  13 1  53 87 0  ",
		"6  3  1  0  56 0  ",
		"6  4  1  55 57 0  ",
		"6  5  1  56 58 113",
		"6  6  1  57 59 114",
		"6  7  1  58 60 115",
		"6  8  1  59 61 116",
		"6  9  1  60 62 117",
		"6  10 1  61 63 118",
		"6  11 1  62 64 0  ",
		"6  12 1  63 0  0  ",
		"7  4  1  0  66 0  ",
		"7  5  1  65 67 119",
		"7  6  1  66 68 120",
		"7  7  1  67 69 121",
		"7  8  1  68 70 122",
		"7  9  1  69 71 123",
		"7  10 1  70 72 124",
		"7  11 1  71 0  0  ",
		"8  2  1  0  74 0  ",
		"8  3  1  73 75 0  ",
		"8  4  1  74 76 0  ",
		"8  5  1  75 77 0  ",
		"8  6  1  76 78 0  ",
		"8  7  1  77 79 0  ",
		"8  8  1  78 80 0  ",
		"8  9  1  79 81 0  ",
		"8  10 1  80 82 0  ",
		"8  11 1  81 83 0  ",
		"8  12 1  82 84 0  ",
		"8  13 1  83 0  0  ",
		"9  1  1  0  31 0  ",
		"9  16 1  0  0  0  ",
		"9  14 1  42 88 0  ",
		"9  15 1  87 0  0  ",
		"2  5  2  0  90 0  ",
		"2  6  2  89 91 0  ",
		"2  7  2  90 92 0  ",
		"2  8  2  91 93 0  ",
		"2  9  2  92 94 0  ",
		"2  10 2  93 0  0  ",
		"3  5  2  0  96 0  ",
		"3  6  2  95 97 125",
		"3  7  2  96 98 126",
		"3  8  2  97 99 127",
		"3  9  2  98 100128",
		"3  10 2  99 0  0  ",
		"4  5  2  0  1020  ",
		"4  6  2  101103129",
		"4  7  2  102104130",
		"4  8  2  103105131",
		"4  9  2  104106132",
		"4  10 2  1050  0  ",
		"5  5  2  0  1080  ",
		"5  6  2  107109133",
		"5  7  2  108110134",
		"5  8  2  109111135",
		"5  9  2  110112136",
		"5  10 2  1110  0  ",
		"6  5  2  0  1140  ",
		"6  6  2  113115137",
		"6  7  2  114116138",
		"6  8  2  115117139",
		"6  9  2  116118140",
		"6  10 2  1170  0  ",
		"7  5  2  0  1200  ",
		"7  6  2  1191210  ",
		"7  7  2  1201220  ",
		"7  8  2  1211230  ",
		"7  9  2  1221240  ",
		"7  10 2  1230  0  ",
		"3  6  3  0  1260  ",
		"3  7  3  1251270  ",
		"3  8  3  1261280  ",
		"3  9  3  1270  0  ",
		"4  6  3  0  1300  ",
		"4  7  3  129131141",
		"4  8  3  130132142",
		"4  9  3  1310  0  ",
		"5  6  3  0  1340  ",
		"5  7  3  133135143",
		"5  8  3  134136144",
		"5  9  3  1350  0  ",
		"6  6  3  0  1380  ",
		"6  7  3  1371390  ",
		"6  8  3  1381400  ",
		"6  9  3  1390  0  ",
		"4  7  4  0  142145",
		"4  8  4  1410  145",
		"5  7  4  0  144145",
		"5  8  4  1430  145",
		"9  16 1  0  0  0  "
			]
s = Shanghai()
