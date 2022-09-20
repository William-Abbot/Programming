#!python3
#printSudokuBoard
#William Abbot

#takes in an array of size 81, representing the digits that fill the board, then,
#   with that array, creates a 9x9 sudoku grid.

import sys

#setup

#sys.argv[0]

LETTERS = ['' for i in range(9)]
for i in range(65, 74):
    LETTERS[i-65] = (chr(i)) #number to letter (ASCII)

NUMSTRING = '   '
for i in range(1, 10):
    NUMSTRING += str(i) + ' '
    if((i%3) == 0):
        NUMSTRING += '  '

#end setup

def getRowOfNumbers(list, row):
    templist = [0]*9
    #row is going to be in between 0 and 8, so it needs to be converted to
    #   the start of a range of indices in the list input that correspond
    #   to ith row on the sudoku board
    start = 9*row - 9
    for i in range(start, start + 9):
        #print(str(start+9)+"\n")
        templist[i-start] = list[i]

    #here, the row of digits is converted from a list to a string and is
    #   then formatted
    rowstring = " "
    for i in range(len(templist)):
        filteredString = ""
        if (templist[i] == 0):
            filteredString = "." #converting the 0's to .'s
        else:
            filteredString = str(templist[i])#convert list to string
        #format
        rowstring += filteredString + " "
        if((i+1)%3 == 0):
            rowstring += "| "
    return rowstring


#line by line, this function prints the sudoku board:
#   * numbers + cell borders
#   * at the first, the last, the fifth, and the 9th lines, print top lines
#   * LETTERS[i in rows] + rest of the row including input number[i in 81]
def printBoard(digits):
    rownum = 0
    for i in range(14):
        #print board line-by-line(14 lines in total)
        
        #1. print top numbers
        if(i==0):
            print(" " + NUMSTRING)
        
        #2. every third, including first, print top.
        elif(i == 1 or i == 5 or i == 9 or i == 13):
            print("  +-------+-------+-------+")
        
        #3. else, print each row (includes the letter on the side then the input
        #   digits with the cell walls in between)
            
        elif(rownum < 9): #make sure there is no out of range error
            letter = LETTERS[rownum]
            rownum += 1
            row = getRowOfNumbers(digits, rownum)
            print(letter + " |" + row)

