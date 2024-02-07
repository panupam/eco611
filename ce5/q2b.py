import numpy as np 
x=float(input("Input starting point for 3cos(x)-e^x"))

f=lambda x: 3*np.cos(x)-np.exp(x)
f1=lambda x: -3*np.sin(x)-np.exp(x)
while (np.abs(f(x))>1e-6):
    x=x-f(x)/f1(x)

print("Root & val of 3cos(x)-e^x is",x ,f(x) )
