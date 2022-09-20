import re, functions.printSudokuBoard as printsb, functions.updateBoard as upsb
import functions.isValid as valid
#import functions.generate as gen

list1 = [5,0,1,0,0,0,0,9,6,0,0,0,0,9,0,0,5,0,0,0,0,0,0,5,2,0,7,4,9,0,1,0,0,0,7,0,0,0,0,0,0,7,0,0,0,1,3,0,0,0,0,0,2,0,3,0,4,0,5,9,0,0,0,0,2,8,0,7,1,0,4,0,7,6,5,8,2,0,0,0,0]
list2 = [0]*81

printsb.printBoard(list1)
print("\nHello!! Type \'help\' for a list of commands, otherwise, enjoy the game!\n")


next_move = ''
help_commands = {'<new value> <letter><number>': 'puts <new value> in specified cell', 'quit': 'quits game', 'generate': 'generates a random sudoku board for you'}


def delimenate(string):
	templist = []
	for i in string:
		templist.append(int(i))
	return templist


while(True):

    next_move = input("\n>>> ")
    print(" ")#print function prints the input to a NEW LINE, no need to has a \n here
    
    if next_move == 'help':
        print(help_commands)
        continue
    #if next_move == 'generate':
    #    
    if next_move == 'quit' or next_move == 'exit':
        break
    
    command_list = re.split(r'\s',next_move)
    
    try:
        result = valid.isValid(list1, command_list[1], command_list[0])
    except IndexError:
        print("invalid command\n")
        continue
    
    if result:
        printsb.printBoard(upsb.UpdateBoard(list1, command_list[1], command_list[0]))
    else:
        print("not a valid move\n")   


print("Thanks for playing!\n")