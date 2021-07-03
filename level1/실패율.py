#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import operator
def solution(N, stages):
    d = dict()
    num_stage_player = len(stages)
    
    for i in range(1,N+1):
        if stages.count(i) == 0:
            d[i] = 0
        else:
            d[i] = stages.count(i)/num_stage_player
            num_stage_player = num_stage_player-stages.count(i)
        
    sd = sorted(d.items(), key=lambda x:x[1], reverse=True)
    
    answer = [k for k, v in sd]
    return answer

