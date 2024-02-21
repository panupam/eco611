import numpy as np

f=lambda x,rho: 4*x[0]**2-2*x[0]*x[1]+x[1]**2+ rho*(max(0,x[0]+x[1]-1))**2/2
g=lambda x,rho: np.array([8*x[0]-2*x[1]+rho*max(0,x[0]+x[1]-1),-2*x[0]+2*x[1]-rho*max(0,x[0]+x[1]-1)])
x=np.array([0.1,0.1])
c=0.1
count_g=0
rho=1e6
while np.linalg.norm(g(x,rho))>1e-6:
    alpha=0.1 
    while (f(x,rho)-alpha*g(x,rho).dot(g(x,rho))>f(x-alpha*g(x,rho),rho)):
        alpha=0.9*alpha
    #print(x)
    x=x-alpha*g(x,rho)
    count_g+=1

print(x,f(x,0),count_g)

# Conjugate Gradient Inexact line search 
    
x=np.array([0.1,0.1])
c=0.7
count_cg=0
d=-g(x,rho)
while np.linalg.norm(g(x,rho))>1e-6:
    alpha=0.1
    while f(x,rho)+alpha*d.dot(g(x,rho))>f(x+alpha*d,rho):
        alpha=0.9*alpha
    x_p=x
    x=x+alpha*d
    if count_cg%2==0:
        d=-g(x,rho)+g(x,rho).dot(g(x,rho))/g(x_p,rho).dot(g(x_p,rho)) *d 
        count_cg+=1
    else:
        d=-g(x,rho)
        count_cg+=1
    

print(x,f(x,0),count_cg)