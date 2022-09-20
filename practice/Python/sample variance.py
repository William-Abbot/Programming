def sample_variance(array):
    buffer = 0
    mean = 1072006 
    n = len(array)


    for i in range(n):
        buffer += (array[i]-mean)**2

    result = buffer/(n-1)

    print(result)
    print("")
