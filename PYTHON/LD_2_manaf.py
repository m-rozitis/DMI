#!/usr/bin/python
#-*- coding: utf-8 -*-
import math
x = 1. * input("Lietotāj, lūdzu, ievadi argumentu (x): ")


y = (1+(x))*math.exp(x)
print "(1+(%.2f))*exp(%.2f) = %.2f"%(x,x,y)

def my_function(x):
    k = 0
    a = 1*(k+1)
    S = a
    print "a%d = %.2f S%d = %6.2f"%(k,a,k,S)
    while k < 500:
        k = k + 1
        R = ((k+1)*x)/(k*k)
        a = a * R
        S = S + a
        if k == 499:
            print "a%d = %.2f S%d = %6.2f"%(k,a,k,S)
        elif k == 500:
            print "a%d = %.2f S%d = %6.2f"%(k,a,k,S)
    return "(1+(%.2f))*exp(%.2f) caur summu: %.2f"%(x,x,S)

print " "
print "                               1000"
print "                               _____"
print "                              \     /           k"
print "                               \       (k+1) * x"
print "y(%.2f)=(1+(%.2f))*exp(%.2f)  = >    _____________"%(x,x,x)
print "                               /"
print "                              /_____\      k!"
print "                                k=0"
print "rekurences reizinātājs:"
print ""
print "       (k+1)*x"
print " R =  _________"
print "           2"
print "          k "
print ""
print my_function(x)
