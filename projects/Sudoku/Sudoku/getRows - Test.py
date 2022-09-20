import re

digits = [5,0,1,0,0,0,0,9,6,0,0,0,0,9,0,0,5,0,0,0,0,0,0,5,2,0,7,4,9,0,1,0,0,0,7,0,0,0,0,0,0,7,0,0,0,1,3,0,0,0,0,0,2,0,3,0,4,0,5,9,0,0,0,0,2,8,0,7,1,0,4,0,7,6,5,8,2,0,0,0,0]

number = 5
letter = chr(4+65)
letter_num = 4

#string_to_location converts the string input. which will be in the format [A-I][1-9]
#   into an index from 1 to 81, representing the location on the sudoku board
def string_to_location(string):
    pattern = re.compile(r'([ABCDEFGHI])(\d)') #creates a regex pattern
    mo = pattern.search(string)
    Letter = mo.group(1)
    Number = mo.group(2)

    location = int(Number) + (ord(Letter)-65)*9 #ord function converts a uncode(ASCII) letter to a number
    return location-1


def getColumn(digits, number, letter_num):
    column = [0]*9
    for i in range(0, 9):
        letter_num = i
        lst = [chr(letter_num+65), str(number)]
        index = string_to_location("".join(lst))
        column[i] = digits[index]
    return column

def getRow(digits, number, letter_num):
    row = [0]*9
    for i in range(1, 10):
        number = i
        lst = [chr(letter_num+65), str(number)]
        index = string_to_location("".join(lst))
        row[i-1] = digits[index]
    return row

column = getColumn(digits, number, letter_num)
row = getRow(digits, number, letter_num)
print(column)
print(row)
