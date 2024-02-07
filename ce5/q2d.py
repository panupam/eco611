import numpy as np 
x=float(input("Input starting point for x**4-3*x**3+4*x**2+5*x-2"))

f=lambda x: x**4-3*x**3+4*x**2+5*x-2
f1=lambda x: 4*x**3-9*x**2+8*x+5
while (np.abs(f(x))>1e-6):
    x=x-f(x)/f1(x)

print("Root & val of x**4-3*x**3+4*x**2+5*x-2 is",x ,f(x) )
