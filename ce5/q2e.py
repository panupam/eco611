import numpy as np 
x=float(input("Input starting point for cos(x)-x^3"))

f=lambda x: -10*x**5 +60*x**4-121*x**3+86*x**2-12*x+8
f1=lambda x: -50*x**4+24*x**3-363*x**2+172*x-12
while (np.abs(f(x))>1e-6):
    x=x-f(x)/f1(x)

print("Root & val of cos(x)-x^3 is",x ,f(x) )
