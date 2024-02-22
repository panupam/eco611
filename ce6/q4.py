import numpy as np 

f=lambda x: 100*(x[1]-x[0]*x[0])**2 + (1-x[0])*(1-x[0])
g=lambda x: np.array([-400*(x[1]-x[0]*x[0])*x[0]-2*(1-x[0]),200*(x[1]-x[0]*x[0])])
x=np.array([0.5,0.5])
c=0.9
count=0

count_cg=0
d=-g(x)
while np.linalg.norm(g(x))>1e-6:
    alpha=0.001
    while f(x)+alpha*d.dot(g(x))>f(x+alpha*d):
        alpha=0.5*alpha
    x_p=x
    x=x+alpha*d
    print(x)
    if count_cg%2==0:
        d=-g(x)+g(x).dot(g(x))/g(x_p).dot(g(x_p)) *d 
        count_cg+=1
    else:
        d=-g(x)
        count_cg+=1
# while np.linalg.norm(g(x))>1e-6:
#     alpha=0.001
#     while f(x)-alpha*c*g(x)@g(x)>f(x-alpha*g(x)):
#         alpha=0.1*alpha
#         #print(alpha)

#     x=x-alpha*g(x)
#     count+=1
#     print(x)

print(count,x)

