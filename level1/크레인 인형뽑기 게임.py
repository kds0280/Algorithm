#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(board, moves):
    doll = []
    count = 0
    for i in moves:
        for j in board:
            if (j[i-1]) != 0:
                doll.append(j[i-1])
                if len(doll) > 1:
                    if doll[-1] == doll[-2]:
                        del doll[-2:]
                        count = count + 2
                j[i-1] = 0
                break
    return count

