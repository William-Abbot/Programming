def Algorithm_4(X):
    P = 0
    Q = len(X)-1
    
    maxSoFar = 0
    maxEndingHere = 0
    for I in range(P, Q+1):
        maxEndingHere = max(0, maxEndingHere + X[I])
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar