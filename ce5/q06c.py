#not working 
import numpy as np 
x=[0.2,0.2,0.2]
J=lambda x:np.array([[-2,-1,-1],[-1,-4 ,-1],[-1,-1,-2 -6*x[2]]])
f=lambda x: np.array([-2*x[0]-x[1]-x[2],1-4*x[1]-x[0]-x[2],1-2*x[2]-x[1]-x[0]-3*x[2]*x[2]])

while np.sum(f(x)*f(x))>1e-6:
    x=x-np.linalg.inv(J(x))@f(x)
    x[x<0]=1e-6

print(x)
