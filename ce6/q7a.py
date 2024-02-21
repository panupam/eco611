import numpy as np 

A=np.array([[1,0,-2,-1,0,4],[2,-1,1,0,-1,2],[3,-5,1,0,0,0]])

b=np.array([False,False,False,True,True])

lem=lambda A,b:A[-1,:-1][~b]-((np.linalg.inv(A[:-1,:-1][:,b])@A[:-1,:-1][:,~b]).T)@A[-1,:-1][b]

while  all(lem(A,b)<-1e-6):
    q=np.argmin(lem(A,b))
    #b[q]=True
    B,N=A[:-1,:-1][:,b],A[:-1,:-1][:,~b]
    
    bq=((np.linalg.inv(B)@N)[:,q]>0)
    if not any(bq):
        print("Unconstraint Optimization")
        break

    nq=np.argmin((np.linalg.inv(B)@A[:-1,-1])[bq]/(np.linalg.inv(B)@N)[:,q][bq])
    b[~b][q],b[b][nq]=True,False

x=np.zeros(5)
x[b]=np.linalg.inv(A[:-1,:-1][:,b])@A[:-1,-1]
print(x,A[-1,:-1]@x)

