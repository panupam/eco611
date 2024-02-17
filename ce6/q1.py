import numpy as np 
z1=False
for i in range(100): 
    X=np.random.randint(-9,10,25).reshape(5,5)
    A= X@X.T+ np.diag([1,1,1,1,1])
    c=np.random.randint(-9,10,5)
    z=False
    g= lambda A,c,x: A@x+c
    x=np.random.randint(0,100,5)
    d=-g(A,c,x)
    count=0
    while np.linalg.norm(g(A,c,x))>1e-6:
        x_p=x.copy()
        x=x-((g(A,c,x).dot(d))/(d.dot(A.dot(d))))*d
        #print(x)
        if np.linalg.norm(g(A,c,x))<1e-6:
            break
        if count%5<4 :
            d=-g(A,c,x) + (g(A,c,x).dot(g(A,c,x))/ g(A,c,x_p).dot(g(A,c,x_p))) *d
            count+=1
        else:
            d=-g(A,c,x)
            z=True
            count+=1
        
    if z:
        print("No, solution doesn't converge in 5 step for",A,c,count)
        z1=True
        




    
if not z1:
    print("Verified that all solution converges in 5 steps")


        

    
    
