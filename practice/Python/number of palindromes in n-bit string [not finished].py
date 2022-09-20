#function definitions
def isPal(biString):
	tempString = ''
	n = len(biString)-1
	for i in range(len(biString)):
		tempString += biString[n-i]
	result = True if tempString == biString else False
	return(result)

def printTheArray(arr, n):  
  
    for i in range(0, n):  
        print(arr[i], end = " ")  
      
    print() 


def generateAllBinaryStrings(n, arr, i):  
  
    if i == n: 
        printTheArray(arr, n)  
        return
      
    # First assign "0" at ith position  
    # and try for all other permutations  
    # for remaining positions  
    arr[i] = 0
    generateAllBinaryStrings(n, arr, i + 1)  
  
    # And then assign "1" at ith position  
    # and try for all other permutations  
    # for remaining positions  
    arr[i] = 1
    generateAllBinaryStrings(n, arr, i + 1) 

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
n = input("enter number of bits in each string: ")
finalList = createAll6bitStrings()

numOfPalindromes = 0
for i in range(len(finalList)):
	if isPal(finalList[i]):
		numOfPalindromes += 1

print(numOfPalindromes)