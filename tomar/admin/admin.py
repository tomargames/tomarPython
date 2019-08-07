#!/Users/tomar/Anaconda3/python.exe
"""
Created on 1/13/2017
#!/usr/bin/python
#!/Users/tomar/Anaconda3/python.exe
@author: marie
"""
from __future__ import division
from __future__ import nested_scopes
from __future__ import generators
from __future__ import division
from __future__ import absolute_import
from __future__ import with_statement
from __future__ import print_function
from __future__ import unicode_literals
import sys
import os
try:
	import gUtils
	import Users
except:
	sys.path.append("..")
	import gUtils
	import Users
import cgi
import random
print("Content-type: text/html \n")
users = Users.Users()
print(users.authenticate('testG', 'testN', 'testM', 'testI', users.ADMIN))
print('</form></body></html>')