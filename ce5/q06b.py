import numpy as np 
x=[0.2,0.2,0.2]
J=lambda x:np.array([[-2*np.sum(x)*x[0]-2*(x[0]+np.sum(x)),-2*np.sum(x)*x[1]-2*x[0],-2*np.sum(x)*x[2]-2*x[0]],[-2*np.sum(x)*x[0]-2*x[1],-2*np.sum(x)*x[1]-2*(x[1]+np.sum(x)),-2*np.sum(x)*x[2]-2*x[1]],[-2*np.sum(x)*x[0]-2*x[2],-2*np.sum(x)*x[1]-2*x[2],-2*np.sum(x)*x[2]-2*(x[2]+np.sum(x))]])
f=lambda x: np.array([1-np.sum(x)**2-2*x[0]*x[0]*np.sum(x) -0.5,1-np.sum(x)**2-2*x[1]*x[1]*np.sum(x) -0.5,1-np.sum(x)**2-2*x[2]*x[2]*np.sum(x) -0.5])

while np.sum(f(x)*f(x))>1e-6:
    x=x-np.linalg.inv(J(x))@f(x)

print(x)
