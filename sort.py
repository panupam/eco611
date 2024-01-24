import numpy as np 
a=np.array([int(i) for i in input("Please enter the array:").split()])
for i in range(a.size):
    temp=a[i]
    
    for j in range(i+1):
        if a[j]>= temp:
            a=np.insert(a,j,temp)
            break
    
    a=np.delete(a,i+1)

print(a)