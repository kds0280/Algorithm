#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(s):
    quotient = len(s)//2
    if len(s)%2 == 0:
        answer = s[quotient-1:quotient+1]
    else:
        answer = s[quotient]
    return answer

