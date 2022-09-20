#!pyhton3
#isValid.py
#william Abbot

from . import stringToLocation as stl
import re


#This Function checks to see if the given candidate(digit) at the
#   entered location is legal given the rules of Sudoku. If there 
#   are 1 or more occurences of the candidate in it's block, row, 
#   or column, or row, then it returs false
def isValid(digits_list, location, candidate):
    l_string = location #location string (just doing this to make the data type clear)
    digits = digits_list #list of all digits in board, has size of 81
    number = stl.getNumber(l_string) #location number
    letter = stl.getLetter(l_string) #location letter
    candidate = int(candidate) #ensure integerness
    
    current_block = getBlock(digits, number, letter)
    current_row = getRow(digits, number, letter)
    current_column = getColumn(digits, number, letter)
    if (candidate in current_block or candidate in current_row or candidate in current_column):
        return False
    return True


#returns the values of all squares within the same block that
#   the current square is in
def getBlock(digits, number, letter):
    block = [0]*9
    counter = 0
    arr = [1, 4, 7]
    n = len(arr)
    letterInt = (ord(letter)-64)
    
    #round the number and letter to the beginning of the current block
    rounded_number = floorSearch(arr, 0, n-1, number)
    rounded_letter = floorSearch(arr, 0, n-1, letterInt)
    
    for x in range(rounded_number, rounded_number + 3):
        for y in range(rounded_letter, rounded_letter + 3):
            lst = [chr(y+64), str(x)]
            l_string = ''.join(lst)
            index = stl.stringToLocation(l_string)
            block[counter] = digits[index]#get the value at (x, y) and put it in block[]
            counter += 1
    return block

#returns the values of all squares (cells) in the same row as
#   the letter input, as a list
def getRow(digits, number, letter):
    row = [0]*9
    for i in range(1, 10):
        number = i
        lst = [letter, str(number)]
        index = stl.stringToLocation("".join(lst))
        row[i-1] = digits[index]
    return row

#returns the values of all squares (cells) in the same column as
#   the letter input, as a list
def getColumn(digits, number, letter):
    column = [0]*9
    letter_num = (ord(letter)-65)
    for i in range(0, 9):
        letter_num = i
        lst = [chr(letter_num+65), str(number)]
        index = stl.stringToLocation("".join(lst))
        column[i] = digits[index]
    return column


# Function to get index of floor
# of x in arr[low..high]
def floorSearch(arr, low, high, x):  
    # If low and high cross each other  
    if (low > high):  
        return -1
  
    # If last element is smaller than x  
    if (x >= arr[high]):  
        return arr[high]
  
    # Find the middle point  
    mid = int((low + high) / 2)  
    
    # If middle point is floor.  
    if (arr[mid] == x):
        return arr[mid]
  
    # If x lies between mid-1 and mid  
    if (mid > 0 and arr[mid-1] <= x  
                and x < arr[mid]):  
        return arr[mid - 1]
  
    # If x is smaller than mid,  
    # floor must be in left half.  
    if (x < arr[mid]):  
        return floorSearch(arr, low, mid-1, x)  
  
    # If mid-1 is not floor and x is greater than  
    # arr[mid],  
    return floorSearch(arr, mid+1, high, x) 
