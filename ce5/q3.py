import numpy as np 
import matplotlib.pyplot as plt

F= lambda x,c : 1-c - x*np.exp(-x)-np.exp(-x)
f=lambda x: x*np.exp(-x)


u=np.random.rand(1000)
X=np.zeros(1000)
for i in range(1000):
    x=1
    c=u[i]
    while np.abs(F(x,c))>1e-6:
        x=x-F(x,c)/f(x)
    
    X[i]=x


plt.hist(X,30,density=True)
plt.show()