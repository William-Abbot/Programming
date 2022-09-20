import math
def length(vector, length):
    result = 0
    for i in range(length):
        result += vector[i]**2
    result = math.sqrt(result)
    return result

if __name__ == "__main__":
    vector_string = input("enter in vector as a comma seperated list: ")
    vector_string = vector_string.split(',')
    #print(vector_string)
    vector = [0]*len(vector_string)
    count = 0
    for i in vector_string:
        vector[count] = int(i)
        count += 1
    #print(vector)
    print(length(vector,len(vector)))
    
