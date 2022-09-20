#!python3
#updateBoard.py
#William Abbot

#This file contains the UpdateBoard function which will put a new value on your 
#   sudoku board at a specific location.

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



#UpdateBoard function will first, convert the location input to an index 
#   of the digits_list which has a size of 81, using the string_to_location 
#   function. Then, it will replace the element at that location with 
#   newValue input param.
def UpdateBoard(digits_list, location, newValue):
    index = stringToLocation(location)
    digits_list[index] = int(newValue)
    return digits_list
