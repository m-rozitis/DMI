#!/usr/bin/python
# -*- coding: utf-8 -*-
#print formāti
# http://www.cplusplus.com/refrence/cstdio/printf
import numpy as np
import matplotlib.pyplot as plt


def my_function(x):
    k = 0
    a = 1*(k+1)
    S = a
    while k < 500:
        k = k + 1
        R = ((k+1)*x)/(k*k)
        a = a * R
        S = S + a
    return S

a = -2
b = 1
x = np.arange(a,b,0.05)
y = my_function(x)
plt.plot(x,y,label = u'(1+x)*exp(x)')
plt.grid()
#plt.show()

n = len(x)
y_prim = []
for i in range(n-1):
    #print i, x[i], y[i]
    delta_y = y[i+1] - y[i]
    delta_x = x[i+1] - x[i]
    #y_prim = delta_y/delta_x
    #print y_prim
    y_prim.append(delta_y/delta_x)
    
plt.plot(x[:n-1],y_prim,label = u'((1+x)*exp(x))`')
#plt.show()

y_primprim = []
for i in range(n-2):
    delta_y_prim = y_prim[i+1] - y_prim[i]
    y_primprim.append(delta_y_prim/delta_x)

plt.plot(x[:n-2],y_primprim,label = u'((1+x)*exp(x))``')
#plt.show()

plt.legend()
plt.show()
