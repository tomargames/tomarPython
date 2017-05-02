#!/Users/tomar/Anaconda3/python.exe
"""
Created on 2017-02-26
#!/usr/bin/python
#!/Users/tomar/Anaconda3/python.exe
"""
import json
import utils
import string

class user(object):
	def __init__(self):
		'''
		file will have I, N, and P
		object will unscramble to id, name, and pword
		'''
		with open("userList.json") as uData:
			self.users = json.load(uData)
		for u in self.users:
			u["name"] = utils.scramble(u["N"][:], -7)
			u["pword"] = utils.scramble(u["P"][:], -7)
			gnum = ''
			for n in u["I"]:
				gnum += str(string.ascii_lowercase[:].find(n))
			u["id"] = gnum
	def saveUserList(self):
		with open("userList.json") as outfile:
			json.dump(self.users, outfile, default=utils.jdefault)
	def isRegisteredUser(self, uId):
		'''
		scrambles uId and then checks for it
		'''
		i = utils.scramble(uId[:], 7)
		print('''
		in isRegisteredUser, uId coming in is %s, looking for %s
		''' % uId, i)
		for u in self.users:
			if i == u["I"]:
				return True
		return False
	def encodeID(self, uId):
		gnum = ''
		for num in uId:
			gnum += string.ascii_lowercase[:][int(num):int(num)+1]
		return gnum
	def registerUser(self, uId, gName, pword):
		if pword not in ['teawithdeeandmarie']:
			with open('pending.txt', 'a') as pendingUsers:
				pendingUsers.write(''' %s : %s ''' % (uId, gName))
			return False
		newrec = {}
		newrec["I"] = uId
		newrec["P"] = utils.scramble(pword, 7)
		newrec["N"] = utils.scramble(gName, 7)
		self.users.append(newrec)
		self.saveUserList()
		return True
#test = user().users
#print(test)
#print(test.isRegisteredUser('106932376942135580175'))
#print(test.encodeID('106932376942135580175'))
#outfile = open('userList.json', 'w')
#json.dump(test.users, outfile, default=utils.jdefault)
#outfile.close()
