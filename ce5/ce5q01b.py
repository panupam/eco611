import numpy as np 

p,n=input("Enter positive and negative starting point for 3cos(x)-e^x:").split()
p,n=float(p),float(n)

f=lambda x: 3*np.cos(x)-np.exp(x)
if f(p)*f(n)>0:
    print("invalid input") 
    exit()

if f(p)<0:
    p,n=n,p


while np.abs(f((p+n)/2))>1e-6:
    if f((p+n)/2) >0:
        p=(p+n)/2
    else:
        n=(p+n)/2

print((p+n)/2,f((p+n)/2))