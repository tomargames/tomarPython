#!/Users/tomar/Anaconda3/python.exe
"""
Created on Mon Apr 16 10:06:29 2018 by tomar
#!/usr/bin/python3
#!/Users/tomar/Anaconda3/python.exe
sudoku
"""
import sys
try:
	import Users
except:
	sys.path.append("..")
	import Users
import utils
import json
import random

class Sudoku(object):
	def __init__(self):
		self.symbols = '123456789'
		self.names = {}
		self.images = {}
		self.puzzles = []
		self.templates = []
		with open("templates.json") as dData:
			self.templates = json.load(dData)
		with open("puzzles.json") as dData:
			self.puzzles = json.load(dData)
	def addPuzzle(self, sPuz, tPuz):
		self.puzzles.append(sPuz)
		self.templates.append(tPuz)
		outfile = open('puzzles.json', 'w')
		json.dump(self.puzzles, outfile)
		outfile.close()
		outfile = open('templates.json', 'w')
		json.dump(self.templates, outfile)
		outfile.close()
	def recordGame(self, gid, puzzleNum):
		if puzzleNum == '':
			return "Welcome to Sudoku!"
		rec = {}
		rec["I"] = gid
		rec["T"] = utils.timeStamp()
		rec["N"] = puzzleNum
		with open("games.json") as gjson:
			games = json.load(gjson)
		games.append(rec)
		outfile = open('games.json', 'w')
		json.dump(games, outfile)
		outfile.close()
		return 'You solved #{}!'.format(puzzleNum)
	def setUpAdmin(self, oper):
		returnHtml = '<script>'
		if (oper[0] == 'N'):
			rnd = int(oper[1:])
			returnHtml += 'var PUZZLE = "{}"; '.format(self.puzzles[rnd])
			returnHtml += 'var TEMPLATE = "{}"; '.format(self.templates[rnd])
			returnHtml += 'var PUZZLENUM = {}; '.format(rnd)
		elif (oper[0] == 'S'):
			returnHtml += 'var PUZZLENUM = "TEST"; '
			tpuz = ''
			for ch in oper[1:]:
				if (ch > '0'):
					tpuz += '1'
				else:
					tpuz += '0'
			returnHtml += 'var PUZZLE = "{}"; '.format(oper[1:])
			returnHtml += 'var TEMPLATE = "{}"; '.format(tpuz)
		elif (oper[0] == 'X'):
			if (len(oper) != 163):
				print('input length is {}, {}'.format(len(oper), oper))
				return 'ERROR'
			sp = oper[1:82]
			tp = oper[82:]
			self.addPuzzle(sp, tp)
#			returnHtml += 'var PUZZLENUM = {}; '.format(len(self.puzzles))
#			returnHtml += 'var PUZZLE = "{}"; '.format(sp)
#			returnHtml += 'var TEMPLATE = "{}"; '.format(tp)
			return (returnHtml + "window.location = 'http://localhost/python/sudoku.html'; </script>")
		else:
			return 'ERROR'
		returnHtml += 'var tileReady = []; '
		returnHtml += 'var tileImage = []; '
		returnHtml += 'var tileName = []; '
		returnHtml += 'var message = "TEST"; '
		returnHtml += 'var TEA = false; '
		returnHtml += '</script>'
		return returnHtml
	def setUpScript(self, gid, oper):
		returnHtml = '<script>'
		rnd = random.randrange(len(self.templates))
		returnHtml += 'var PUZZLE = "{}"; '.format(self.puzzles[rnd])
		returnHtml += 'var TEMPLATE = "{}"; '.format(self.templates[rnd])
		returnHtml += 'var PUZZLENUM = {}; '.format(rnd)
		returnHtml += 'var tileReady = []; '
		returnHtml += 'var tileImage = []; '
		returnHtml += 'var tileName = []; '
		returnHtml += 'var message = "{}"; '.format(oper)
		users = Users.Users()
		if (users.auth(gid, users.TEA)):
			returnHtml += 'var TEA = true; '
		else:
			returnHtml += 'var TEA = false; '
		iCnt = 0
		for u in utils.randomSubset(list(users.imageList(gid)), 9):
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


s = Sudoku()

