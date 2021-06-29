#!/usr/bin/env python
# coding: utf-8

# In[ ]:


\def solution(lottos, win_nums):
    answer = []
    lowest = 0
    for num in win_nums:
        if num in lottos: lowest = lowest + 1 
    highest = lowest + lottos.count(0)
    answer.append(6) if (7 - highest) > 5 else answer.append(7-highest)
    answer.append(6) if (7 - lowest) > 5 else answer.append(7-lowest)
    return answer

