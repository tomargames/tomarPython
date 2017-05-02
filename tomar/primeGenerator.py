# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 22:32:31 2016

@author: tomar
"""

def genPrimes():
    """ yields the next prime number with each call to __next__
        a number is prime if (x % p) != 0 for all earlier primes """
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        print('last is %s' % last)
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last
p = genPrimes()
for i in range(10):
    print('call to genPrimes yields %s \n' % p.__next__())