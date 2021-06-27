#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(n):
    numbers = []
    answer = 0
    while n > 2:
        n, remainder = divmod(n,3)
        numbers.insert(0, remainder)
    numbers.insert(0, n)
    numbers.reverse()
    for i in range(len(numbers)):
        answer += numbers[i]*(3**(len(numbers)-(i+1)))
    return answer

