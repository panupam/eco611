import numpy as np  
a=input("Enter first vactor of coeffiecient:").split()
b=input("Enter second vactor of coeffiecient:").split()

m=np.array([int(i) for i in a])
n=np.array([int(i) for i in b])
mlen=m.size
nlen=n.size
m=np.append(m,np.zeros(nlen-1))
n=np.append(n,np.zeros(mlen-1))
out=np.array([])
for i in range(mlen+nlen-1):
    out=np.append(out,sum(m[:(i+1)]*n[i::-1]))
    
print(out)
