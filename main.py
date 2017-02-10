# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 14:57:29 2017

@author: tooraj
"""
import numpy as np
import time
from fns import sort_count
from fns import sort_count_dumb
#input
#x=np.random.permutation(2000)
#x=[x[i]+1 for i in range(len(x))]
#x=[7,11, 3, 2,9, 4, 5,10, 1, 6,8]
lines = [line.rstrip('\n') for line in open('IntegerArray.txt')]
x=[int(h) for h in lines]

y=x[:]
t1=time.clock()
m=sort_count(y)
print('t1= '+str(time.clock()-t1))
print(m)

t1=time.clock()
n=sort_count_dumb(x)
print('t2= '+str(time.clock()-t1))

print(n)
