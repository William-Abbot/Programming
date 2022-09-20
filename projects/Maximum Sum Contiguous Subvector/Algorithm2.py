def Algorithm_2(X):
    maxSoFar = 0
    P = 0
    Q = len(X)-1
    for L in range(P, Q+1):
        sum = 0;
        for U in range(L, Q+1):
            sum = sum + X[U]
            # sum now contains the sum of X[L..U]
            maxSoFar = max(maxSoFar, sum)
    return maxSoFar