import numpy as np 
import matplotlib.pyplot as plt
#not correct
F1= lambda n,x,c : (x*(n+1)+(-x)**(n+1))/(2*n)-c-0.5
F2=lambda n,x,c: 0.5-c+(x*(n+1)-(x)**(n+1))/(2*n)
f=lambda n,x: (n+1)*(1-np.abs(x)**n)/(2*n)

n=2
u=np.random.rand(1000)
X=np.zeros(1000)
for i in range(1000):
    
    c=u[i]
    if c>0.5:
        x=0.1
        while np.abs(F2(n,x,c))>1e-6:
            x=x-F2(n,x,c)/f(n,x)
    else:
        x=-0.1
        while np.abs(F1(n,x,c))>1e-6:
            x=x-F1(n,x,c)/f(n,x)

    X[i]=x

x=np.arange(-1.0,1.0,0.01)
plt.hist(X,30,density=True)
plt.plot(x,f(n,x))
plt.show()