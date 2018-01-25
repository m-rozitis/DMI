#!/usr/bin/python
# -*- coding: utf-8 -*-
#print formāti
# http://www.cplusplus.com/refrence/cstdio/printf
import numpy as np
import matplotlib.pyplot as plt

def mans_sinuss(x):
    k = 0
    a = (-1)**0*x**1/(1)
    S = a
    while k < 500:
        k = k + 1
        R = (-1)*x*x/((2*k)*(2*k+1))
        a = a * R
        S = S + a   
    return S

a = 0
b = 3 * np.pi
x = np.arange(a,b,0.05)
y = mans_sinuss(x)
plt.plot(x,y,label = u'sin x')
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
    
plt.plot(x[:n-1],y_prim,label = u'(sin x)`')
#plt.show()

y_primprim = []
for i in range(n-2):
    delta_y_prim = y_prim[i+1] - y_prim[i]
    y_primprim.append(delta_y_prim/delta_x)

plt.plot(x[:n-2],y_primprim,label = u'(sin x)``')
#plt.show()

plt.legend()
plt.show()
