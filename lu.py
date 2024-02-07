import numpy as np 
def ech(A):
    if A.shape[0]==1 :
        return np.zeros((1,1))
    else:
        m,n=A.shape
        if A[0,0]==0:
            if np.min(A[:,0])==np.max(A[:,0])==0:
                L=np.diag([1]*m)
                L1=np.zeros((m,m))
                L1[0,0]=1
                L1[1:,1:]=ech(A[1:,1:])
                return L@L1
                
            else:
                for i in range(m):
                    if A[i,0]!=0:
                        break 

                A[0,:],A[i,:]=A[i,:],A[0,:]
                return ech(A)

        else:
            
            v=A[1:,0].reshape((m-1,1)).copy()
            w=A[0,1:].reshape((1,n-1))
            A[1:,1:]=A[1:,1:]-v@w/A[0,0]
            A[1:,0]=A[1:,0]*0
            L=np.diag([1]*m)
            L1=np.zeros((m,m))
            L1[0,0]=1
            L1[1:,0]=v.T[0]
            L1[1:,1:]=ech(A[1:,1:])
            return L@L1
            

A=np.array([[1,1],[1,1],[2,3]],dtype=float) 
U=A.copy()
L=ech(U)
print("Printing L\n",L)
print("printing U\n",U)
print("Printing L@U\n",L@U)
print("Printing initial matrix\n",A)

