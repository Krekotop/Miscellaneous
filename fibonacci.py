# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 22:54:51 2019

@author: User
"""
import numpy

def fib1(n):
    seq=numpy.zeros(n)
    seq[0]=seq[1]=1
    for i in range(2,n):
        seq[i]=seq[i-1]+seq[i-2]
    return seq[n-1]
a = int(input("Which number in Fibonacci sequence you want to see?\n"))
print(fib1(a))