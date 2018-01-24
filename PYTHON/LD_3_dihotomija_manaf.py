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
b = 2
x = np.arange(a,b,0.01)
y = my_function(x)
plt.plot(x,y)
plt.grid()
#plt.show()

delta_x = 1.e-3 # 0.001 ir tas pats kas 1.e-3
funa = my_function(a)
funb = my_function(b)
if funa * funb > 0:
    print "[%.2f,%.2f] intervālā sakņu nav"%(a,b)
    print "vai šajā intervālā ir pāru sakņu skaits"
    exit()
print "Turpinajums, kad sakne ir:"
print "Vertības intervāla galapunktos - ",
print "f(%.2f)=%.2f un f(%.2f)=%.2f"%(a,funa,b,funb)

k = 0
while b-a > delta_x:
    k = k + 1
    x = (a+b)/2
    funx = my_function(x)
    print "%3d. a=%.5f f(%.5f)=%8.5f b=%.5f"%(k,a,x,funx,b)
    if funa *funx > 0:
        a = x
    else:
        b = x
print "Rezultāts:"
print "a=%.5f f(%.5f)=%12.9f b=%.9f"%(a,x,funx,b)
print "Aprēķins veikts ar %d iterācijam"%(k)
        
