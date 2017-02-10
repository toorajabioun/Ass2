# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 15:08:57 2017

@author: tooraj
"""
import math

def sort_count(y):
    m=0
    l=len(y)
    if l>2:
        l2=math.ceil(l/2)
        y1=y[:l2]
        y2=y[l2:]
        m1=sort_count(y1)  #left part
        m2=sort_count(y2)  #right part
        m+=m1+m2
        #crossing part:
        i,j=0,0
        for k in range(0,l):
            if y1[i]<=y2[j]:
                y[k]=y1[i]
                i+=1
                if i==l2:
                    y[k+1:]=y2[j:]
                    break
            else:
                y[k]=y2[j]
                j+=1
                m+=(l2-i)
                if j==l-l2:
                    y[k+1:]=y1[i:]
                    break
                
                
    elif l==2:
        if y[0]>y[1]:
            y[0],y[1]=y[1],y[0]
            m += 1
    return m

    
def sort_count_dumb(x):
    l=len(x)
    m=0
    for i in range(0,l-1):
        for j in range(i+1,l):
            if x[i]>x[j]:
                m+=1
    return m
    