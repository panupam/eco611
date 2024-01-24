import numpy as np
import numpy.random as random 
import matplotlib.pyplot as plt

a=random.rand(10000)
b=np.zeros(10000)
for i in range(10000):
    if a[i]>0.5:
        b[i]=1-np.sqrt(2*(1-a[i]))
    else:
        b[i]=np.sqrt(2*a[i])-1


plt.hist(b,10,density=True)
plt.show()
