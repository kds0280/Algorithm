#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while scoville[0] < K:
        if len(scoville) == 1: 
            return -1        
        combine = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, combine)
        count += 1
    return count

