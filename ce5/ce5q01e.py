import numpy as np 

p,n=input("Enter positive and negative starting point for  8 -12x + 86x2 - 121x3 + 60x4 - 10x5:").split()
p,n=float(p),float(n)

f=lambda x: -10*x**5 +60*x**4-121*x**3+86*x**2-12*x+8
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