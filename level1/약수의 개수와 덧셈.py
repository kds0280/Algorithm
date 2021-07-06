#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(left, right):
    total = 0
    for i in range(left, right+1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count % 2 == 0:
            total += i
        else:
            total -= i
    return total

