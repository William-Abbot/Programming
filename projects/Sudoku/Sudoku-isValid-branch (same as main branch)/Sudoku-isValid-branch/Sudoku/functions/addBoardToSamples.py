import io

string = input("enter a string of 81 numbers: ")

def delimenate(string):
	templist = []
	for i in string:
		templist.append(int(i))
	return templist

fileIn = open(r'..\sample boards.txt', "a")

fileIn.write("\n" + str(delimenate(string)) + "\n")

fileIn.close()
