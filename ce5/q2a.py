import numpy as np 
import matplotlib.pyplot as plt
x=float(input("Input starting point for cos(x)-x^3"))

l,count=[],0
f=lambda x: np.cos(x)-x**3 
f1=lambda x: -np.sin(x)-3*x**2
while (np.abs(f(x))>1e-6):
    x=x-f(x)/f1(x)
    count+=1
    l.append(x)

y=np.arange(len(l))
plt.plot(y,l)

print("Root & val of cos(x)-x^3 is",x ,f(x) )
print("No of steps is ",count)
plt.show()
