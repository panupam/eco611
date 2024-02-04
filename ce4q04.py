import numpy as np 
A=np.array([[2,3,7],[1,1,5],[4,3,1]]) 
B=np.array([[1,1,1],[0,1,0],[1,1,0]])

rA=np.linalg.matrix_rank(A)
rB=np.linalg.matrix_rank(B)
rABT=np.linalg.matrix_rank(A@B.T)

if rA==rB and rA==rABT:
    print("Possible matrix is:\n",A@B.T)
else:
    print("Not Possible")