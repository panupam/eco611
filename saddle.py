import numpy as np
a=input("Enter Matrix Dim:").split()
m,n=int(a[0]),int(a[1])
b=np.array([int(i) for i in input("Enter matrix data by row:").split()])
b=b.reshape((m,n))
k=[]
for i in range(m):
    for j in range(n):
        if (b[i,j]==max(b[i]) and b[i,j]==min(b[:,j]))or (b[i,j]==min(b[i]) and b[i,j]==max(b[:,j])):
            k.append((i,j))

print("Saddle points are ",[b[i] for i in k])


