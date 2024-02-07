import numpy as np 
x=float(input("Input starting point for x^1/3-e^-x^2"))

f=lambda x: x**(1/3)-np.exp(-x*x)
f1=lambda x:x**(-2/3)/3+2*x*np.exp(-x*x)
while (np.abs(f(x))>1e-6):
    x=x-f(x)/f1(x)

print("Root & val of x^1/3-e^-x^2 is",x ,f(x) )
