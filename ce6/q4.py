#!/bin/python3
import numpy as np 

f=lambda x: 100*(x[1]-x[0]*x[0])**2 - (1-x[0])*(1-x[0])
g=lambda x: np.array([-400*(x[1]-x[0]*x[0])*x[0]+2*(1-x[0]),200*(x[1]-x[0]*x[0])])
x=np.array([0.5,0.5])
c=0.7
count=0
while np.linalg.norm(g(x))>1e-6:
    alpha=0.001
    while f(x)-alpha*c*g(x)@g(x)>f(x-alpha*g(x)):
        alpha=0.9*alpha
        #print(alpha)
    while f(x)-alpha*0.9*g(x)@g(x)>f(x-alpha*g(x)):
        alpha=1.1*alpha
    x=x-alpha*g(x)
    count+=1

print(count,x)

