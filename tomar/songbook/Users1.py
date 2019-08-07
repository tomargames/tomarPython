#!/Users/tomar/Anaconda3/python.exe
"""
Created on Wed Oct  4 22:29:16 2017 by tomar
#!/usr/bin/python
#!/Users/tomar/Anaconda3/python.exe
"""
import json

class Users(object):
	def __init__(self):
		'''
json file will be a dict by googleId, record is a List:
[0] user name
[1] user level

user level values:
        0 is a guest
        1 is a user
        2 is a user i know
        3 is full privileges
		'''
		with open("users.json") as users:
			self.userDict = json.load(users)
		self.userTypes = ["Guest", "Welcome!", "Friend", "Owner"]
	def writeToPending(self, id, name):
		outfile = open('pending.txt', 'a')
		outfile.write('''
		{}: {} '''.format(id, name))
		outfile.close()
#u = Users()
