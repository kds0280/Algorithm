#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(a, b):
    sum = 0
    
    if a == b:
        return a
    elif a > b: 
        a ,b = b, a
        
    for i in range(a, b+1):
        sum += i
        
    return sum

