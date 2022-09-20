import math

def MaxSum(X, L, U):
    if L > U:
        return 0
    if L == U:
        return max(0, X[L]) # one-element vector
    M = math.floor((L+U)/2) # A is X[L..M], B is X[M+1..U]
    # Find max crossing to left
    sum = 0
    maxToLeft = 0
    for I in range(M, L-1, -1):
        sum = sum + X[I]
        maxToLeft = max(maxToLeft, sum)
    # Find max crossing to right
    sum = 0
    maxToRight = 0
    for I in range(M+1, U+1):
        sum = sum + X[I]
        maxToRight = max(maxToRight, sum)
    maxCrossing = maxToLeft + maxToRight
    
    maxInA = MaxSum(X,L,M)
    maxInB = MaxSum(X,M+1,U)
    return max(maxCrossing, maxInA, maxInB)