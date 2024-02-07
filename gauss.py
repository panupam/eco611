import numpy as np 
def ech(A):
    if A.shape[0]==1 :
        return 
    else:
        m,n=A.shape
        if A[0,0]==0:
            if np.min(A[:,0])==np.max(A[:,0])==0:
                ech(A[1:,1:])
            else:
                for i in range(m):
                    if A[i,0]!=0:
                        break 

                A[0,:],A[i,:]=A[i,:],A[0,:]
                ech(A)
        else:
            
            v=A[1:,0].reshape((m-1,1))
            w=A[0,1:].reshape((1,n-1))
            A[1:,1:]=A[1:,1:]-v@w/A[0,0]
            A[1:,0]=A[1:,0]*0
            ech(A[1:,1:])

A=np.array([[1,1],[1,1],[2,3]],dtype=float) 
B=A.copy()
ech(B)
print(B)
