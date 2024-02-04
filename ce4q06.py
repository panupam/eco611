import numpy as np 

A=np.array([[2,3,7],[1,1,5],[4,3,1]])
z=np.zeros(A.shape)

for i in range(A.shape[1]):
    if A[:,i].dot(A[:,i])>0:
        z[:,i]=A[:,i]
        for j in range(i):
            if z[:,j].dot(z[:,j])>0:
                z[:,i]=z[:,i]- z[:,i].dot(z[:,j])*z[:,j]/(z[:,j].dot(z[:,j]))

z_norm=np.array([np.sqrt(z[:,i].dot(z[:,i])) for i in range(A.shape[1])])
z[:,z_norm>0]=z[:,z_norm>0]/z_norm[z_norm>0]
print("Maximal set of linearly independent colums are \n", A[:,z_norm>0])
print("Orthonormal basis for colum space of A is",z)
