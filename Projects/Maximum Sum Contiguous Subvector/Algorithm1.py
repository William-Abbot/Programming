def Algorithm_1(X):
    maxSoFar = 0
    P = 0
    Q = len(X)-1
    for L in range(P, Q+1):
        for U in range(L, Q+1):
            sum = 0
            for I in range(L, U+1):
                sum += X[I]
                # sum now contains the sum of X[L..U]
            maxSoFar = max(maxSoFar, sum)
    return maxSoFar