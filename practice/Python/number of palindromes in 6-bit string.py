#function definitions
def isPal(biString):
	tempString = ''
	n = len(biString)-1
	for i in range(len(biString)):
		tempString += biString[n-i]
	result = True if tempString == biString else False
	return(result)

def createAll6bitStrings():
	bSet = {0, 1}
	finalList = ['']*64
	counter = 0
	for a in bSet:
		for b in bSet:
			for c in bSet:
				for d in bSet:
					for e in bSet:
						for f in bSet:
							binaryString = str(a)+str(b)+str(c)+str(d)+str(e)+str(f)
							finalList[counter] = binaryString
							counter += 1
	return finalList


#main program 
finalList = createAll6bitStrings()

numOfPalindromes = 0
for i in range(len(finalList)):
	if isPal(finalList[i]):
		numOfPalindromes += 1

print(numOfPalindromes)