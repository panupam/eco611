import numpy as np 

f=lambda x: x[0]*x[0]*np.exp(x[1])+ x[1]*x[1]*np.exp(x[0])
g=lambda x: np.array([2*x[0]*np.exp(x[1])+x[1]*x[1]*np.exp(x[0]),2*x[1]*np.exp(x[0])+x[0]*x[0]*np.exp(x[1])])
H=lambda x: np.array([[2*np.exp(x[1])+x[1]*x[1]*np.exp(x[0]),2*x[1]*np.exp(x[0])+2*x[0]*np.exp(x[1])],[2*x[1]*np.exp(x[0])+2*x[0]*np.exp(x[1]),2*np.exp(x[0])+x[0]*x[0]*np.exp(x[1])]])

x=np.array([1.0,1.0])
# Newtons method 
count_n=0
while np.linalg.norm(g(x))>1e-6:
    x=x-np.linalg.inv(H(x))@g(x)
    count_n+=1

# Gradiant descent Inexact line search 

x=np.array([1.0,1.0])
c=0.9
count_g=0
while np.linalg.norm(g(x))>1e-6:
    alpha=0.1 
    while (f(x)-alpha*g(x).dot(g(x))>f(x-alpha*g(x))):
        alpha=0.9*alpha
    
    x=x-alpha*g(x)
    count_g+=1


# Conjugate Gradient Inexact line search 
    
x=np.array([1.0,1.0])
c=0.7
count_cg=0
d=-g(x)
while np.linalg.norm(g(x))>1e-6:
    alpha=0.1
    while f(x)+alpha*d.dot(g(x))>f(x+alpha*d):
        alpha=0.9*alpha
    x_p=x
    x=x+alpha*d
    if count_cg%2==0:
        d=-g(x)+g(x).dot(g(x))/g(x_p).dot(g(x_p)) *d 
        count_cg+=1
    else:
        d=-g(x)
        count_cg+=1
    

print("Newton solves in {0} Gradient descent in {1} and conjugate gradient in{2}".format(count_n,count_g,count_cg))




