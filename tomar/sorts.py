# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 22:48:42 2016

@author: tomar
"""
import random

def mergeSort(L, counter):
#    print("sort", L, counter)
    if len(L) < 2:
        return (L, counter)
    counter += 1    
    middle = len(L)//2
    left = mergeSort(L[:middle], counter)
    right = mergeSort(L[middle:], counter)    
    return merge(left[0], right[0], counter)
def merge(L1, L2, counter):
#    print("merge",L1, L2, counter)
    result = []
    i, j = 0, 0
    while i < len(L1) and j < len(L2):
        counter += 1
        if L1[i] < L2[j]:
            result.append(L1[i])
            i += 1
        else:    
            result.append(L2[j])
            j += 1
    if i < len(L1):
        result += L1[i:]
    else:    
        result += L2[j:]
    counter += 1
#    print("return:", result, counter)    
    return (result, counter)    
def merge1(L1, L2, counter):
#    print(L1, L2, counter)
    result = []
    i, j = 0, 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            result.append(L1[i])
            i += 1
            counter += 1
        else:    
            result.append(L2[j])
            j += 1
            counter += 1
    while i < len(L1):
        result.append(L1[i])
        i += 1
        counter += 1
    while j < len(L2):    
        result.append(L2[j])
        j += 1
        counter += 1
    return (result, counter)    
def marieSort(L, counter):
#    print(L, str(counter))
    if len(L) < 2:
        return (L, counter)
    leftovers = []
    if L[0] < L[1]:
        minV = L[0]
        maxV = L[1]
    else:
        minV = L[1]
        maxV = L[0]
    counter += 2
    for j in range(2, len(L)):
        counter += 1
        if minV > L[j]:
            leftovers.append(minV)
            minV = L[j]
        elif maxV < L[j]:
            leftovers.append(maxV)
            maxV = L[j]
        else:
            leftovers.append(L[j])
    temp = marieSort(leftovers, counter) 
#   print([minV] + temp[0] + [maxV])
    return ([minV] + temp[0] + [maxV], temp[1])        
def selSort(L):
    counter = 0
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i+1
        while j < len(L):
            counter += 1
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp    
    return "selSort, " + str(len(L)) + ", " + str(counter)
def newSort(L):
    counter = 0
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            counter += 1
            j += 1                
    return "newSort, " + str(len(L)) + ", " + str(counter)
def flipSort(L):
    counter = 0
    flips = True
#    print(L, counter)
    while flips:
        flips = False
        for i in range(len(L)-1):
            counter += 1
            if L[i] > L[i + 1]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp
                flips = True
#                print(L, counter)
#    print(L, counter)
    return "flipsort, " + str(len(L)) + ", " + str(counter)
def swapSort(L): 
    """ L is a list on integers """
    counter = 0
#    print("Original L: ", L)
    for i in range(len(L)):
#        for j in range(i+1, len(L)):
        for j in range(len(L)):
            counter += 1
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
#                print(L)
#    print("Final L: ", L)
    return "swapSort, " + str(len(L)) + ", " + str(counter)
                    
test1 = [5, 1, 3, 8, 4, 9, 6, 2]
test2 = [5, 9, 43, 36, 72, 85, 91, 3, 18, 47, 1, 98, 42, 2, 58, 7, 31, 6, 4, 55, 789, 33, 85]
test3 = [1,3,5,7,9,11,13,15,17,19]
#t1 = mergeSort(test1[:] + test2[:] + test3[:],0)
test4 = []
for i in range(999):
    test4.append(random.randrange(9999))
t1 = mergeSort(test4[:],0)
t2 = marieSort(test4[:],0)
print("List length is", len(test4[:]), "mergeSort is", t1[1], "marieSort is", t2[1])
print("marieSort:", len(t2[0]))
print("mergeSort:", len(t1[0]))
#print(flipSort(test1[:]))
#print(selSort(test1[:]))
#print(newSort(test1[:]))
#print(swapSort(test1[:]))
#print("marieSort", len(test1), marieSort(test1[:],0)[1])
#print(flipSort(test2[:]))
#print(selSort(test2[:]))
#print(newSort(test2[:]))
#print(swapSort(test2[:]))
#print("marieSort", len(test2), marieSort(test2[:],0)[1])
#print(flipSort(test3[:]))
#print(selSort(test3[:]))
#print(newSort(test3[:]))
#print(swapSort(test3[:]))
