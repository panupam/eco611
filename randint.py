import numpy as np
import numpy.random as random 
import matplotlib.pyplot as plt

a=random.randint(1,11,1000)
b=np.zeros(1000)

b[a==1]=1
b[(a<=3)* ( a>1)]=2
b[(a<=6)* ( a>3)]=3
b[ a>6]=4

# for i in range(a.size):
#     if a[i]<=1:
#         b=np.append(b,1)
#     elif a[i]<=3:
#         b=np.append(b,2)
#     elif a[i]<=6:
#         b=np.append(b,3)
#     else:
#         b=np.append(b,4)
        
freq=np.array([])
for i in range(1,5):
    freq=np.append(freq,np.sum(b==i))

plt.bar(range(1,5),freq/1000)
plt.plot()

