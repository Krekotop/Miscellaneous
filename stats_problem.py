# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 22:44:13 2020

@author: fredh
Goal is to check the stats problem that I saw a while ago. 
We have uniformly distributed numbers from 0 to 1.
How many numbers, on average, do we have to take, in order for their sum to exceed 1?
The null hypothesis was that given expected outcome is 0.5, so on average it will be 2.
"""

import random 

def Average(lst): 
    return sum(lst) / len(lst)
sum1 = 0
number_of_tries = []
j=0
for i in range(100000):
    sum1 += random.uniform(0,1)
    j += 1
    if sum1 > 1:
        number_of_tries.append(j)
        sum1 = 0
        j = 0
print(Average(number_of_tries))

"""
We can conclude, that null hypothesis is rejected. Program is constantly giving number
very close to exponent, 2.718.
"""