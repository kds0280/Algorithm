#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(d, budget):
    d.sort()
    count = 0
    for i in d:
        if i > budget:
            break
        else:
            budget -= i
            count += 1
    return count

