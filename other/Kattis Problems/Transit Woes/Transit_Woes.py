import sys
import math

def main():
    arr = input().split()
    s = int(arr[0])
    t = int(arr[1])
    n = int(arr[2])
    D = list(map(int, input().split()))#time it takes to walk from the ith bus' drop off point to the i+1th bus stop
    B = list(map(int, input().split()))#time on ith bus
    C = list(map(int, input().split()))#the ith bus arrives every C[i] interval time to the bus stop

    #print(s,t,n, sep = ', ')

    fullTime = t-s
    currentTime = 0
    for i in range(n):
        currentTime += D[i]
        ratio = currentTime/C[i]
        if ratio <= 1:
            currentTime += C[i]-currentTime
        else:
            currentTime += ((math.ceil(currentTime/C[i])*C[i])-currentTime)
        currentTime += B[i]
    currentTime += D[n]

    if fullTime >= currentTime:
        print("yes")
    else:
        print("no")
    

if __name__=="__main__":
    main()
