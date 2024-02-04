import numpy as np 

A=np.array([[2,3,7],[1,1,5],[4,3,1],[2,1,5]])
b=np.array([5,13,3,15]).reshape((4,1))
rA=np.linalg.matrix_rank(A)
rAb=np.linalg.matrix_rank(np.concatenate((A,b),axis=1))
print(rA,rAb)
if rA==rAb:
    if rA==A.shape[1]:
        s=np.linalg.pinv(A)@b
        print("Unique Solution \n",s)
    else:
        x=np.linalg.pinv(A)@b 
        u,s,v=np.linalg.svd(A)
        print("Infinite solution:",x, "+ one of the element of null space with basis") 
        print(v.T[:,rA:])
else:
    x=np.linalg.lstsq(A,b,rcond=None)
    print("No Solution, Best fit solution is",x[0].T,"\nand sum of squared error is", x[1])
