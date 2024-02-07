import numpy as np 
def lu(A):
    if A.shape[0]==1 :
        return np.array([[1]]), A
    else:
        if A[0,0]!=0:
            L=np.diag([1]*A.shape[0])
            L[1:,0]=A[1:,0]/A[0,0]
            A[1:,0]=A[1:,0]*0
            L2=np.zeros((A.shape[0],A.shape[0]))
            L2[0,0]=1
            L2[1:,1:],A[1:,1:]=lu(A[1:,1:])
            return L@L2, A
        else:
            if np.max(A[:,0])==np.min(A[:,0])==0:
                L2=np.zeros((A.shape[0],A.shape[0]))
                L2[0,0]=1
                L2[1:,1:],A[1:,1:]=lu(A[1:,1:])
                return L2, A
            else:
                pass

