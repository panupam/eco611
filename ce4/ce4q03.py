import numpy as np 
A=np.array([[1,0],[0,0],[0,1]]) 
B=np.zeros((A.shape[0],A.shape[0]))
B[:,:A.shape[1]]=A
u,z,v=np.linalg.svd(A)
for i in range(A.shape[1],A.shape[0]):
    B[:,i]=u[:,i]
    for j in range(i):
        B[:,i]=B[:,i]-B[:,i].dot(B[:,j])*B[:,j]

print("Orthonormal Matrix is \n", B)
print(B@B.T)