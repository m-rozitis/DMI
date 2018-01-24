#!/usr/bin/python
#-*- coding: utf-8 -*-
import math

def my_function(x):
    k = 0
    a = 1*(k+1)
    S = a
    print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)
    
    while k < 500:
        k = k + 1
        R = ((k+1)*x)/(k*k)
        a = a * R
        S = S + a
        if k == 499:
            print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)
        elif k == 500:
            print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)
    return "(1+(%.2f))*exp(%.2f) caur summu: %.2f"%(x,x,S)


x = 1. * input("Lietotāj, lūdzu, ievadi argumentu (x): ")

y = (1+(x))*math.exp(x)
print "standarta (1+(%.2f))*exp(%.2f) = %.2f"%(x,x,y)

print ""
print "mana funkcija:"
print my_function(x)
print ""
print "                               1000"
print "                              ______"
print "                              \     /"
print "                               \      (k+1) * x"
print "y(%.1f)=(1+(%.1f))*exp(%.1f)  = >    ___________"%(x,x,x)
print "                               /          k!"
print "                              /_____\ "
print "                                k=0"
print ""
print "rekurences reizinātājs:"
print ""
print "       (k+1)*x"
print " R =  _________"
print "           2"
print "          k "

