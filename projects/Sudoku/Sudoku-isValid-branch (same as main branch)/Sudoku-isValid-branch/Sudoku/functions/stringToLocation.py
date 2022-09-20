#!python3
#stringToLocation.py
#William Abbot

import re

#string_to_location converts the string input. which will be in the format [A-I][1-9]
#   into an index from 1 to 81, representing the location on the sudoku board
def stringToLocation(string):
    pattern = re.compile(r'([ABCDEFGHI])(\d)') #creates a regex pattern
    mo = pattern.search(string)
    Letter = mo.group(1)
    Number = mo.group(2)
    
    location = int(Number) + (ord(Letter)-65)*9 #ord function converts a uncode(ASCII) letter to a nuber
    return location-1


def getNumber(string):
    pattern = re.compile(r'([ABCDEFGHI])(\d)') #creates a regex pattern
    mo = pattern.search(string)
    number = mo.group(2)
    return int(number)

def getLetter(string):
    pattern = re.compile(r'([ABCDEFGHI])(\d)') #creates a regex pattern
    mo = pattern.search(string)
    letter = mo.group(1)
    return letter