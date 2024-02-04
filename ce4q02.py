import numpy as np 

A=np.array([[2,3,7],[1,1,5],[4,3,1]])
e,ev=np.linalg.eig(A)
if min(e)>1e-5:
    print(A,"is a 'Positive Definite' matrix")
elif max(e)<-1e-5: 
    print(A,"is a 'negative Definite' matrix")
elif min(e)>-1e-5:
    print(A,"is a Positive Semi Definite Matrix")
    print(ev[:,e<1e-5], 'are vectors such that xTAx=0')
    print(ev[:,e>1e-5], 'are vectors such that xTAx!=0')
elif max(e)<1e-5:
    print(A,"is a Negative Semi Definite Matrix")
    print(ev[:,e>-1e-5], 'are vectors such that xTAx=0')
    print(ev[:,e<-1e-5], 'are vectors such that xTAx!=0')
else:
    print(A, "is indefinite")
    print(ev[:,e==max(e)],'is vactor such that xTAx>0', (ev[:,e==max(e)]).T @A@ev[:,e==max(e)])
    print(ev[:,e==min(e)],'is vactor such that xTAx<0',(ev[:,e==min(e)]).T @A@ev[:,e==min(e)])

