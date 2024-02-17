import numpy as np 
import matplotlib.pyplot as plt
l=[]
for a in np.arange(-1.9,2.0,0.1):
    
    H=np.array([[2,a],[a,2]])
    x=np.array([200,25])
    g= lambda H,x: H@x
    d=-g(H,x)
    count=0
    while np.linalg.norm(g(H,x))>1e-6:
        x_p=x.copy()
        x=x-((g(H,x).dot(d))/(d.dot(H.dot(d))))*d
        #print(x)
        if count%5<4 :
            d=-g(H,x) + (g(H,x).dot(g(H,x))/ g(H,x_p).dot(g(H,x_p))) *d
            count+=1
        else:
            d=-g(H,x)
            count+=1
    
    l.append((a,count))
z=np.array(l)
plt.plot(z[:,0],z[:,1])
plt.show()

            
        