import numpy as np 


f=lambda x,rho: -x[0]-x[1] + rho*(max(0,x[0]*x[0]+x[1]*x[1]-1)**2)/2
g=lambda x,rho: np.array([-1+x[0]*rho*max(0,x[0]*x[0]+x[1]*x[1]-1),-1+x[1]*rho*max(0,x[0]*x[0]+x[1]*x[1]-1)])
rho=1e6
x=np.array([0,0])
c=0.09
count_g=0
flag=False
while np.linalg.norm(g(x,rho))>1e-3:
    alpha=0.001 
    if(max(0,x[0]*x[0]+x[1]*x[1]-1)>0) or flag:
        alpha=1e-06
        if not flag:
            x=xp
            flag=True
    while (f(x,rho)-alpha*g(x,rho).dot(g(x,rho))>f(x-alpha*g(x,rho),rho)):
        alpha=0.5*alpha
    print(x)
    xp=x
    
    x=x-alpha*g(x,rho)
    
    count_g+=1

if(max(0,x[0]*x[0]+x[1]*x[1]-1)>0):
    print("False")
else:
    print(x,f(x,rho))