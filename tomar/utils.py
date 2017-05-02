#!/Users/tomar/Anaconda3/python.exe
from __future__ import division
from __future__ import nested_scopes
from __future__ import generators
from __future__ import division
from __future__ import absolute_import
from __future__ import with_statement
from __future__ import print_function
from __future__ import unicode_literals
"""
Created on Sun Dec  4 23:28:36 2016
#!/usr/bin/python
#!/Users/tomar/Anaconda3/python.exe
"""
import string
import time

def formatDate(inYYYYMMDD):
    return inYYYYMMDD[0:4]+"&ndash;"+formatNumber(inYYYYMMDD[4:6], 2)+"&ndash;"+formatNumber(inYYYYMMDD[6:], 2)

def formatNumber(num, length):
    """ this will pad a number with zeroes to length """
    return ("0" * length + str(num))[-length:]

def baseConvert(n, base):
   convertString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   if n < base:
      return convertString[n]
   else:
      return baseConvert(n//base,base) + convertString[n%base]
def jdefault(o):
	return o.__dict__
def escape(txt):
    """
    fix special characters for display in html
    """
    msgOut = ""
    for letter in txt[:]:
        if letter == '-':
            msgOut += '&ndash;'
        else:
            msgOut += letter
    return msgOut

def scramble(txt, n):
    code = {}
    letters = string.ascii_lowercase[:]
    for letter in letters:
        code[letter] = letters[(letters.index(letter) + n) % len(letters)]
        code[letter.upper()] = code[letter].upper()
    msgOut = ""
    for letter in txt[:]:
        if letter in code.keys():
            msgOut += code[letter]
        else:
            msgOut += letter
    return msgOut

def dateTime():
    """ this will return a tuple: YYYYMMDD, then HH:MM:SS """
    def mkStr(n):
        return str(time.localtime()[n])
    return (mkStr(0)+formatNumber(mkStr(1), 2)+formatNumber(mkStr(2), 2), formatNumber(mkStr(3), 2)+":"+formatNumber(mkStr(4), 2)+":"+formatNumber(mkStr(5), 2))

