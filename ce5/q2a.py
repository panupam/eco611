import numpy as np 
x=float(input("Input starting point for cos(x)-x^3"))

f=lambda x: np.cos(x)-x**3 
f1=lambda x: -np.sin(x)-3*x**2
while (np.abs(f(x))>1e-6):
    x=x-f(x)/f1(x)

print("Root & val of cos(x)-x^3 is",x ,f(x) )
