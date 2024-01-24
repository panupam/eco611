import numpy as np
import numpy.random as random 
import matplotlib.pyplot as plt

a=random.rand(1000)
b=np.zeros(1000)
p=np.sqrt(np.arange(1,5))
cdf=np.array([sum(p[:i+1])/sum(p) for i in range(4)])
b[a<=cdf[0]]=1
b[(a<=cdf[1])*(a>cdf[0])]=2
b[(a<=cdf[2])*(a>cdf[1])]=3
b[a>cdf[2]]=4

freq=np.array([])
for i in range(1,5):
    freq=np.append(freq,np.sum(b==i))

plt.bar(range(1,5),freq/1000)
plt.plot()



