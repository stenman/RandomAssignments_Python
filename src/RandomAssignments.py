'''
Created on 30 okt 2012

@author: Gildur
'''

import random
import sys

def ReadFileToList(file):
    nameList = []
    try:
        with open(file , encoding='utf-8') as a_file:
            for a_line in a_file:
                nameList.append(a_line.rstrip())
        return nameList
    except IOError as err:
        print ("No such file or directory: ", err)
        sys.exit(0)

def CopyList(aList):
    copiedList = []
    for x in aList:
        copiedList.append(x)
    return copiedList

def AssignListToDictValues(theList):
#TODO: 1. implement REAL error handling
#TODO: 2. Refactor!

    if len(set(theList)) >= 2:
        list1 = CopyList(set(theList))
        list2 = CopyList(set(theList))
    
        while list1[len(list1)-1] == list2[len(list2)-1]:
            random.shuffle(list2)
   
        theDict = {}
        for x in list1:
            theDict[x] = ""
    
        rejectedList = []
        for x in list1:
            for y in list2:
                if x == y:
                    continue
                elif rejectedList.__contains__(y):
                    continue
                else:
                    theDict[x] = y
                    rejectedList.append(y)
                    break
        return theDict
    else:
        print("List has to contain more than 1 name!")

def ShuffleList(aList):
    random.shuffle(aList)

#TODO: Add the option to read input from user    
nameList = ReadFileToList("c:\\Users\\Gildur\\workspace\\se.gildur.python.randomassignments\\participants.txt")

print("***** Christmas Present Assigning Program V0.1.10 *****\n")

nameDict = AssignListToDictValues(nameList)

print ("NAME",'\t\t',"BUY TO")
for x in nameDict.keys():
    if len(x) <= 6:
        print (x,'\t\t',nameDict[x])
    else:
        print (x,'\t',nameDict[x])
