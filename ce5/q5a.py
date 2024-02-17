import numpy as np 
x=np.array([3,3])
f=lambda x: np.array([x[0]**0.2+x[1]**0.2-1,x[0]**0.1+x[1]**0.4-2])
J=lambda x: np.array([[0.2*x[0]**(-0.8),0.2*x[1]**(-0.8)],[0.1*x[0]**(-0.9),0.4*x[1]**(-0.6)]])
count=0
while np.linalg.norm(f(x))>1e-6:
    x=x-np.linalg.inv(J(x))@f(x)
    count+=1

print(x,f(x),count)
