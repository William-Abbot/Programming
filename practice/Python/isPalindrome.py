def isPal(biString, compString, n):
	tempString = ''
	n  -= 1
	for i in range(len(biString)):
		tempString += biString[n-i]
	result = True if tempString == compString else False
	return(result)