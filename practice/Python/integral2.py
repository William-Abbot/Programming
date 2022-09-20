from math import cos, e

def y(x):
    return (e**(2*x))*cos(x)

def produceBigArray(start, stop, increment):
    lst = []
    size = int(abs((stop - start)/increment))
    x = start
    for i in range(size+1):
        lst.append(x)
        x += increment
    return lst

x = produceBigArray(0,10,0.1)
print(sum(y(x[i])*(x[i]-x[i-1]) for i in range(1,len(x))))