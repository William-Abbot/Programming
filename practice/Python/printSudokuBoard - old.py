import sys

dots = " . . . "
border = "|"
block = border + dots + border + dots + border + dots + border
#sys.argv[1]
board = ''
top = "  +-------+-------+-------+"

LETTERS = ['' for i in range(9)]
for i in range(65, 74):
    LETTERS[i-65] = (chr(i))

NUMSTRING = '   '
for i in range(1, 10):
    NUMSTRING += str(i) + ' '
    if ((i)%3 == 0):
        NUMSTRING += '  '

#end setup

def printBlock(index):
    if(index == 1):
        index += 2
    if(index == 2):
        index += 4
    for i in range(index, (index+3)):
        print(LETTERS[i] + " " + block)

def printRow(i):
    print(top)
    printBlock(i)
    
def printBoard(digits):
    print(" " + NUMSTRING)
    for i in range(3):
        printRow(i)
    print(top)

printBoard([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0])
