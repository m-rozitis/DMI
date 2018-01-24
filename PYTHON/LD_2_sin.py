#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import sin

def mans_sinuss(x):
    k = 0
    a = (-1)**0*x**1/(1)
    S = a
    print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)

    while k < 500:
        k = k + 1
        R = (-1)*x*x/((2*k)*(2*k+1))
        a = a * R
        S = S + a
        if k == 499:
            print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)
        elif k == 500:
            print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)
        #print "Izdruka no liet.f. Beigas!"
    return "Sin(%.2f) caur summu: %.2f"%(x,S)


x = 1. * input("Lietotāj, lūdzu, ievadi argumentu (x): ")

y = sin(x)
print "standarta sin(%.2f) = %6.2f"%(x,y)

print ""
print "mana funkcija:"
print mans_sinuss(x)
print ""
print "                     500"
print "                    ______"
print "                   \     /    k    2*k+1"
print "                    \      (-1) * x"
print "y(%.1f)=sin(%.1f) =  >    _______________"%(x,x)
print "                    /         (2*k+1)!"
print "                   /_____\ "
print "                     k=0"
print ""
print "rekurences reizinātājs:"
print ""
print "             2"
print "       (-1)*x"
print " R =  _____________"
print "       2*k*(2*k+1)"
