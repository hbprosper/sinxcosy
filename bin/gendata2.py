#!/usr/bin/env python
#------------------------------------------------------------------------------
import os, sys
from math import *
from random import uniform
def main():
    N  = 100000
    z1 = 0.0
    z2 = 0.0
    x = [0]*N
    y = [0]*N
    z = [0]*N

    for i in xrange(N):
        x[i] = uniform(-2,2)
        y[i] = uniform(-2,2)
        z[i] = exp(sin(x[i]))* sin(5*x[i]) * cos(5*y[i])
        z1 += z[i]
        z2 += z[i]*z[i]
    z1 /= N
    z2 /= N
    z2 = sqrt(z2-z1*z1)

    out = open("function.var","w")
    out.write('x\t0\t1\n')
    out.write('y\t0\t1\n')
    out.write('z\t%f\t%f\n' % (z1, z2))
    out.close()
    
    out = open("function.dat","w")
    record = "%10s%10s%10s\n" % ("x", "y", "z")
    out.write(record)
    for i in xrange(N):
        record = "%10.4f%10.4f%10.4f\n" % (x[i], y[i], (z[i] - z1)/z2)
        out.write(record)
    out.close()
#------------------------------------------------------------------------------
main()

        

