import numpy as np 
import matplotlib.pyplot as plt

f=lambda x: 4*x[0]**2-2*x[0]*x[1]+x[1]**2
g=lambda x: np.array([8*x[0]-2*x[1],-2*x[0]+2*x[1]])
x=np.array([-1,-1])


c=0.9
count_g=0
while np.linalg.norm(g(x))>1e-6:
    alpha=0.001 
    while (f(x)-alpha*g(x).dot(g(x))>f(x-alpha*g(x))):
        alpha=0.9*alpha
    
    x=x-alpha*g(x)
    count_g+=1

print(x,f(x),g(x))


z=np.arange(-10,10,0.01)
plt.plot(z,f(z))
plt.show()
