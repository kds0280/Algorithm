#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(arr):
    list = []
    list.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            list.append(arr[i])
    
    return list

