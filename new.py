#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 16:10:36 2024

@author: pranav
"""

def oddeven(x)-> (int):
    if x%2==0 : 
        return 99.0
    else: 
        return 0


#print(oddeven(10))

# (1+sqrt(5))/2  = 1.618

def gcd(a,b):
    if(a%b==0):
        return b
    else:
        return gcd(b,a%b)


gcd(14,7)
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-5,5,0.01)
y=x*x
# z=np.exp(x)
# plt.plot(x,y) 
# plt.plot(x,z)
# plt.plot(x,y,x,z)
# plt.show()

# plt.scatter(x, y)
# plt.show()

print(np.random.rand(10))
print(np.random.randn(10))
print(np.random.randint(1,6+1,100))