from numpy import linalg as LA
import numpy as np

A = np.array([[4,1],[2,3],[5,4],[1,0]])

w,v = LA.eig(A)

print(w)
print(v)