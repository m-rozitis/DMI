#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import sin
x = 1. * input("Lietotāj, lūdzu, ievadi argumentu (x): ")


y = sin(x)
print "sin(%.2f) = %.2f"%(x,y)

k = 1
a = (-1)**0*x**1/(1)
S = a
print "a0 = %.2f S0 = %.2f"%(a,S)

#a = a * (-1)*x*x/(2*3)
a = a * (-1)*x*x/((2*k)*(2*k+1))
S = S + a
#print "a1 = %.2f S1 = %.2f"%(a,S)
print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)


#a = a * (-1)*x*x/(4*5)
a = a * (-1)*x*x/((2*k)*(2*k+1))
S = S + a
#print "a2 = %.2f S2 = %.2f"%(a,S)
print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)


#a = a * (-1)*x*x/(6*7)
a = a * (-1)*x*x/((2*k)*(2*k+1))
S = S + a
#print "a3 = %.2f S3 = %.2f"%(a,S)
print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)
