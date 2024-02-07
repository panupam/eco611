import numpy as np 
x=[0.2,0.2,0.2]
J=lambda x:np.array([[-2 -1/x[0],-1,-1],[-1,-2 -1/x[0],-1],[-1,-1,-2 -1/x[0]]])
f=lambda x: np.array([-np.log(x[0])-2*x[0]-x[1]-x[2],-np.log(x[1])-2*x[1]-x[0]-x[2],-np.log(x[2])-2*x[2]-x[1]-x[0]])

while np.sum(f(x)*f(x))>1e-6:
    x=x-np.linalg.inv(J(x))@f(x)

print(x)
