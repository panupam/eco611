import numpy as np 
import numpy.random as random
import matplotlib.pyplot as plt 

a=random.rand(10000)
b=random.rand(10000)
c=np.zeros(10000)
for i in range(10000):
    c[i]=-np.log(a[i]*b[i])

plt.hist(c,density=True,bins=30)
plt.show()
