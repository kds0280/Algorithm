#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer = answer + a[i]*b[i]
    return answer

