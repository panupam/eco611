import numpy as np 
import matplotlib.pyplot as plt

x=float(input("Input starting point for 3cos(x)-e^x"))

l,count=[],0

f=lambda x: 3*np.cos(x)-np.exp(x)
f1=lambda x: -3*np.sin(x)-np.exp(x)
while (np.abs(f(x))>1e-6):
    x=x-f(x)/f1(x)
    count+=1
    l.append(x)

y=np.arange(len(l))
plt.plot(y,l)

print("Root & val of 3cos(x)-e^x is",x ,f(x) )
print("No of Steps, ",count)
plt.show()
